import pandas as pd

path = input("CSV Path: ")
df = pd.read_csv(path)
column_data = df['Email'].tolist()

def domain(email):
    result = email.split('@')
    return result[1]

data = []
for item in column_data:
    domain_name = domain(item)
    data.append(domain_name)

domains = list(set(data))

count = []
for item in domains:
    counter = 0
    for entry in data:
        if item == entry:
            counter += 1
    count.append(counter)

domain_counter = dict(zip(domains, count))

for key, value in domain_counter.items():
    if domain_counter[key] > 1:
        print(key, value)
