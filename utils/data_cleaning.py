def clean_data(df):
    """
    Perform data cleaning operations on the given DataFrame.

    Args:
    - df: DataFrame to be cleaned

    Returns:
    - cleaned_df: Cleaned DataFrame
    """
    # Get the columns that have exactly 1 null value
    columns_with_one_null = df.columns[df.isnull().sum() == 1]

    # Drop rows that have a null value in any of those columns
    cleaned_df = df.dropna(subset=columns_with_one_null)

    obj_type_df = cleaned_df.copy()

    # Fill missing categorical values with mode
    categorical_columns = obj_type_df.select_dtypes(include="object").columns
    obj_type_df[categorical_columns] = obj_type_df[categorical_columns].fillna(
        obj_type_df[categorical_columns].mode().iloc[0]
    )

    num_df = obj_type_df.copy()

    # Get numerical columns
    numerical_columns = num_df.select_dtypes(include=["float64"]).columns

    # Remove the columns you want to exclude
    columns_to_exclude = ["Bearer Id", "IMSI", "MSISDN/Number", "IMEI"]
    numerical_columns = numerical_columns.drop(columns_to_exclude)

    # Fill missing numerical values with mean
    num_df[numerical_columns] = num_df[numerical_columns].fillna(
        num_df[numerical_columns].mean()
    )

    final_df = num_df.copy()

    columns_to_fill = ["Bearer Id", "IMSI", "MSISDN/Number", "IMEI"]
    final_df[columns_to_fill] = final_df[columns_to_fill].fillna("Unknown")

    return final_df
