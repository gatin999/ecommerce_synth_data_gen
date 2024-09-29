# eCommerce Synthetic Data Generation Project

## Overview

This project is designed to generate **synthetic eCommerce data** for testing fraud detection algorithms, machine learning models, or analytical environments. It simulates real-world eCommerce transactions, customer behavior, product purchases, payment information, and other related datasets.

The generated data can be used for:

- Testing fraud detection systems.
- Simulating customer purchase behavior.
- Creating analytical datasets for machine learning and data science experiments.

## Features

- **Customer Data**: Simulates customer profiles, including names, email addresses, account creation dates, billing and shipping addresses, and engagement behavior.
- **Product Data**: Includes product details like product names, categories, prices, and suppliers.
- **Transaction Data**: Simulates purchase transactions, including multi-channel purchases (web, mobile), quantities, total amounts, discounts, and loyalty points.
- **Payment Data**: Simulates payment methods (credit card, PayPal, etc.), transaction statuses (completed, failed, abandoned), and payment amounts.
- **Shipping Data**: Handles shipping details, including shipping addresses, shipment statuses, and shipping costs.
- **Behavioral Data**: Generates customer engagement data like frequency and recency of purchases, abandoned carts, and unsuccessful transactions.

## Directory Structure

```plaintext
ecommerce_synthetic_data/
│
├── src/
│   ├── __init__.py
│   ├── customer_generator.py        # Generates customer data
│   ├── product_generator.py         # Generates product data
│   ├── transaction_generator.py     # Generates transactions with loyalty points, discounts, and more
│   ├── payment_generator.py         # Simulates payment methods and payment statuses
│   ├── shipping_generator.py        # Generates shipping details and addresses
│   ├── location_device_generator.py # Generates device info and geolocation anomalies
│   └── behavioral_data_generator.py # Simulates customer behavioral data
│
├── data/                            # Directory to store the generated data (e.g., CSV files)
├── tests/                           # Unit tests for the data generators
├── README.md                        # Documentation
├── .gitignore                       # Ignoring unnecessary files in Git
└── requirements.txt                 # Python dependencies
