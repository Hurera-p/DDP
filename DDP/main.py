import dask.dataframe as dd

# Path to the dataset
dataset_path = './data/yellow_tripdata_2015-01.csv'  # Update with your file path

# Load dataset with Dask
ddf = dd.read_csv(dataset_path)

# Perform your data analysis using Dask
# Example: Calculate the total revenue per payment type
revenue_per_payment_type = ddf.groupby("payment_type")["total_amount"].sum().compute()
print("Total revenue per payment type:")
print(revenue_per_payment_type)

# Count the number of rides for each payment type
rides_per_payment_type = ddf.groupby('payment_type')['total_amount'].count().compute()
print("Number of rides per payment type:")
print(rides_per_payment_type)

# Average trip distance per payment type
avg_distance_by_payment_type = ddf.groupby("payment_type")["trip_distance"].mean().compute()
print("Average trip distance per payment type:")
print(avg_distance_by_payment_type)

