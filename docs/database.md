# Database

## Overview

The Supermarket Hot Deals database stores all key data for the project’s A/B testing and user interactions. It logs registered **users**, records each **Project** or campaign under test, tracks the **Bandit** variants (different deal versions) within each project, and saves each user’s **Transaction** (click or purchase) in the context of those variants. This allows the multi-armed bandit algorithm to assign users to different deal variants and then record their responses, enabling continuous experimentation and optimization of deals.

---

## Connection Setup

The application uses **SQLAlchemy** to connect to a PostgreSQL database. A `database.py` module typically does the setup by reading a database URL from environment variables and creating an engine. For example:

```python
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
```

## The DATABASE_URL is stored in a .env file:

```pyhton
DATABASE_URL=postgresql://user:password@localhost:5432/hotdeals
```

### The python-dotenv package loads this file at runtime.

# ORM Models and Database Schema

The SQLAlchemy ORM models define the database schema in `models.py`. Below are the main models used in this project:

---

## 🧑‍💻 User

**Table**: `users`  
**Purpose**: Stores account or identifier information for users interacting with promotional deals.

**Fields**:
- `customer_id` (Primary Key)
- `email` (String, unique, not null)
- `name` (String, not null)

**Relationships**:
- One-to-many with `Transaction` (a user can have multiple interactions)

---

## 📦 Project

**Table**: `projects`  
**Purpose**: Represents a campaign (A/B test or experiment setup)

**Fields**:
- `project_id` (Primary Key)
- `project_name` (String, not null)
- `project_description` (Text)
- `number_of_bandits` (Integer)

**Relationships**:
- One-to-many with `Bandit`
- One-to-many with `Transaction`

---

## 🎰 Bandit

**Table**: `bandits`  
**Purpose**: Represents a variant in a campaign (e.g., layout A, layout B)

**Fields**:
- `bandit_id` (Primary Key)
- `project_id` (Foreign Key to `projects.project_id`)
- `bandit_name` (String, not null)
- `alpha`, `beta` (Float): Parameters for probabilistic models (e.g., Thompson Sampling)
- `n`, `number_of_success`, `number_of_failures` (Integer): Tracking success/failure

**Relationships**:
- Many-to-one with `Project`
- One-to-many with `Transaction`

---

## 🧾 Transaction

**Table**: `transactions`  
**Purpose**: Logs user interactions (clicks, views, or purchases)

**Fields**:
- `transaction_id` (Primary Key)
- `customer_id` (Foreign Key to `users.customer_id`)
- `project_id` (Foreign Key to `projects.project_id`)
- `bandit_id` (Foreign Key to `bandits.bandit_id`)
- `timestamp` (DateTime)
- `clicked` (Boolean): Indicates if the user clicked on the item

**Relationships**:
- Many-to-one with `User`
- Many-to-one with `Bandit`
- Many-to-one with `Project`

---

## 🔄 Relationships Summary

| From        | To           | Type         |
|-------------|--------------|--------------|
| Project     | Bandit       | One-to-Many  |
| Bandit      | Transaction  | One-to-Many  |
| User        | Transaction  | One-to-Many  |
| Transaction | Bandit       | Many-to-One  |
| Transaction | User         | Many-to-One  |

---

## 🛠 Technologies Used

- **SQLAlchemy** – Python ORM
- **PostgreSQL** – Relational database
- **Docker** – Containerization of the app and the database
- **python-dotenv** – Load environment variables from a `.env` file

---

## 🐳 Dockerfile Behavior

The Dockerfile sets up the environment to run your ETL and ORM code. It does the following:

1. Installs Python and system dependencies
2. Installs Python dependencies from `requirements.txt`
3. Copies your source files
4. Runs a script to create the database schema:

```python
from models import Base
Base.metadata.create_all(engine)
