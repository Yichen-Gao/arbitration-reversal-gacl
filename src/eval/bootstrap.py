"""Small bootstrap helper used by optional analyses."""
from __future__ import annotations

import random
from typing import Callable, Sequence


def bootstrap_ci(values: Sequence[float], statistic: Callable[[list[float]], float] | None = None, n_resamples: int = 1000, seed: int = 0) -> tuple[float, float, float]:
    if not values:
        raise ValueError("values must be non-empty")
    statistic = statistic or (lambda xs: sum(xs) / len(xs))
    rng = random.Random(seed)
    stats = []
    values = list(map(float, values))
    for _ in range(n_resamples):
        sample = [values[rng.randrange(len(values))] for _ in values]
        stats.append(statistic(sample))
    stats.sort()
    return statistic(values), stats[int(0.025 * n_resamples)], stats[int(0.975 * n_resamples) - 1]
