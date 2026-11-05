"""derm7pt loading: concept/label mapping and the official train/val/test splits.

Mappings follow the grouping used in Kawahara et al. (2019) and the official
derm7pt repository (https://github.com/jeremykawahara/derm7pt).
"""

from __future__ import annotations

from pathlib import Path

import pandas as pd

# --- Diagnosis -> 5 classes -------------------------------------------------
DIAGNOSIS_CLASSES = ["BCC", "NEV", "MEL", "MISC", "SK"]

DIAGNOSIS_MAP = {
    "basal cell carcinoma": "BCC",
    "blue nevus": "NEV",
    "clark nevus": "NEV",
    "combined nevus": "NEV",
    "congenital nevus": "NEV",
    "dermal nevus": "NEV",
    "recurrent nevus": "NEV",
    "reed or spitz nevus": "NEV",
    "melanoma": "MEL",
    "melanoma (in situ)": "MEL",
    "melanoma (less than 0.76 mm)": "MEL",
    "melanoma (0.76 to 1.5 mm)": "MEL",
    "melanoma (more than 1.5 mm)": "MEL",
    "melanoma metastasis": "MEL",
    "dermatofibroma": "MISC",
    "lentigo": "MISC",
    "melanosis": "MISC",
    "miscellaneous": "MISC",
    "vascular lesion": "MISC",
    "seborrheic keratosis": "SK",
}

# --- 7-point checklist criteria -> categorical concepts ---------------------
# Each concept maps raw meta.csv values to a small set of categories.
CONCEPTS: dict[str, dict[str, str]] = {
    "pigment_network": {
        "absent": "absent", "typical": "typical", "atypical": "atypical",
    },
    "streaks": {
        "absent": "absent", "regular": "regular", "irregular": "irregular",
    },
    "pigmentation": {
        "absent": "absent",
        "diffuse regular": "regular", "localized regular": "regular",
        "diffuse irregular": "irregular", "localized irregular": "irregular",
    },
    "regression_structures": {
        "absent": "absent",
        "blue areas": "present", "white areas": "present",
        "combinations": "present",
    },
    "dots_and_globules": {
        "absent": "absent", "regular": "regular", "irregular": "irregular",
    },
    "blue_whitish_veil": {
        "absent": "absent", "present": "present",
    },
    "vascular_structures": {
        "absent": "absent",
        "arborizing": "regular", "comma": "regular", "hairpin": "regular",
        "within regression": "regular", "wreath": "regular",
        "dotted": "irregular", "linear irregular": "irregular",
    },
}

# Ordered category list per concept (absent first).
CONCEPT_CATEGORIES: dict[str, list[str]] = {
    name: list(dict.fromkeys(mapping.values())) for name, mapping in CONCEPTS.items()
}


def load_metadata(root: str | Path) -> pd.DataFrame:
    """Load meta.csv and add integer-encoded `label` and `<concept>_idx` columns."""
    root = Path(root)
    meta = pd.read_csv(root / "meta" / "meta.csv")

    meta["label"] = meta["diagnosis"].map(DIAGNOSIS_MAP).map(DIAGNOSIS_CLASSES.index)
    for name, mapping in CONCEPTS.items():
        cats = CONCEPT_CATEGORIES[name]
        meta[f"{name}_idx"] = meta[name].map(mapping).map(cats.index)

    unmapped = meta[["label"] + [f"{c}_idx" for c in CONCEPTS]].isna().any(axis=1)
    if unmapped.any():
        raise ValueError(f"{unmapped.sum()} rows have unmapped diagnosis/concept values")
    return meta


def load_splits(root: str | Path) -> dict[str, pd.Index]:
    """Official derm7pt split indexes (row indices into meta.csv)."""
    meta_dir = Path(root) / "meta"
    return {
        split: pd.read_csv(meta_dir / f"{name}_indexes.csv")["indexes"].values
        for split, name in [("train", "train"), ("val", "valid"), ("test", "test")]
    }


# TODO: torch Dataset returning (image, concept_indices, label) with augmentations.
