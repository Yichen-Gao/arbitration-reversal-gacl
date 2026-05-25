# GACL Anonymous Reproduction Package

This repository contains the reproduction package for **Gated Audio Counterfactual Logit Correction (GACL)**, including cached scores, plotting scripts, baseline summaries, and method implementations for the paper's main results.

## 1. Overview

GACL targets repairable arbitration reversals in audio-language models: the joint audio-text branch follows conflicting text, while a same-audio reference branch recovers the audio-supported answer. The method computes a sample-level gate and applies a bounded interpolation from joint scores toward same-audio reference scores.

The core equation implemented in `src/methods/gacl.py` is:

```text
alpha(x) = clip(lambda * R_A(x) * N_out(x), 0, 1)
s_GACL(y) = s_J(y) + alpha(x) * (s_A(y) - s_J(y))
```

## 2. Installation

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

A conda environment file is also provided:

```bash
conda env create -f environment.yml
conda activate anonymous-gacl
```

## 3. Data Preparation

Cached reproduction uses the included score files. Full inference uses the upstream benchmarks and the split IDs in `data/splits/`.

```bash
bash data/download_mcrbench.sh
bash data/download_alme.sh
```

Raw benchmark audio/images and model checkpoints are downloaded from their upstream sources.

## 4. Quick Reproduction With Cached Scores

Run all cached artifacts from the repository root:

```bash
bash scripts/reproduce_all_cached.sh
```

Or run individual commands:

```bash
bash scripts/reproduce_table1.sh --cached
bash scripts/reproduce_fig2.sh --cached
bash scripts/reproduce_main_nauc_table.sh
bash scripts/reproduce_table3.sh --cached
bash scripts/reproduce_fig5.sh --cached
bash scripts/reproduce_table2.sh --cached
bash scripts/reproduce_fig3.sh --cached
bash scripts/reproduce_component_table.sh
bash scripts/reproduce_sft_table.sh
bash scripts/reproduce_mc2_table.sh
bash scripts/reproduce_gate_proxy_table.sh
bash scripts/reproduce_baselines.sh
```

Generated outputs:

```text
results/expected_table1.csv
results/expected_fig2.pdf
results/expected_main_nauc_table.csv
results/expected_table3.csv
results/expected_fig5.pdf
results/expected_table2.csv
results/expected_fig3.pdf
results/expected_component_table.csv
results/expected_sft_table.csv
results/expected_mc2_table.csv
results/expected_gate_proxy_table.csv
results/expected_aad_acd_selected_results.csv
results/expected_dola_sanity.csv
```

You can also exercise the GACL formula over cached candidate scores:

```bash
bash scripts/run_gacl_cached.sh --limit 20
```

## 5. Full Inference Reproduction

Full inference uses public Hugging Face checkpoints, upstream datasets, and model-specific adapters. The model roster and revision prefixes are listed in `configs/models.yaml`.

Example interface:

```bash
bash scripts/run_gacl_full.sh --model qwen2_audio --task aqa
bash scripts/run_aad_acd.sh --model qwen2_audio --task aqa
```

Cached reproduction is the default path for regenerating the reported tables and figures.

## 6. Reproducing Cached Tables and Figures

- Table 1 behavior summary: `bash scripts/reproduce_table1.sh --cached`
- Figure 2 margin scatter: `bash scripts/reproduce_fig2.sh --cached`
- Main nAUC table: `bash scripts/reproduce_main_nauc_table.sh`
- Appendix selected operating-point summary: `bash scripts/reproduce_table3.sh --cached`
- Figure 5 rescue-faithfulness frontier: `bash scripts/reproduce_fig5.sh --cached`
- Component-ablation table: `bash scripts/reproduce_component_table.sh`
- SFT comparison table: `bash scripts/reproduce_sft_table.sh`
- MC2 two-model G2 fixed-GACL transfer table: `bash scripts/reproduce_mc2_table.sh --cached`
- AAD/ACD/DoLa baseline artifacts: `bash scripts/reproduce_baselines.sh`
- Table 2 site-localization summary: `bash scripts/reproduce_table2.sh --cached`
- Figure 3 mechanism-to-output bridge: `bash scripts/reproduce_fig3.sh --cached`

Cached inputs are documented in `cached/README.md` and `cached/*/PROVENANCE.md`.
The cached path covers the quantitative main tables and Figures 2/3/5.

## MC2 note

The MC2 transfer result uses the G2 prefix-trie constrained short-label generation protocol on two Qwen3-VL backbones. The paper-facing table uses fixed GACL with `lambda=0.5` and `tau_A=0.5`: Qwen3-VL-2B improves from 43.0 to 83.5 (+40.5 pp), and Qwen3-VL-8B improves from 55.5 to 82.0 (+26.5 pp). Cached fixed summaries and auxiliary per-sample endpoint outputs are included under `cached/scores/mc2_g2/`.

## 7. Activation Patching Analysis

Activation patching entry points are in `src/analysis/activation_patching.py`; cached summaries in `cached/patch_results/` redraw Figure 3 and the site-localization table.

```bash
bash scripts/run_patching.sh
bash scripts/reproduce_fig3.sh --cached
```

## 8. Expected Results

The cached outputs reproduce the reported values:

- Same-audio reference recovers 76.6% macro audio-reference accuracy in Table 1.
- The strict repairable quadrant covers 64.1% of conflict samples in Table 1.
- GACL improves conflict accuracy over Joint/AAD/ACD in the cached main-result table.
- Fixed GACL transfers to MC2 G2 on two Qwen3-VL models, with up to +40.5 pp adversarial gain at near-zero faithful cost.
- Patch-to-output alignment is high in the representative cached Figure 3 scatter.

## 9. Repository Structure

```text
configs/      model, task, method, and prompt configuration
cached/       anonymized score and patch-result caches
data/         data download helpers and split IDs
src/          GACL, baseline, evaluation, analysis, and plotting code
scripts/      reproduction commands
results/      generated outputs from cached reproduction scripts
tests/        lightweight unit tests for formula and cached scripts
```

## 10. Citation

Anonymous submission. Citation metadata will be added after review.
