import pandas as pd
path = input("CSV path: ")
df = pd.read_csv(path)
print(f'Shape: {df.shape}')
print('-' * 8)
print(f'Columns: {df.columns.tolist()}')
print('-' * 8)
print(f'Types:\n{df.dtypes}')
