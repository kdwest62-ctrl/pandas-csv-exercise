import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
print(df.loc[0:4].to_string())
