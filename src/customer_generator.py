import random
import pandas as pd
from faker import Faker

fake = Faker()


def generate_customers(num_customers, locations_df):
    customers = []
    for _ in range(num_customers):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = f"{first_name.lower()}.{last_name.lower()}@{fake.free_email_domain()}"  # Email related to name
        location = random.choice(locations_df.to_dict('records'))  # Pick a location from the location table

        preferred_payment_method = random.choice(["credit_card", "paypal", "bank_transfer"])

        customer = {
            "customer_id": fake.uuid4(),  # Unique ID for each customer
            "first_name": first_name,
            "last_name": last_name,
            "email": email,
            "phone_number": fake.phone_number(),
            "gender": random.choice(["Male", "Female"]),
            "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=90),
            "account_creation_date": fake.date_this_decade(),
            "account_status": random.choice(["active", "inactive", "blocked", "suspended"]),
            "customer_tier": random.choice(["regular", "premium", "VIP"]),
            "loyalty_points": random.randint(0, 1000),
            "customer_lifetime_value": round(random.uniform(100, 5000), 2),
            "billing_address": fake.street_address(),  # Generate billing address
            "billing_city": location['city'],  # Linked to location table
            "billing_country": location['country'],  # Linked to location table
            "preferred_payment_method": preferred_payment_method,  # Preferred payment method
            "location_id": location['location_id']  # Link to location table
        }
        customers.append(customer)
    return pd.DataFrame(customers)
