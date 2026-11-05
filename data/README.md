# Data: derm7pt

The dataset is **not** committed (licence + size). Each group member downloads it locally.

1. Register and download from <https://derm.cs.sfu.ca> (release_v0).
2. Unzip so the layout is:

```
data/release_v0/
├── images/            # clinical + dermoscopic images, in sub-folders
└── meta/
    ├── meta.csv
    ├── train_indexes.csv
    ├── valid_indexes.csv
    └── test_indexes.csv
```

If you place it elsewhere, update the data path in the notebook.

## What we use from `meta.csv`

- `diagnosis` → grouped into 5 classes (BCC, NEV, MEL, MISC, SK).
- 7-pt criteria → concepts: `pigment_network`, `streaks`, `pigmentation`,
  `regression_structures`, `dots_and_globules`, `blue_whitish_veil`, `vascular_structures`.
- `derm` / `clinic` → image paths (dermoscopic / clinical photo).

Split sizes (official): 413 train / 203 val / 395 test cases.
