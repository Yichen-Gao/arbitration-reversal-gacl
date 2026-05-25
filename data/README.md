# Data Preparation

This anonymous artifact does not redistribute raw audio, images, or benchmark files.
Download the upstream datasets from their official sources, then use the split IDs in `data/splits/` to select the paper subsets.

Expected sources:

- MCR-Bench for AQA, VSC, and SER audio-text conflict tasks.
- ALME-English for transcript/audio conflict evaluation.
- MC2 for the optional vision-text transfer experiment.

The cached reproduction scripts do not require raw data:

```bash
bash scripts/reproduce_table1.sh --cached
bash scripts/reproduce_fig2.sh --cached
bash scripts/reproduce_table3.sh --cached
bash scripts/reproduce_fig3.sh --cached
```
