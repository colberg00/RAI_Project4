"""CBM architecture: concept model g (x -> c) and label model f (c -> y).

The bottleneck is the concatenation of per-concept softmax probabilities over the
categories in `cbm.data.CONCEPT_CATEGORIES`; f only ever sees this vector.
"""
# TODO: ConceptModel(backbone -> one head per concept), LabelModel, CBM wrapper
