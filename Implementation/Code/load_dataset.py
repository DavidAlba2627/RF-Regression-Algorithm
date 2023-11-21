import pandas as pd
from sklearn.model_selection import train_test_split

# Load the dataset and split it into training and testing sets
def load_and_split_dataset(test_size=0.2, random_state=0):
    """
    Parameters:
    - test_size: Proportion of the dataset to include in the test split.
    - random_state: Random state seed for reproducibility.

    Returns:
    - X_train, X_test: Training and testing data.
    - y_train, y_test: Labels for training and testing data.
    """

    # Load the dataset
    url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/housing.csv"
    dataset = pd.read_csv(url, header=None)

    # Splitting the dataset into features and target variable
    X = dataset.iloc[:, :-1]
    y = dataset.iloc[:, -1]

    # Splitting the dataset into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)

    return X_train, X_test, y_train, y_test
