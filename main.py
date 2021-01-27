import csv
from collections import Counter
import matplotlib.pyplot as plt

country = []


with open("Unique_sellers.csv", 'r', encoding='utf-8') as f:
    reader = csv.reader(f, delimiter=',')

    for row in reader:
        country.append(row[1][-2:])


country_count = Counter(country)

countries, company_count = zip(*country_count.items())

print(countries)
print(company_count)

plt.figure(figsize=(20, 40))  # width:20, height:3
plt.bar(range(len(country_count)), country_count.values(), align='edge', width=0.8)
plt.bar(countries, company_count)
plt.title('Locations Of Companies That Sell On Amazon')
plt.xlabel('Country')
plt.xticks(rotation=75)
plt.ylabel('Amount Of Companies')
plt.show()