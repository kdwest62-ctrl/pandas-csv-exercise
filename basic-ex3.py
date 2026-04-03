import pandas as pd

path = input("CSV path: ")
df = pd.read_csv(path)
countries_draft = df['Country'].tolist()

countries_final = []
for country in countries_draft:
    if country not in countries_final:
        countries_final.append(country)

customers = []
for country in countries_final:
    count = 0
    for item in countries_draft:
        if country == item:
            count += 1
    customers.append(count)

data_gathered = dict(zip(countries_final, customers))
descending_list= dict(sorted(data_gathered.items(), key=lambda a: a[1], reverse=True))

data = {'Country': [key for key in descending_list],
        'Customers': [value for value in descending_list.values()]}
df = pd.DataFrame(data, index=[num for num in range(1, (len(countries_final) + 1))])
print(df.to_string())
