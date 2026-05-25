# Cached Artifacts

This directory provides a low-cost reproduction path for the paper tables and figures.
The cached files are derived outputs: they do not include raw benchmark audio or model checkpoints.

- `scores/table1_behavior_summary.csv`: paper-facing behavioral summary for repairable arbitration reversal.
- `scores/main_results.csv`: cached Joint/AAD/ACD/GACL main-result rows with source paths anonymized.
- `scores/macro_results.csv`: macro averages over the cached main-result rows.
- `scores/score_cache_r1p2_5m4t.jsonl`: candidate-score cache for same-audio reference and joint branches.
- `scores/margin_rows_r005.jsonl`: sanitized margin rows for the repairable-quadrant scatter plot.
- `patch_results/*.csv`: cached activation-patching and patch-score-alignment summaries.

Additional cached tables added for main-paper coverage:

- `scores/main_nauc_results.csv`: nAUC table for AAD, ACD, and GACL under 0--5 and 0--10 pp budgets.
- `scores/fig5_frontier_bootstrap.csv`: paper-facing 0--50 pp rescue-faithfulness frontier with 95% bootstrap bands over model-task configurations.
- `scores/aad_acd_selected_results.csv`: selected AAD/ACD operating points.
- `scores/dola_sanity.csv`: one-cell DoLa sanity check.
- `scores/component_diagnostic.csv`: component-ablation diagnostic table.
- `scores/sft_comparison.csv`: SFT comparison table.
- `scores/mc2_g2/`: fixed-parameter MC2 transfer summary plus auxiliary per-sample endpoint caches for the two-model G2 prefix-trie generation evaluation.
- `scores/gate_proxy_fidelity.csv`: gate/proxy coverage and precision table.
