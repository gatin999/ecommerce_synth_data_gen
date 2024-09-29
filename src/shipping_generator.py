import random
import pandas as pd
from faker import Faker
from datetime import timedelta

fake = Faker()

def generate_shipping_info(transactions_df):
    shipping = []
    for _, transaction in transactions_df.iterrows():
        shipping_details = {
            "transaction_id": transaction["transaction_id"],  # Link to existing transaction
            "shipping_address": fake.address(),  # Full address for the shipping
            "shipping_city": transaction["shipping_city"],  # Link shipping city from transactions
            "shipping_country": transaction["shipping_country"],  # Link shipping country from transactions
            "delivery_method": random.choice(["standard", "express", "overnight"]),
            "shipping_cost": round(random.uniform(5, 50), 2),
            "delivery_estimate": transaction["transaction_date"] + timedelta(days=random.randint(2, 10)),
            "shipping_tracking_number": fake.uuid4(),
        }
        shipping.append(shipping_details)
    return pd.DataFrame(shipping)
