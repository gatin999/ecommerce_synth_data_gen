import random

import pandas as pd
from faker import Faker

fake = Faker()

def generate_suppliers(num_suppliers=50):
    suppliers = []
    for _ in range(num_suppliers):
        supplier = {
            "supplier_id": fake.uuid4(),  # Unique ID for each supplier
            "supplier_name": fake.company(),  # Random supplier name
            "supplier_country": fake.country(),  # Supplier's country
            "supplier_reliability_score": round(random.uniform(0.5, 1.0), 2),  # Reliability score
        }
        suppliers.append(supplier)
    return pd.DataFrame(suppliers)
