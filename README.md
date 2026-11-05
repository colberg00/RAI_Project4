# RAI Project 4 — Concept Bottleneck Models for Skin Lesion Diagnosis

Responsible AI (02517), DTU, 2026. Assignment text: [`docs/assignment4_part1.pdf`](docs/assignment4_part1.pdf).

We build an intrinsically explainable **concept bottleneck model (CBM)** (Koh et al., 2020) on the
**derm7pt** dataset (Kawahara et al., 2019). The model maps a lesion image to the **7-point checklist
criteria** (the concepts) and then from those concepts to one of **5 diagnostic categories**
(BCC, NEV, MEL, MISC, SK). The final deliverable is a poster.

## Repository layout

```
.
├── project4.ipynb    # all code: config, data, CBM, training regimes, evaluation, interventions
├── data/             # derm7pt goes here (git-ignored), see data/README.md
├── docs/             # assignment text
├── poster/           # poster source + exported figures
└── results/          # checkpoints, metrics, figures (git-ignored)
```

## Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
jupyter lab project4.ipynb
```

All settings (paths, image type, training regime, hyperparameters) are in the `CONFIG` cell at
the top of the notebook.

> The project folder lives in OneDrive. Keep `.venv/`, `data/derm7pt/` and `results/` out of sync
> if possible (they are git-ignored, but OneDrive will still try to upload them).

Then download the dataset — see [`data/README.md`](data/README.md).

## Training regimes (Koh et al., 2020)

| Regime | Concept model g: x → ĉ | Label model f: c → y |
|---|---|---|
| **Independent** | trained on (x, c) | trained on **ground-truth** c; at test time fed ĉ = g(x) |
| **Sequential** | trained on (x, c) | trained on **predicted** ĉ = g(x) (g frozen) |
| **Joint** | trained together, loss = L_y + λ · L_c | — |

## Data splits

We use the **official derm7pt splits** (`meta/train_indexes.csv`, `valid_indexes.csv`,
`test_indexes.csv`): validation is used for model selection / early stopping only, test is
touched once per final model.

## Assignment progress

### Part 1 — Building the CBM and explanation success criteria
- [ ] Download derm7pt and build a CBM with the 7-pt criteria as concepts
- [ ] Support independent, sequential and joint training; document data allocation
- [ ] Train all three regimes; standard performance assessment
- [ ] Exploratory study of concept explanations + concept interventions
- [ ] 3 use cases for model explanations with measurable success criteria → section 7 of the notebook

### Part 2 — TBA
### Part 3 — TBA

## References
- Koh et al., *Concept Bottleneck Models*, ICML 2020.
- Kawahara et al., *Seven-Point Checklist and Skin Lesion Classification Using Multitask
  Multimodal Neural Nets*, IEEE JBHI 2019. Dataset: <https://derm.cs.sfu.ca>,
  code: <https://github.com/jeremykawahara/derm7pt>
