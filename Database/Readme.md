# Supermarket Hot Deals – Group Project

This project simulates a bandit-model-based system for supermarket discount tracking. It features PostgreSQL integration via SQLAlchemy, synthetic data generation using Faker, and Docker support for consistent setup across the group.

---

##  Project Structure

Supermarket_Hot_Deals/
└── db/
└── Database/
├── create_table.py # Creates database tables using SQLAlchemy
├── data_generator.py # Generates fake data and saves as CSV
├── database.py # SQLAlchemy DB connection (uses .env)
├── models.py # ORM models for users, projects, bandits, transactions
├── .env # Local DB credentials (not shared)
├── docker-compose.yml # Sets up PostgreSQL container
└── generated_data/ # Folder with CSV outputs after data generation

yaml
Copy
Edit

---

##  How to Run the Project

### 1. Run PostgreSQL with Docker

Make sure Docker is installed and running. Then, in the `Database/` directory:

```bash
docker-compose up -d