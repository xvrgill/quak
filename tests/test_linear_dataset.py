import pytest
from quak.datasets import LinearDataset


def test_invalid_correlation_coefficient_error():
    invalid_correlation_coefficient = -10
    with pytest.raises(AttributeError):
        LinearDataset(invalid_correlation_coefficient)


@pytest.mark.parametrize("valid_coefficient", [-1, -.559405870233894723, 0, 0.334093, 1])
def test_valid_positive_correlation_coefficient_is_set(valid_coefficient):
    ld = LinearDataset(correlation_coefficient=valid_coefficient)
    assert ld.correlation_coefficient == valid_coefficient


def test_default_params_are_set():
    ld = LinearDataset(correlation_coefficient=1)
    assert ld.n_rows == 10
    assert ld.n_features == 5
    assert ld.feature_names is None


def test_custom_params_are_set():
    ld = LinearDataset(
        correlation_coefficient=1,
        n_rows=20,
        n_features=8,
        feature_names=["n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8"]
    )
    assert ld.n_rows == 20
    assert ld.n_features == 8
    assert ld.feature_names == ["n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8"]


def test_feature_count_matches_feature_names():
    ld = LinearDataset(
        correlation_coefficient=1,
        n_rows=20,
        n_features=8,
        feature_names=["n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8"]
    )
    assert ld.n_features == len(ld.feature_names)


def test_feature_names_are_strings():
    ld = LinearDataset(
        correlation_coefficient=1,
        n_rows=20,
        n_features=8,
        feature_names=["n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8"]
    )
    for name in ld.feature_names:
        assert type(name) == str


def test_validate_feature_names():
    with pytest.raises(AttributeError):
        LinearDataset(
            correlation_coefficient=1,
            n_rows=20,
            n_features=8,
            feature_names=["n1", "n2", "n3", "n4", "n5", "n6", "n7", "n8", "n9"]
        )
