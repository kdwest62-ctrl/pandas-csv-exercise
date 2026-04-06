import pandas as pd

path = input("Path: ")
df = pd.read_csv(path)
column_data = df['Subscription Date'].tolist()

dates = []
for item in column_data:
    if item[0:4] == '2021':
        dates.append(item)

customers = df[df['Subscription Date'].isin(dates)]
print(customers.to_string())
