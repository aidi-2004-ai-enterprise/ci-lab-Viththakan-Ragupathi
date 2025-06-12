import pandas as pd
import seaborn as sns

def load_penguin_data():
    """Load penguin dataset and return DataFrame shape"""
    df = sns.load_dataset("penguins")  # This line loads the dataset into 'df'
    return df.shape                    # Now df is defined, so this will work

if __name__ == "__main__":
    shape = load_penguin_data()
    print(f"Penguin dataset shape: {shape}")
