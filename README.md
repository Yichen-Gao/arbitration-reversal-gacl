<div align="center">

# Beyond Text Following: Repairable Arbitration Reversals in Audio-Language Models

**Official implementation of [Beyond Text Following: Repairable Arbitration Reversals in Audio-Language Models](https://arxiv.org/abs/2606.05161)** · **EMNLP 2026 Main**

[![arXiv](https://img.shields.io/badge/arXiv-2606.05161-b31b1b.svg)](https://arxiv.org/abs/2606.05161)
[![EMNLP 2026 Main](https://img.shields.io/badge/EMNLP_2026-Main-2ea44f.svg)](https://2026.emnlp.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![CI](https://github.com/Yichen-Gao/arbitration-reversal-gacl/actions/workflows/ci.yml/badge.svg)](https://github.com/Yichen-Gao/arbitration-reversal-gacl/actions/workflows/ci.yml)

<img src="assets/fig1.png" alt="GACL overview" width="100%" />

</div>

## TL;DR

Audio-language models are overly text-following: when the transcript conflicts with the audio, they often answer from the text even though the audio evidence is clear.

We find that this is usually **repairable, not unavailable** — in **64.1%** of conflict samples, the same-audio reference branch already ranks the correct audio answer first. **GACL** (Gated Audio Counterfactual Logit Correction) is a training-free decoding rule that repairs these reversals at inference time:

```text
α(x)    = clip(λ · R_A(x) · N_out(x), 0, 1)
s_GACL  = s_J + α(x) · (s_A − s_J)
```

- `N_out` — joint and audio reference disagree
- `R_A` — audio reference is confident
- `s_A − s_J` — score displacement toward the audio-supported answer

No fine-tuning. No gradients. No extra model weights.

## Results at a Glance

| Metric | GACL | Meaning |
| --- | ---: | --- |
| **+41.7 pp** | ✅ | macro conflict accuracy over Joint, at only **4.2 pp** faithful drop |
| **+17.8 pp** | ✅ | nAUC over the best contrastive baseline under a 5 pp faithful-drop budget |
| **+40.5 pp** | ✅ | MC2 vision-text transfer on Qwen3-VL-2B — no retuning |
| **0.93** | ✅ | Spearman ρ between patch effects and output candidate-score displacement |

Evaluated across **5 audio-language models** and **4 audio-text conflict tasks**.

## Quick Demo

No dataset download, no GPU, no model weights — the repo ships the paper-facing score artifacts.

```bash
git clone https://github.com/Yichen-Gao/arbitration-reversal-gacl.git
cd arbitration-reversal-gacl
pip install -r requirements.txt
python scripts/demo.py
```

This prints the main tables. Add `--figures` to regenerate Figures 2, 3, and 5:

```bash
python scripts/demo.py --figures
```

Full data download and end-to-end reproduction notes are in [`data/README.md`](data/README.md); the core method is in [`src/methods/gacl.py`](src/methods/gacl.py).

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

MIT — see [`LICENSE`](LICENSE).
