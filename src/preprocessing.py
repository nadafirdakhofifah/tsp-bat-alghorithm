import pandas as pd
import numpy as np


def load_dataset(uploaded_file):
    df = pd.read_csv(uploaded_file)
    return df



def extract_coordinates(df):
    row = df.iloc[0]

    num_cities = int(row['Num_Cities'])

    coords = []

    for i in range(1, num_cities + 1):
        x = row[f'City_{i}_X']
        y = row[f'City_{i}_Y']
        coords.append((x, y))

    return coords

def create_distance_matrix(coords):
    n = len(coords)

    matrix = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            x1, y1 = coords[i]
            x2, y2 = coords[j]

            distance = np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

            matrix[i][j] = distance

    return matrix