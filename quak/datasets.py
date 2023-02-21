import numpy as np
import numpy.typing as npt


class Dataset:

    def __init__(self, n_rows, n_columns):
        self.dataset = None
        self.n_rows = n_rows
        self.n_columns = n_columns
        self.column_names = []

    def __getitem__(self, item):
        return getattr(self, item, None)

    def make_array_of_zeros(self, n_rows: int, n_columns: int):
        self.dataset = np.zeros((n_rows, n_columns))
        return self

    def create_column(self, name: str, data: list = None):
        if not data:
            # create empty array of length equal to number of rows
            # cols will be transformed later
            col_data = np.zeros(self.n_rows, 1)
        else:
            col_data = np.array(data).reshape(self.n_rows, 1)
        # add new column name to col names attribute
        # create attribute to store column data so that it can be accessed later
        setattr(self, name, col_data)
        self.column_names.append(name)
        return self


if __name__ == "__main__":
    ds = Dataset(3, 5)
    ds = (ds
          .create_column("feature_one", [3, 7, 5]))

    feature_one = ds["feature_one"]
    print(feature_one)
