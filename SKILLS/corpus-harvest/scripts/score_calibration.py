#!/usr/bin/env python3
"""Deterministically score one calibration result against a task rubric."""

import argparse
import json
import os
import sys


COUNT_FIELDS = (
    "actual_tokens", "target_hits", "target_total",
    "primary_repertoire_correct", "primary_repertoire_total",
    "fabrications", "attribution_errors", "misroutes", "evaluated_rows",
    "quote_matches", "quote_total",
)
DENOMINATORS = (
    "target_total", "primary_repertoire_total", "evaluated_rows",
    "quote_total",
)


class MetricsError(ValueError):
    pass


def load_json(path):
    with open(path, encoding="utf-8") as handle:
        return json.load(handle)


def validate_metrics(metrics):
    if not isinstance(metrics, dict):
        raise MetricsError("metrics must be a JSON object")
    if not isinstance(metrics.get("candidate"), str) or not metrics["candidate"].strip():
        raise MetricsError("candidate must be a non-empty string")
    for field in COUNT_FIELDS:
        value = metrics.get(field)
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise MetricsError(f"{field} must be a nonnegative integer")
    for field in DENOMINATORS:
        if metrics[field] == 0:
            raise MetricsError(f"{field} must be greater than zero")
    pairs = (
        ("target_hits", "target_total"),
        ("primary_repertoire_correct", "primary_repertoire_total"),
        ("misroutes", "evaluated_rows"),
        ("quote_matches", "quote_total"),
    )
    for numerator, denominator in pairs:
        if metrics[numerator] > metrics[denominator]:
            raise MetricsError(f"{numerator} cannot exceed {denominator}")


def derived_metrics(metrics):
    return {
        "target_recall": metrics["target_hits"] / metrics["target_total"],
        "primary_repertoire_accuracy": (
            metrics["primary_repertoire_correct"]
            / metrics["primary_repertoire_total"]
        ),
        "fabrications": metrics["fabrications"],
        "attribution_errors": metrics["attribution_errors"],
        "misroute_rate": metrics["misroutes"] / metrics["evaluated_rows"],
        "quote_fidelity": metrics["quote_matches"] / metrics["quote_total"],
    }


def compare(actual, operator, threshold):
    if operator == "gte":
        return actual >= threshold
    if operator == "lte":
        return actual <= threshold
    if operator == "eq":
        return actual == threshold
    raise MetricsError(f"unknown rubric operator: {operator}")


def score(mode, metrics, rubric):
    validate_metrics(metrics)
    values = derived_metrics(metrics)
    try:
        mode_spec = rubric[mode]
        rule_specs = mode_spec["rules"]
    except (KeyError, TypeError) as error:
        raise MetricsError(f"rubric has no valid {mode!r} rules") from error
    rules = {}
    for name, spec in rule_specs.items():
        if name not in values:
            raise MetricsError(f"rubric names unknown metric: {name}")
        if not isinstance(spec, dict):
            raise MetricsError(f"rubric rule {name} must be an object")
        operator = spec.get("operator")
        threshold = spec.get("threshold")
        if (isinstance(threshold, bool)
                or not isinstance(threshold, (int, float))):
            raise MetricsError(f"rubric rule {name} threshold must be numeric")
        passed = compare(values[name], operator, threshold)
        rules[name] = {
            "passed": passed,
            "actual": values[name],
            "operator": operator,
            "threshold": threshold,
        }
    failed = [name for name, result in rules.items() if not result["passed"]]
    return {
        "candidate": metrics["candidate"],
        "mode": mode,
        "passed": not failed,
        "actual_tokens": metrics["actual_tokens"],
        "metrics": values,
        "rules": rules,
        "failed_rules": failed,
        "diagnostic_only": True,
    }


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", required=True, choices=("survey", "extraction"))
    parser.add_argument("--metrics", required=True)
    parser.add_argument(
        "--rubric",
        default=os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "..", "references", "CALIBRATION_RUBRICS.json"),
    )
    args = parser.parse_args(argv)
    try:
        result = score(args.mode, load_json(args.metrics), load_json(args.rubric))
    except (OSError, json.JSONDecodeError, MetricsError) as error:
        print(f"REFUSED: invalid metrics or rubric: {error}", file=sys.stderr)
        return 2
    json.dump(result, sys.stdout, indent=2, sort_keys=True)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
