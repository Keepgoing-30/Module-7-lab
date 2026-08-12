"""
Task 2: Mathematical Operations Behind ML Paradigms
Instead of using massive libraries, implement the foundational math from scratch.
"""
import math

def calculate_supervised_loss(actual_y: list[float], predicted_y: list[float]) -> float:
    """
    TODO: Calculate the Mean Squared Error (MSE) between actual and predicted values.
    Formula: (1/n) * sum((actual - predicted)^2)
    """
    if len(actual_y) != len(predicted_y):
        raise ValueError("actual_y and predicted_y must have the same length.")

    squared_errors = [(actual - predicted) ** 2 for actual, predicted in zip(actual_y, predicted_y)]
    return sum(squared_errors) / len(actual_y)


def calculate_euclidean_distance(sensor_reading_a: list[float], sensor_reading_b: list[float]) -> float:
    """
    TODO: Calculate the Euclidean distance between two N-dimensional sensor vector arrays.
    Formula: sqrt(sum((a_i - b_i)^2))
    Used as the core distance metric for Unsupervised K-Means clustering.
    """
    if len(sensor_reading_a) != len(sensor_reading_b):
        raise ValueError("Sensor readings must be the same length.")

    squared_diff = sum((a - b) ** 2 for a, b in zip(sensor_reading_a, sensor_reading_b))
    return math.sqrt(squared_diff)
