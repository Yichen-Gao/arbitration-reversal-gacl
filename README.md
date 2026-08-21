# Beyond Text Following: Repairable Arbitration Reversals in Audio-Language Models

[![arXiv](https://img.shields.io/badge/arXiv-2606.05161-b31b1b.svg)](https://arxiv.org/abs/2606.05161)
![EMNLP 2026 Main](https://img.shields.io/badge/EMNLP_2026-Main-2ea44f.svg)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

<p align="center">
  <img src="assets/fig1.png" alt="GACL overview" width="100%" />
</p>

**GACL** (Gated Audio Counterfactual Logit Correction) is a training-free decoding rule that repairs arbitration reversals in audio-language models. When conflicting text overrides clear audio evidence, GACL recovers the audio-supported answer at inference time — no fine-tuning, no gradients, no extra model weights.

```text
alpha(x) = clip(lambda * R_A(x) * N_out(x), 0, 1)
s_GACL(y) = s_J(y) + alpha(x) * (s_A(y) - s_J(y))
```

## Highlights

| Number | What it means |
| --- | --- |
| **64.1%** | of conflict samples contain a repairable sign flip: the audio answer is present, but text wins arbitration |
| **76.6%** | macro audio-reference accuracy recovered by the same-audio branch |
| **+41.7 pp** | macro conflict accuracy over Joint, at a **4.2 pp** faithful-accuracy drop |
| **+17.8 pp** | nAUC over the best contrastive baseline under a strict 5 pp faithful-drop budget |
| **+40.5 pp** | MC2 vision-text transfer without retuning, on Qwen3-VL-2B |
| **0.93** | Spearman rho between patch effects and output candidate-score differences |

GACL is evaluated across five audio-language models and four audio-text conflict tasks, with a cross-modal MC2 transfer experiment.

## Quick Start

```bash
git clone https://github.com/Yichen-Gao/arbitration-reversal-gacl.git
cd arbitration-reversal-gacl
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python scripts/demo.py
```

The demo prints the main tables from the bundled score artifacts in `data/cached/` — no dataset download or GPU required. To regenerate paper Figures 2, 3, and 5:

```bash
python scripts/demo.py --figures
```

For a minimal GACL scoring example:

```bash
python scripts/run_gacl_cached.py --limit 20
```

## Repository Layout

- `src/methods/` — GACL, AAD, ACD, and DoLa scoring rules.
- `src/eval/` — metrics, bootstrap, margins, and rescue-faithfulness utilities.
- `src/plotting/` — paper figure generators.
- `configs/` — model, task, baseline, and hyperparameter settings.
- `data/cached/` — precomputed paper-facing score artifacts.
- `data/` — upstream dataset preparation and public split IDs.
- `scripts/` — `demo.py` and the minimal GACL scorer.
- `tests/` — unit tests for the core scoring rule and patch alignment.

Raw audio, images, and model weights are not redistributed. Full-inference dataset details are in `data/README.md`.

## Citation

```bibtex
@article{gao2026beyond,
  title={Beyond Text Following: Repairable Arbitration Reversals in Audio-Language Models},
  author={Gao, Yichen and Zhang, Yiqun and Wang, Zijing and Li, Yujia and Guo, Heng and Wu, Xi and Yang, Xiaocui and Feng, Shi and Zhang, Yifei and Wang, Daling},
  journal={arXiv preprint arXiv:2606.05161},
  year={2026},
  note={Accepted to EMNLP 2026 Main Conference}
}
```

## License

Released under the [MIT License](LICENSE).
