# 📘 Modeling Documentation

## 🚀 Setup & Configuration

### 📦 Environment Variables (`.env`)

The `.env` file is used to store environment variables that are required:

```python
DATABASE_URL=postgresql://postgres:admin1234@db:5432/supermarket_hot_deals_db
DB_USER=postgres
DB_PASSWORD=admin1234
DB_NAME=supermarket_hot_deals_db
```

## Overview of the DS Service

The **DS (Data Science)** service provides backend capabilities for user data management and experimentation using a FastAPI application. Its core functions include:

- **CRUD operations** on user data stored in a MySQL database.
- **Loading simulated user data** from a CSV file into the database upon startup.
- **Serving API endpoints** such as:
  - `POST /create` — Create a new user.
  - `GET /users` — Retrieve all users.
  - `PUT /update/{user_id}` — Update a user's name.
  - `DELETE /delete/{user_id}` — Delete a user and their transactions.

This service also includes the logic to **load data at startup** using pandas, which enables quick initialization with pre-existing datasets.

---

## Thompson Sampling Notebook

The service contains a Jupyter Notebook named `thompson_new.ipynb` that performs a **Thompson Sampling experiment** using SQLAlchemy and a relational database. It is designed to:

- Connect to a project database and define an experiment (`Project`) and a set of `Bandit` entries (representing different products).
- Initialize the bandits with random priors (`alpha`, `beta`).
- Sample from beta distributions to determine the best products to show.
- Simulate user interaction (clicks) and update the bandits’ parameters accordingly.

Key functionalities:
- Automatically creates or uses existing projects and bandits.
- Implements page-wise recommendations (e.g., 3 products per page).
- Simulates real-time click behavior using `simulate_click`.

---

### 🐳 `Dockerfile`
The `Dockerfile` defines the image used to run the DS service.
