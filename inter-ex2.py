import pandas as pd

path = input("Path: ")
df = pd.read_csv(path)
column_data = df['Phone 1'].tolist()

count = 0
for item in column_data:
    if '+1' in item:
        count += 1
print(count)
