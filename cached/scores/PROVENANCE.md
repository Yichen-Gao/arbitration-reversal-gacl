# Score Cache Provenance

The cached score files are anonymized exports from the experiment artifacts.
CSV fields use anonymized paths and run names.

Use:

```bash
bash scripts/reproduce_table1.sh --cached
bash scripts/reproduce_table3.sh --cached
bash scripts/reproduce_fig5.sh --cached
bash scripts/run_gacl_cached.sh --limit 20
```

`fig5_frontier_bootstrap.csv` is the anonymized paper-facing curve export for
Figure 5: macro frontier values over 20 model-task cells with 1000 bootstrap
resamples and raw faithful-drop caps from 0 to 50 percentage points.

ACD uses a perturbed-audio reference branch. Cached CSVs store the selected
operating points and frontier values used by the paper-facing tables/figures.

The full inference path requires downloading upstream benchmarks and public Hugging Face checkpoints listed in `configs/models.yaml`.
