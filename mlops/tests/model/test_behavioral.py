# tests/model/test_behavioral.py
from pathlib import Path
import pytest
from config import config
from tagifai import main, predict

@pytest.fixture(scope="module")
def artifacts():
    run_id = open(Path(config.CONFIG_DIR, "run_id.txt")).read()
    artifacts = main.load_artifacts(run_id=run_id)
    return artifacts

@pytest.mark.parametrize(
    "text_a, text_b, tag",
    [
        (
            "Transformers applied to NLP have revolutionized machine learning.",
            "Transformers applied to NLP have disrupted machine learning.",
            "natural-language-processing",
        ),
    ],
)
def test_inv(text_a, text_b, tag, artifacts):
    """INVariance via verb injection (changes should not affect outputs)."""
    tag_a = predict.predict(texts=[text_a], artifacts=artifacts)[0]["predicted_tag"]
    tag_b = predict.predict(texts=[text_b], artifacts=artifacts)[0]["predicted_tag"]
    assert tag_a == tag_b == tag
