# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# data = pd.read_csv("housing.csv")
# print("Dataset Preview:")
# print(data.head())

# plt.figure()
# plt.hist(data["median_house_value"], bins=30)
# plt.title("Distribution")
# plt.xlabel("House Price")
# plt.ylabel("Count")
# plt.show()

# plt.figure()
# plt.scatter(data["median_income"], data["median_house_value"])
# plt.title("IncomePrice")
# plt.xlabel("Median Income")
# plt.ylabel("House Price")
# plt.show()


# grouped = data.groupby("ocean_proximity")["median_house_value"].mean()
# plt.figure()
# plt.bar(grouped.index, grouped.values)
# plt.title("LocationPrice")
# plt.xlabel("Ocean Proximity")
# plt.ylabel("Average Price")
# plt.xticks(rotation=45)
# plt.show()

# plt.figure()
# plt.boxplot(data["median_house_value"])
# plt.title("Outliers")
# plt.ylabel("Price")
# plt.show()

# corr = data.corr(numeric_only=True)
# plt.figure(figsize=(10, 8))
# plt.imshow(corr)
# plt.colorbar()
# plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
# plt.yticks(range(len(corr.columns)), corr.columns)
# plt.title("Correlation")
# plt.show()

# cols = ["median_income", "total_rooms", "population", "median_house_value"]
# pd.plotting.scatter_matrix(
#     data[cols],
#     figsize=(10, 10)
# )
# plt.show()
# print("All charts generated successfully!")


# Q1 = data["median_house_value"].quantile(0.25)
# Q3 = data["median_house_value"].quantile(0.75)

# IQR = Q3 - Q1
# lower_limit = Q1 - 1.5 * IQR
# upper_limit = Q3 + 1.5 * IQR

# clean_data = data[
#     (data["median_house_value"] >= lower_limit) &
#     (data["median_house_value"] <= upper_limit)
# ]

# print("Original Data:", len(data))
# print("After Cleaning:", len(clean_data))
# plt.figure()
# plt.scatter(
#     clean_data["median_income"],
#     clean_data["median_house_value"]
# )
# plt.title("CleanedData")
# plt.xlabel("Median Income")
# plt.ylabel("House Price")
# plt.show()













import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os


save_path = "c:/Users/Parul Thakur/Desktop/house/"

data = pd.read_csv("housing.csv")

print("Dataset Preview:")
print(data.head())


plt.figure()
plt.hist(data["median_house_value"], bins=30)
plt.title("Distribution")
plt.xlabel("House Price")
plt.ylabel("Count")
plt.savefig(os.path.join(save_path, "distribution.png"))


plt.figure()
plt.scatter(data["median_income"], data["median_house_value"])
plt.title("IncomePrice")
plt.xlabel("Median Income")
plt.ylabel("House Price")
plt.savefig(os.path.join(save_path, "income_price.png"))


grouped = data.groupby("ocean_proximity")["median_house_value"].mean()

plt.figure()
plt.bar(grouped.index, grouped.values)
plt.title("LocationPrice")
plt.xlabel("Ocean Proximity")
plt.ylabel("Average Price")
plt.xticks(rotation=45)
plt.savefig(os.path.join(save_path, "location_price.png"))


plt.figure()
plt.boxplot(data["median_house_value"])
plt.title("Outliers")
plt.ylabel("Price")
plt.savefig(os.path.join(save_path, "outliers.png"))


corr = data.corr(numeric_only=True)

plt.figure(figsize=(10, 8))
plt.imshow(corr)
plt.colorbar()

plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)

plt.title("Correlation")
plt.savefig(os.path.join(save_path, "correlation.png"))


cols = ["median_income", "total_rooms", "population", "median_house_value"]

pd.plotting.scatter_matrix(
    data[cols],
    figsize=(10, 10)
)

plt.savefig(os.path.join(save_path, "pairplot.png"))


Q1 = data["median_house_value"].quantile(0.25)
Q3 = data["median_house_value"].quantile(0.75)

IQR = Q3 - Q1

lower_limit = Q1 - 1.5 * IQR
upper_limit = Q3 + 1.5 * IQR

clean_data = data[
    (data["median_house_value"] >= lower_limit) &
    (data["median_house_value"] <= upper_limit)
]


plt.figure()
plt.scatter(
    clean_data["median_income"],
    clean_data["median_house_value"]
)

plt.title("CleanedData")
plt.xlabel("Median Income")
plt.ylabel("House Price")
plt.savefig(os.path.join(save_path, "cleaned_data.png"))


print("All charts saved successfully!")

plt.show()
