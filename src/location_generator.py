import pandas as pd
from faker import Faker

fake = Faker()

def generate_locations(num_locations=100):
    locations = []
    for _ in range(num_locations):
        location = {
            "location_id": fake.uuid4(),  # Unique ID for each location
            "country": fake.country(),    # Generate random country
            "city": fake.city(),          # Generate random city
        }
        locations.append(location)
    return pd.DataFrame(locations)
