import random
import pandas as pd
from faker import Faker

fake = Faker()

def generate_behavioral_data(customers_df, num_sessions):
    behavioral_data = []
    for _ in range(num_sessions):
        customer = random.choice(customers_df["customer_id"])  # Link to existing customer
        behavior = {
            "customer_id": customer,  # Link to customer
            "session_id": fake.uuid4(),  # Unique session ID
            "session_start": fake.date_time_this_year(),
            "session_end": fake.date_time_this_year(),
            "session_duration": random.randint(30, 1800),  # Duration in seconds
            "pages_visited": random.randint(1, 20),
            "cart_additions": random.randint(0, 5),  # Items added to the cart
            "cart_abandonment_rate": round(random.uniform(0, 1), 2),  # Rate of cart abandonment
            "wishlist_additions": random.randint(0, 3),  # Items added to wishlist
            "bounce_rate": round(random.uniform(0, 1), 2),  # Bounce rate (leaving after viewing one page)
            "time_on_page": round(random.uniform(5, 120), 2),  # Average time spent per page (in seconds)
            "product_views": random.randint(0, 15),  # Number of product pages viewed
        }
        behavioral_data.append(behavior)
    return pd.DataFrame(behavioral_data)
