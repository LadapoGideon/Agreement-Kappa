"""Measure how well two annotators agree, beyond what chance would produce."""
from collections import Counter


def percent_agreement(rater_a, rater_b):
    _check_lengths(rater_a, rater_b)
    return sum(a == b for a, b in zip(rater_a, rater_b)) / len(rater_a)


def cohens_kappa(rater_a, rater_b):
    """
    Cohen's kappa: 1.0 is perfect agreement, 0 is what chance alone would give,
    and negative values mean the raters disagree more than chance.
    """
    _check_lengths(rater_a, rater_b)
    n = len(rater_a)
    observed = percent_agreement(rater_a, rater_b)

    counts_a = Counter(rater_a)
    counts_b = Counter(rater_b)
    labels = set(counts_a) | set(counts_b)
    expected = sum((counts_a[label] / n) * (counts_b[label] / n) for label in labels)

    if expected == 1.0:
        return 1.0
    return (observed - expected) / (1 - expected)


def _check_lengths(rater_a, rater_b):
    if len(rater_a) != len(rater_b):
        raise ValueError("both raters must label the same number of items")
    if not rater_a:
        raise ValueError("no labels given")
