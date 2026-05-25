# Data Preparation

Cached reproduction uses the included score files. Full inference uses the upstream datasets listed below, then applies the split IDs in `data/splits/`.

## Upstream Sources

| Dataset | Used for | Upstream link |
| --- | --- | --- |
| MCR-Bench | AQA, VSC, SER audio-text conflict tasks | https://github.com/WangCheng0116/MCR-BENCH |
| MCR-Bench data archive | Raw MCR-Bench manifests/audio | https://drive.google.com/file/d/1nXJCx8Neqdm0WMfe9Uq6sX2bvk_3FWUG/view?usp=sharing |
| ALME | ALME-English transcript/audio conflict task | https://github.com/jb1999/alme-benchmark |
| Common Voice Corpus 22.0 | Natural speech backing ALME | https://commonvoice.mozilla.org/en/datasets |
| MC2 | Optional vision-text transfer experiment | https://huggingface.co/datasets/271754echo/MC2 |

## Helper Commands

```bash
bash data/download_mcrbench.sh
bash data/download_alme.sh
bash data/download_mc2.sh
```

The expected local layout is:

```text
data/raw/mcrbench/
data/raw/alme/
data/raw/common_voice/cv-corpus-22.0-2025-06-20/
data/raw/mc2/
```

Cached reproduction commands do not need raw data:

```bash
bash scripts/reproduce_table1.sh --cached
bash scripts/reproduce_fig2.sh --cached
bash scripts/reproduce_table3.sh --cached
bash scripts/reproduce_fig3.sh --cached
```
