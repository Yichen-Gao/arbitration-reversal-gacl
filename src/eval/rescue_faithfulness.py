"""Rescue-faithfulness frontier and normalized AUC utilities."""
from __future__ import annotations


def frontier(points: list[tuple[float, float]], budgets: list[float]) -> list[tuple[float, float]]:
    """Return best conflict gain under each faithful-drop budget.

    points are (faithful_drop, conflict_gain), both in percentage points.
    """
    out = []
    for budget in budgets:
        feasible = [gain for drop, gain in points if drop <= budget]
        out.append((budget, max(feasible) if feasible else 0.0))
    return out


def normalized_auc(frontier_points: list[tuple[float, float]], max_gain: float = 100.0) -> float:
    if len(frontier_points) < 2:
        return 0.0
    area = 0.0
    for (x0, y0), (x1, y1) in zip(frontier_points[:-1], frontier_points[1:]):
        area += (x1 - x0) * (y0 + y1) / 2.0
    width = frontier_points[-1][0] - frontier_points[0][0]
    return 0.0 if width <= 0 else area / (width * max_gain)
