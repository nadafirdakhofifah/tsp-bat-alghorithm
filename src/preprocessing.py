import pandas as pd
import numpy as np


def load_dataset(uploaded_file):
    """
    Membaca dataset CSV
    """
    df = pd.read_csv(uploaded_file)
    return df


def get_instances(df):
    """
    Mengambil daftar instance TSP
    """
    return df['TSP_Instance'].unique()


def select_instance(df, instance_name):
    """
    Memilih 1 instance TSP
    """
    selected = df[df['TSP_Instance'] == instance_name]

    return selected.iloc[0]


def extract_10_cities(instance_row):
    """
    Mengambil 10 kota pertama dari instance
    """

    coords = []

    for i in range(1, 11):

        x = float(instance_row[f'City_{i}_X'])
        y = float(instance_row[f'City_{i}_Y'])

        coords.append((x, y))

    return coords


def create_distance_matrix(coords):
    """
    Membuat distance matrix Euclidean
    """

    n = len(coords)

    matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):

            x1, y1 = coords[i]
            x2, y2 = coords[j]

            distance = np.sqrt(
                (x1 - x2) ** 2 +
                (y1 - y2) ** 2
            )

            matrix[i][j] = distance

    return matrix


def preprocessing_pipeline(df, instance_name):
    """
    Pipeline preprocessing otomatis
    """

def preprocessing_pipeline(df, instance_name):

    # Pilih instance
    instance_row = select_instance(df, instance_name)

    # Ambil 10 kota
    coords = extract_10_cities(instance_row)

    # Generate distance matrix
    distance_matrix = create_distance_matrix(coords)

    return coords, distance_matrix