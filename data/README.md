# Data

This directory contains dataset preparation scripts, public split IDs, and the precomputed score artifacts used by the GACL demo.

## Cached score artifacts

`data/cached/` ships the paper-facing results as compact CSV/JSONL scores. It does not redistribute raw audio, images, or model weights.

- `scores/main_results.csv` — per-model, per-task Joint / AAD / ACD / GACL results.
- `scores/macro_results.csv` — macro averages across audio-text conflict cells.
- `scores/table1_behavior_summary.csv` — reversal and repairability diagnostics.
- `scores/main_nauc_results.csv` — nAUC operating points under 0--5 pp and 0--10 pp budgets.
- `scores/mc2_g2/` — MC2 vision-text transfer results.
- `patch_results/` — activation-patching and patch-score-alignment summaries used by Figure 3.

## Full-inference data

Full model inference uses the upstream benchmarks below, then the split IDs in `data/splits/`.

| Dataset | Use | Source |
| --- | --- | --- |
| MCR-Bench | AQA, VSC, SER audio-text conflict tasks | https://github.com/WangCheng0116/MCR-BENCH |
| MCR-Bench archive | Raw MCR-Bench manifests/audio | https://drive.google.com/file/d/1nXJCx8Neqdm0WMfe9Uq6sX2bvk_3FWUG/view?usp=sharing |
| ALME | ALME-English transcript/audio conflict task | https://github.com/jb1999/alme-benchmark |
| Common Voice 22.0 | Natural speech backing ALME | https://commonvoice.mozilla.org/en/datasets |
| MC2 | Optional vision-text transfer experiment | https://huggingface.co/datasets/271754echo/MC2 |

```bash
bash data/download_mcrbench.sh
bash data/download_alme.sh
bash data/download_mc2.sh
```

Expected local layout:

```text
data/raw/mcrbench/
data/raw/alme/
data/raw/common_voice/cv-corpus-22.0-2025-06-20/
data/raw/mc2/
```

The bundled demo does not require these downloads.
