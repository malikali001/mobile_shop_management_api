# Django Inventory Management System

This project is a Django-based Inventory Management System designed to manage products, users, inventory, transactions (sales, transfers, receipts), and bills with role-based access control, JWT-based authentication, and custom permissions. The system includes functionality for managing brands, categories, inventory, and product records, as well as utilities for calculating profits and generating sales reports.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Models](#models)
- [Serializers](#serializers)
- [Views](#views)
- [Authentication](#authentication)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)

---

## Features

- **Role-Based Access Control**: Users have different permissions based on their roles (e.g., admin, manager).
- **JWT Authentication**: Secure user authentication using JSON Web Tokens.
- **Inventory Management**: Track product stock, sold quantities, and available inventory.
- **Transaction Management**: Record sales, transfers, receipts, and bill payments.
- **Profit Calculation**: Calculate profits based on transactions.
- **CRUD Operations**: For users, products, categories, brands, and inventory.

---


---

## Models

1. **CustomUser**: User model with fields for phone number, name, user type, and password.
2. **Brand**: Represents brands of products.
3. **Category**: Categorizes products.
4. **Product**: Contains product details like name, description, price, brand, and category.
5. **Inventory**: Manages product stock, including quantities sold and available.
6. **Receive**: Records product receipts.
7. **Sale**: Manages product sales transactions.
8. **Transfer**: Handles product transfers between locations.
9. **TransferSale**: Manages sales during transfers.
10. **Bill**: Represents bills for transactions.
11. **BillPayment**: Handles payments made towards bills.

---

## Serializers

- **CustomTokenObtainPairSerializer**: Custom JWT serializer for token authentication.
- **CustomUserSerializer**: Serializer for user management, including create and update operations.
- **BrandSerializer**: Serializer for brand management.
- **CategorySerializer**: Serializer for category management.
- **InventorySerializer**: Serializer for managing product stock.
- **ProductSerializer**: Serializer for product data, with inventory handling on creation.
- **ReceiveSerializer**: Serializer for recording product receipts and updating inventory.
- **SaleSerializer**: Serializer for sales transactions and updating inventory.
- **TransferSaleSerializer**: Serializer for recording transfer sales.
- **TransferSerializer**: Serializer for transfers between locations.
- **BillSerializer**: Serializer for managing bill details.
- **BillPaymentSerializer**: Serializer for recording payments made toward bills.

---

## Views

- **User Views**: `CustomUserList`, `CustomUserDetail`, `CustomTokenObtainPairView`, `CustomLogoutView`.
- **Product Views**: `BrandList`, `BrandDetail`, `CategoryList`, `CategoryDetail`, `InventoryList`, `ProductList`, `ProductDetail`, `ReceiveList`, `ReceiveDetail`, `SaleList`, `SaleDetail`, `ProfitCalculation`.
- **Transfer Views**: `TransferList`, `TransferDetail`, `TransferSaleList`, `TransferSaleDetail`.
- **Bill Views**: `BillList`, `BillDetail`, `BillPaymentList`, `BillPaymentDetail`.

Each view is configured to handle specific CRUD operations and permissions based on user roles and HTTP methods.

---

## Authentication

This project uses **JWT Authentication** with the following custom features:

- `CustomTokenObtainPairView`: Allows users to authenticate using phone number and password.
- `CustomLogoutView`: Provides JWT logout functionality by blacklisting the refresh token.

---

