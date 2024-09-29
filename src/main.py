import os
import pandas as pd
from location_generator import generate_locations  # Generates location reference table
from supplier_generator import generate_suppliers  # Generates suppliers data
from customer_generator import generate_customers  # Generates customers data
from product_generator import generate_products  # Generates product data
from transaction_generator import generate_transactions  # Generates transaction data
from payment_generator import generate_payments  # Generates payment data
from shipping_generator import generate_shipping_info  # Generates shipping data
from location_device_generator import generate_location_device_info  # Generates device info linked to transactions
from behavioral_data_generator import generate_behavioral_data  # Generates behavioral data linked to customers

# Constants
NUM_CUSTOMERS = 1000
NUM_PRODUCTS = 200
NUM_TRANSACTIONS = 20000
NUM_SESSIONS = 2000
NUM_SUPPLIERS = 50  # Number of unique suppliers
NUM_LOCATIONS = 100  # Number of unique locations

# Define data directory (this will ensure cross-platform compatibility)
data_dir = os.path.join("..", "data")

# Ensure the data directory exists
os.makedirs(data_dir, exist_ok=True)

# Generate reference data
locations_df = generate_locations(NUM_LOCATIONS)  # Generate location reference table
suppliers_df = generate_suppliers(NUM_SUPPLIERS)  # Generate supplier reference table

# Generate main data
customers_df = generate_customers(NUM_CUSTOMERS, locations_df)  # Linked to locations
products_df = generate_products(NUM_PRODUCTS, suppliers_df)  # Linked to suppliers
transactions_df = generate_transactions(NUM_TRANSACTIONS, customers_df, products_df)  # Includes discounts, loyalty points, etc.
payments_df = generate_payments(transactions_df, customers_df)  # Linked to transactions and customers
shipping_df = generate_shipping_info(transactions_df)  # Linked to transactions
location_device_df = generate_location_device_info(transactions_df, customers_df)  # Linked to transactions and customers
behavioral_data_df = generate_behavioral_data(customers_df, NUM_SESSIONS)  # Linked to customers

# Save the data to CSV for review and further use
suppliers_df.to_csv(os.path.join(data_dir, "suppliers.csv"), index=False)
customers_df.to_csv(os.path.join(data_dir, "customers.csv"), index=False)
products_df.to_csv(os.path.join(data_dir, "products.csv"), index=False)
transactions_df.to_csv(os.path.join(data_dir, "transactions.csv"), index=False)
payments_df.to_csv(os.path.join(data_dir, "payments.csv"), index=False)
shipping_df.to_csv(os.path.join(data_dir, "shipping.csv"), index=False)
location_device_df.to_csv(os.path.join(data_dir, "location_device.csv"), index=False)
behavioral_data_df.to_csv(os.path.join(data_dir, "behavioral_data.csv"), index=False)
locations_df.to_csv(os.path.join(data_dir, "locations.csv"), index=False)

print("Synthetic data generated and saved to CSV files.")
