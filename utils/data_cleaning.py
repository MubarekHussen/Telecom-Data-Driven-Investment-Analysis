class DataCleaner:
    """
    A class used to clean data in a DataFrame.

    ...

    Attributes
    ----------
    df : DataFrame
        a pandas DataFrame to be cleaned
    columns_to_exclude : list
        a list of column names to be excluded from certain operations

    Methods
    -------
    drop_null_rows():
        Drops rows that have a null value in any of the columns that have exactly one null value.
    fill_categorical():
        Fills missing categorical values with the mode of each column.
    fill_numerical():
        Fills missing numerical values with the mean of each column, excluding certain specified columns.
    fill_unknown():
        Fills missing values in certain specified columns with the string "Unknown".
    clean():
        Performs all the cleaning steps and returns the cleaned DataFrame.
    """

    def __init__(self, df):
        """
        Constructs all the necessary attributes for the DataCleaner object.

        Parameters
        ----------
            df : DataFrame
                a pandas DataFrame to be cleaned
        """
        self.df = df.copy()
        self.columns_to_exclude = ["Bearer Id", "IMSI", "MSISDN/Number", "IMEI"]

    def drop_null_rows(self):
        """
        Drops rows that have a null value in any of the columns that have exactly one null value.

        Returns
        -------
        self : object
            Returns self to allow chaining.
        """
        columns_with_one_null = self.df.columns[self.df.isnull().sum() == 1]
        self.df = self.df.dropna(subset=columns_with_one_null)
        return self

    def fill_categorical(self):
        """
        Fills missing categorical values with the mode of each column.

        Returns
        -------
        self : object
            Returns self to allow chaining.
        """
        categorical_columns = self.df.select_dtypes(include="object").columns
        self.df[categorical_columns] = self.df[categorical_columns].fillna(
            self.df[categorical_columns].mode().iloc[0]
        )
        return self

    def fill_numerical(self):
        """
        Fills missing numerical values with the mean of each column, excluding certain specified columns.

        Returns
        -------
        self : object
            Returns self to allow chaining.
        """
        numerical_columns = self.df.select_dtypes(include=["float64"]).columns
        numerical_columns = numerical_columns.drop(self.columns_to_exclude)
        self.df[numerical_columns] = self.df[numerical_columns].fillna(
            self.df[numerical_columns].mean()
        )
        return self

    def fill_unknown(self):
        """
        Fills missing values in certain specified columns with the string "Unknown".

        Returns
        -------
        self : object
            Returns self to allow chaining.
        """
        self.df[self.columns_to_exclude] = self.df[self.columns_to_exclude].fillna(
            "Unknown"
        )
        return self

    def clean(self):
        """
        Performs all the cleaning steps and returns the cleaned DataFrame.

        Returns
        -------
        DataFrame
            The cleaned DataFrame.
        """
        self.drop_null_rows().fill_categorical().fill_numerical().fill_unknown()
        return self.df
