#!/usr/bin/env python3
"""One-command public demo for GACL.

Reads the precomputed score artifacts bundled under data/cached/ and prints the
headline paper tables. Use --figures to also regenerate Figures 2, 3, and 5.
"""
from __future__ import annotations

import argparse
import csv
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCORES = ROOT / "data" / "cached" / "scores"
PATCH = ROOT / "data" / "cached" / "patch_results"


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def pct(value: str | float) -> float:
    return 100.0 * float(value)


def fmt(value: str | float, digits: int = 1) -> str:
    return f"{float(value):.{digits}f}"


def print_main_results() -> None:
    rows = read_csv(SCORES / "macro_results.csv")
    by_method = {row["method"]: row for row in rows}
    print("\nMain results (macro over audio-text conflict cells)")
    print("  method       conflict acc   gain vs Joint   faithful acc   faithful drop")
    for method in ["Joint", "AAD@5pp", "ACD@5pp", "GACL@5pp"]:
        row = by_method.get(method)
        if row is None:
            continue
        print(
            f"  {method:<12} {pct(row['mean_test_conflict_acc']):>10.1f}% "
            f"{pct(row['mean_gain_vs_joint']):>+14.1f}pp "
            f"{pct(row['mean_test_aligned_acc']):>12.1f}% "
            f"{pct(row['mean_aligned_drop']):>14.1f}pp"
        )


def print_behavior() -> None:
    rows = read_csv(SCORES / "table1_behavior_summary.csv")
    print("\nReversal diagnostics")
    print("  task    faithful acc   conflict acc   text-follow   audio-ref acc   repairable")
    for row in rows:
        print(
            f"  {row['task']:<7} {fmt(row['faithful']):>10}% "
            f"{fmt(row['conflict']):>11}% {fmt(row['text_follow']):>12}% "
            f"{fmt(row['audio_ref_acc']):>13}% {fmt(row['repairable_quadrant']):>10}%"
        )


def print_nauc() -> None:
    rows = read_csv(SCORES / "main_nauc_results.csv")
    gacl = [row for row in rows if row["method"] == "GACL"]
    if not gacl:
        return
    print("\nGACL nAUC under a 5 pp faithful-drop budget")
    print("  model               GACL nAUC")
    for row in gacl:
        print(f"  {row['model']:<20} {row['avg_0_5']:>9}")


def print_mc2() -> None:
    rows = read_csv(SCORES / "mc2_g2" / "fixed_lam0p5_tau0p5_summary.csv")
    joint = {row["model"]: row for row in rows if row["method"] == "Joint baseline"}
    gacl = {row["model"]: row for row in rows if row["method"] == "GACL (fixed)"}
    print("\nMC2 vision-text transfer (fixed GACL)")
    print("  model          Joint vision-follow   GACL vision-follow   gain")
    for model in sorted(joint):
        if model not in gacl:
            continue
        j = float(joint[model]["conflict_vision_follow"])
        g = float(gacl[model]["conflict_vision_follow"])
        print(f"  {model:<14} {j:>19.1f}% {g:>19.1f}% {g - j:>+7.1f}pp")


def print_component() -> None:
    rows = read_csv(SCORES / "component_diagnostic.csv")
    full = next((row for row in rows if row["variant"] == "GACL (full)"), None)
    if full is None:
        return
    print("\nAblation headline (GACL full)")
    print(
        f"  MC drop @5pp: {full['mcq_drop_5pp']}pp | "
        f"rescue gain: {full['avg_rescue_gain']}pp | "
        f"free-form surface preserve: {full['free_form_surface_preserve']}%"
    )


def make_figures() -> None:
    print("\nRegenerating figures into assets/figures/ ...")
    for module in [
        "src.plotting.plot_fig2_margins",
        "src.plotting.plot_fig3_bridge",
        "src.plotting.plot_fig5_frontier",
    ]:
        subprocess.run([sys.executable, "-m", module], cwd=ROOT, check=True)
    print("done")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--figures", action="store_true", help="also regenerate paper Figures 2, 3, and 5")
    args = parser.parse_args()

    print("GACL — Beyond Text Following: Repairable Arbitration Reversals in Audio-Language Models")
    print_main_results()
    print_behavior()
    print_nauc()
    print_mc2()
    print_component()
    if args.figures:
        make_figures()


if __name__ == "__main__":
    main()
