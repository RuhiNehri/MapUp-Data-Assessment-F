import pandas as pd
import numpy as np


def generate_car_matrix(ds):
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here

    # Load the dataset into a DataFrame
    df = pd.read_csv(ds)

    # Pivot the DataFrame to create a matrix
    df1 = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)

    # Set diagonal values to 0
    for idx in df1.index:
        df1.at[idx, idx] = 0

    return df1

ds = r'C:\Users\12AU\MapUp\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
result = generate_car_matrix(ds)
print(result)


def get_type_count(df):
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here

   # Create a new column 'car_type' based on the conditions provided
    df['car_type'] = pd.cut(df['car'], bins=[-float('inf'), 15, 25, float('inf')],
                            labels=['low', 'medium', 'high'], right=False)

    # Calculate the count of occurrences for each car_type category
    type_counts = df['car_type'].value_counts().to_dict()

    # Sort the dictionary alphabetically based on keys
    sorted_type_counts = dict(sorted(type_counts.items()))

    return sorted_type_counts

dataset_path = r'C:\Users\12AU\MapUp\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
df = pd.read_csv(dataset_path)
result1 = get_type_count(df)
print(result1)

def get_bus_indexes(df):
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here

   # Calculate the mean value of the 'bus' column
    mean_bus_value = df['bus'].mean()

    # Identify indices where 'bus' values are greater than twice the mean
    bus_indexes = df[df['bus'] > 2 * mean_bus_value].index.tolist()

    # Sort the indices in ascending order
    bus_indexes.sort()

    return bus_indexes

dataset_path = r'C:\Users\12AU\MapUp\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
df = pd.read_csv(dataset_path)
result2 = get_bus_indexes(df)
print(result2)


def filter_routes(df):
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    # Write your logic here

    # Calculate the average of values in the 'truck' column for each route
    route_avg_truck = df.groupby('route')['truck'].mean()

    # Filter routes where the average truck value is greater than 7
    selected_routes = route_avg_truck[route_avg_truck > 7].index.tolist()

    # Sort the list of selected routes
    selected_routes.sort()

    return selected_routes

dataset_path =  r'C:\Users\12AU\MapUp\MapUp-Data-Assessment-F\datasets\dataset-1.csv'
df = pd.read_csv(dataset_path)
result3 = filter_routes(df)
print(result3)


def multiply_matrix(matrix):
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here

    # Apply the specified logic to modify each value in the DataFrame
    modified_df = result.applymap(lambda x: x * 0.75 if x > 20 else x * 1.25)

    # Round the values to 1 decimal place
    rounded_df = modified_df.round(1)

    return rounded_df

result_matrix = generate_car_matrix(r'C:\Users\12AU\MapUp\MapUp-Data-Assessment-F\datasets\dataset-1.csv')
modified_result = multiply_matrix(result_matrix)
print(modified_result)


def time_check(df)->pd.Series:
    """
    Use shared dataset-2 to verify the completeness of the data by checking whether the timestamps for each unique (`id`, `id_2`) pair cover a full 24-hour and 7 days period

    Args:
        df (pandas.DataFrame)

    Returns:
        pd.Series: return a boolean series
    """
    # Write your logic here

    return pd.Series()
