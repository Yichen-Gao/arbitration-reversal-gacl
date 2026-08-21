from pathlib import Path

from src.analysis.patch_score_alignment import spearman_from_csv


def test_cached_patch_alignment_positive():
    rho = spearman_from_csv(Path("data/cached/patch_results/panel_a_qwen2_audio_aqa_scatter.csv"))
    assert rho > 0.8
