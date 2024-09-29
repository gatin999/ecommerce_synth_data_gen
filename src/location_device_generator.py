import random
import pandas as pd
from faker import Faker

fake = Faker()


def generate_location_device_info(transactions_df, customers_df):
    location_device_data = []
    for _, transaction in transactions_df.iterrows():
        customer = customers_df[customers_df['customer_id'] == transaction['customer_id']].iloc[0]

        # 90% chance the geolocation is consistent with the customer's location
        consistent_geolocation = random.choices([True, False], weights=[90, 10], k=1)[0]

        if consistent_geolocation:
            try:
                # Check if we can get valid lat/long for the billing country
                geolocation_data = fake.local_latlng(country_code=customer['billing_country'])
                if geolocation_data:
                    geolocation_lat = geolocation_data[0]  # Latitude for customer location
                    geolocation_lon = geolocation_data[1]  # Longitude for customer location
                else:
                    # Fallback to a random location if local_latlng fails
                    geolocation_lat = round(random.uniform(-90, 90), 6)
                    geolocation_lon = round(random.uniform(-180, 180), 6)
            except Exception as e:
                # Fallback in case of any error
                geolocation_lat = round(random.uniform(-90, 90), 6)
                geolocation_lon = round(random.uniform(-180, 180), 6)
        else:
            # Random geolocation for fraud detection (mismatch case)
            geolocation_lat = round(random.uniform(-90, 90), 6)
            geolocation_lon = round(random.uniform(-180, 180), 6)

        # 20% chance the customer uses a different device (device change)
        device_change = random.choices([True, False], weights=[20, 80], k=1)[0]
        if device_change:
            # Simulate a new device (e.g., customer switching from mobile to desktop)
            device_type = random.choice(["mobile", "desktop", "tablet"])
            device_id = fake.uuid4()
        else:
            # Consistent device
            device_type = transaction["order_channel"]  # Device matches order channel
            device_id = customer['customer_id']  # Simulate same device by linking to customer

        # Device trust level: 90% chance it's a trusted device, 10% chance of a flagged device
        device_trust_level = random.choices(["trusted", "flagged"], weights=[90, 10], k=1)[0]

        location_device = {
            "transaction_id": transaction["transaction_id"],
            "ip_address": fake.ipv4(),
            "geolocation_lat": geolocation_lat,
            "geolocation_lon": geolocation_lon,
            "device_id": device_id,
            "device_type": device_type,
            "device_trust_level": device_trust_level,  # Trust level of the device
            "os_type": random.choice(["Windows", "iOS", "Android"]),
            "browser": random.choice(["Chrome", "Firefox", "Safari"]),
            "vpn_used": random.choice([True, False]),
        }
        location_device_data.append(location_device)

    return pd.DataFrame(location_device_data)

