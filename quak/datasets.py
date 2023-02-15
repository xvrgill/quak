# import pandas as pd
# import numpy as np
from typing import List


class LinearDataset:

    def __init__(self, correlation_coefficient: int | float, n_rows: int = 10, n_features: int = 5,
                 feature_names: List[str] = None) -> None:
        self.correlation_coefficient = self.__validate_coefficient__(correlation_coefficient)
        self.n_rows = n_rows
        self.n_features = n_features
        self.feature_names = self.__validate_feature_names__(n_features, feature_names)

    @staticmethod
    def __validate_coefficient__(coefficient):
        if coefficient < -1 or coefficient > 1:
            error_base_message = "The correlation value passed to LinearDataset is invalid."
            error_expected_value_message = f'Expected a value between -1 and 1. Received {coefficient}'
            final_error_message = " ".join([error_base_message, error_expected_value_message])
            raise AttributeError(final_error_message)
        return coefficient

    @staticmethod
    def __validate_feature_names__(n_features, feature_names):
        if not feature_names:
            return feature_names

        feature_name_count = len(feature_names)
        if n_features < feature_name_count:
            difference = n_features - feature_name_count
            error_base_message = "Invalid number of feature names passed."
            error_expected_value_message = f'Expected {n_features}, but received {feature_name_count} feature names.'
            error_solution_message = f'Either add {difference} more features or remove {difference} feature names.'
            final_error_message = " ".join([error_base_message, error_expected_value_message, error_solution_message])
            raise AttributeError(final_error_message)
        return feature_names


class NonCorrelatedDataset:
    ...


class NonLinearDataset:
    ...


class CustomDataset:
    ...
