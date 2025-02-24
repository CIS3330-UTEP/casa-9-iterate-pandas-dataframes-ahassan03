import pandas as pd

def iterate_with_iterrows(df):
    print("Iteration using iterrows() method:")
    # Using iterrows() to iterate through DataFrame rows
    for index, row in df.iterrows():
        print(f"Index {index}: {row.to_dict()}")

def iterate_with_apply(df):
    print("\nIteration using apply() method:")
    # Define a function for processing each row
    def process_row(row):
        print(f"Index {row.name}: {row.to_dict()}")
    # Apply the function to each row
    df.apply(process_row, axis=1)

csv_file = "big-mac-full-index.csv"
df = pd.read_csv(csv_file)

iterate_with_iterrows(df)
iterate_with_apply(df)
