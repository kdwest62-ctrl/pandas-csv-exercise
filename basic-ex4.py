import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
column = input("Column name: ").capitalize()
column_data = df[column].tolist()

unique_data = tuple(set(column_data))
count = len(unique_data)
print(f"Number of unique {column} names: {count}")

series = pd.Series(unique_data, index=[num for num in range(1, (count + 1))])
print(series.to_string())
