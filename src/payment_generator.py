import random
import pandas as pd
from faker import Faker

fake = Faker()
#
# def generate_payments(transactions_df):
#     payments = []
#     for _, transaction in transactions_df.iterrows():
#         payment = {
#             "payment_id": fake.uuid4(),  # Unique ID for each payment
#             "transaction_id": transaction["transaction_id"],  # Link to existing transaction
#             "payment_method": transaction["payment_method"],  # Use payment method from transaction
#             "card_last_four": str(random.randint(1000, 9999)),
#             "card_issuer": random.choice(["Visa", "MasterCard", "AmEx"]),
#             "billing_address": fake.address(),  # Billing address remains part of payment data
#             "is_successful": random.choice([True, False]),
#         }
#         payments.append(payment)
#     return pd.DataFrame(payments)
def generate_payments(transactions_df, customers_df):
    payments = []
    for _, transaction in transactions_df.iterrows():
        customer = customers_df[customers_df['customer_id'] == transaction['customer_id']].iloc[0]

        # 10% chance of payment failure
        is_successful = random.choices([True, False], weights=[90, 10], k=1)[0]

        payment = {
            "payment_id": fake.uuid4(),  # Unique ID for each payment
            "transaction_id": transaction["transaction_id"],  # Link to existing transaction
            "payment_method": transaction["payment_method"],  # Use payment method from transaction
            "card_last_four": str(random.randint(1000, 9999)),
            "card_issuer": random.choice(["Visa", "MasterCard", "AmEx"]),
            "billing_address": customer["billing_address"],  # Billing address from customer
            "billing_city": customer["billing_city"],
            "billing_country": customer["billing_country"],
            "is_successful": is_successful,
        }
        payments.append(payment)
    return pd.DataFrame(payments)
