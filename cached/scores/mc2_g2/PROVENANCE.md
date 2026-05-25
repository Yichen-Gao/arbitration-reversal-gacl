# MC2 G2 Cached Results

These files cache the two-model MC2 transfer evaluation under the G2 prefix-trie constrained short-label generation protocol. Raw images are not redistributed.

Paper-facing fixed-parameter table:

- `fixed_lam0p5_tau0p5_summary.csv`: anonymized summary for the main cross-modal transfer table. GACL uses the conservative fixed setting `lambda=0.5, tau_A=0.5` on both Qwen3-VL backbones.

Auxiliary per-sample endpoint caches:

- `qwen3vl2b_conflict.jsonl`: Qwen3-VL-2B on the conflict split.
- `qwen3vl2b_consistent.jsonl`: Qwen3-VL-2B on the consistent split.
- `qwen3vl8b_conflict.jsonl`: Qwen3-VL-8B on the conflict split.
- `qwen3vl8b_consistent.jsonl`: Qwen3-VL-8B on the consistent split.

The JSONL rows contain candidate-constrained predictions for joint, vision-only, text-only, prompt-steered, and endpoint branch outputs. The paper table is reproduced from the fixed-parameter summary so that it matches the submitted `GACL (fixed)` operating point rather than the vision-only endpoint.
