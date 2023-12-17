import sys, os

rpath = os.path.abspath("..")
if rpath not in sys.path:
    sys.path.insert(0, rpath)

import pandas as pd
import numpy as np
import unittest
from utils import DataCleaner


class TestDataCleaner(unittest.TestCase):
    """
    This class contains unit tests for the DataCleaner class.
    """

    def setUp(self):
        """
        This method sets up the testing environment. It is called before every test method.
        """
        self.data = pd.DataFrame(
            {
                "A": ["cat", "dog", np.nan, "dog"],
                "B": [1, 2, np.nan, 4],
                "C": ["apple", "banana", "carrot", np.nan],
                "D": [np.nan, "x", "y", "z"],
            }
        )
        self.cleaner = DataCleaner(self.data)

    def test_fill_categorical(self):
        """
        This method tests the fill_categorical method of the DataCleaner class.
        It checks that the method correctly fills missing values in categorical columns.
        """
        self.cleaner.fill_categorical()
        self.assertFalse(
            self.cleaner.df.select_dtypes(include="object").isnull().sum().any()
        )

        for column in self.cleaner.df.select_dtypes(include="object").columns:
            mode = self.data[column].mode().iloc[0]
            filled_value = self.cleaner.df.loc[self.data[column].isnull(), column].iloc[
                0
            ]
            self.assertEqual(filled_value, mode)


if __name__ == "__main__":
    unittest.main()
