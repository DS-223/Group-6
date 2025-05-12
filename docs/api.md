# 📘 API Documentation – Supermarket Hot Deals Backend

This API provides access to manage marketing A/B testing campaigns using bandits (ads), projects, users, and transactions. It supports creating/retrieving projects, managing ads, logging user clicks, and performing Thompson Sampling.

---

## 🌍 Base URL
```
http://<your-host>:8000
```

---

## Setup & Configuration

### 📦 Environment Variables (`.env`)

The API requires these environment variables (typically in `.env`):

```python
DATABASE_URL=postgresql://postgres:admin1234@db:5432/supermarket_hot_deals_db
DB_USER=postgres
DB_PASSWORD=admin1234
DB_NAME=supermarket_hot_deals_db
```

