import random
import pandas as pd
from faker import Faker

fake = Faker()


def generate_transactions(num_transactions, customers_df, products_df):
    transactions = []
    for _ in range(num_transactions):
        customer = random.choice(customers_df.to_dict('records'))  # Select random customer
        product = random.choice(products_df.to_dict('records'))  # Select random product

        # Simulate purchase frequency: 30% frequent, 50% moderate, 20% rare buyers
        purchase_frequency = random.choices(["frequent", "moderate", "rare"], weights=[30, 50, 20], k=1)[0]

        if purchase_frequency == "frequent":
            # Recent frequent purchases
            transaction_date = fake.date_time_between(start_date=customer['account_creation_date'], end_date='now')
        elif purchase_frequency == "moderate":
            # Purchases in the past 2 years
            transaction_date = fake.date_time_between(start_date='-2y', end_date='now')
        else:
            # Purchases older than 5 years
            transaction_date = fake.date_time_between(start_date='-5y', end_date='now')

        # 80% chance that shipping address is the same as billing
        same_shipping_address = random.choices([True, False], weights=[80, 20], k=1)[0]
        if same_shipping_address:
            shipping_address = customer['billing_address']
            shipping_city = customer['billing_city']
            shipping_country = customer['billing_country']
        else:
            shipping_address = fake.street_address()  # Different shipping address
            shipping_city = fake.city()
            shipping_country = fake.country()

        # Transaction velocity: 5% chance of multiple transactions in a short period
        transaction_velocity = random.choices([True, False], weights=[5, 95], k=1)[0]

        # Simulate abandoned carts and unsuccessful transactions
        transaction_status = \
        random.choices(["completed", "pending", "failed", "abandoned"], weights=[70, 10, 10, 10], k=1)[0]

        # Only proceed with transactions that are not abandoned
        if transaction_status != "abandoned":
            # Random quantity between 1 and 5
            quantity = random.randint(1, 5)

            # 20% chance the transaction applies a discount
            apply_discount = random.choices([True, False], weights=[20, 80], k=1)[0]
            discount_amount = round(random.uniform(0.05, 0.30), 2) if apply_discount else 0.0

            # Calculate total_amount as product price times quantity, applying discount if any
            total_amount = round((product['price'] * quantity) * (1 - discount_amount), 2)

            # Earn loyalty points on the transaction (1 point for every 1% of total amount)
            loyalty_points_earned = round(total_amount * 0.01)

            # 10% chance the customer redeems some loyalty points to reduce total amount
            redeem_loyalty_points = random.choices([True, False], weights=[10, 90], k=1)[0]
            if redeem_loyalty_points:
                loyalty_points_redeemed = min(customer['loyalty_points'],
                                              round(total_amount * 0.1))  # Max 10% of total amount
                total_amount = max(total_amount - loyalty_points_redeemed, 0)
            else:
                loyalty_points_redeemed = 0

            transaction = {
                "transaction_id": fake.uuid4(),  # Unique ID for each transaction
                "customer_id": customer["customer_id"],  # Link to existing customer
                "product_id": product["product_id"],  # Link to existing product
                "transaction_date": transaction_date,  # Ensure date is after account creation
                "quantity": quantity,  # Correct quantity
                "total_amount": total_amount,  # Correct total amount calculation
                "discount_amount": discount_amount,  # Record discount if any
                "loyalty_points_earned": loyalty_points_earned,  # Earn points on the transaction
                "loyalty_points_redeemed": loyalty_points_redeemed,  # Points redeemed
                "transaction_status": transaction_status,  # Handle status of the transaction
                "payment_method":
                    random.choices([customer['preferred_payment_method'], "credit_card"], weights=[90, 10])[0],
                # 90% chance preferred payment method is used
                "fraud_score": round(random.uniform(0, 1), 2),  # Fraud score between 0 and 1
                "device_change": random.choice([True, False]),  # Device change flag for fraud detection
                "transaction_velocity": 1 if transaction_velocity else 0,  # Flag for high transaction velocity
                "order_channel": random.choice(["web", "mobile", "tablet"]),  # Multi-channel order support
                "shipping_address": shipping_address,  # Shipping address based on billing
                "shipping_city": shipping_city,
                "shipping_country": shipping_country,
                "location_id": customer['location_id'],  # Link to customer's location
            }
            transactions.append(transaction)

    return pd.DataFrame(transactions)
