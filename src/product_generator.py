import random
import pandas as pd
from faker import Faker

fake = Faker()

def generate_products(num_products, suppliers_df):
    products = []
    for _ in range(num_products):
        product = {
            "product_id": fake.uuid4(),  # Unique ID for each product
            "product_name": fake.word(),
            "product_category": random.choice(["electronics", "fashion", "home goods", "toys", "furniture"]),
            "price": round(random.uniform(10, 1000), 2),
            "discount_applied": round(random.uniform(0, 0.3), 2),
            "stock_level": random.randint(1, 500),
            "rating": round(random.uniform(1, 5), 1),
            "reviews_count": random.randint(0, 500),
            "return_rate": round(random.uniform(0, 0.2), 2),
            "supplier_id": random.choice(suppliers_df["supplier_id"]),  # Link to supplier
        }
        products.append(product)
    return pd.DataFrame(products)
