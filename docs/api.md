# 📘 API Documentation – Supermarket Hot Deals Backend

This API provides access to manage marketing A/B testing campaigns using bandits (ads), projects, users, and transactions. It supports creating/retrieving projects, managing ads, logging user clicks, and performing Thompson Sampling.

---

## 🌍 Base URL
```
http://<your-host>:8000
```

---


## 🚀 Setup & Configuration

### 📦 Environment Variables (`.env`)

The API requires these environment variables:

```python
DATABASE_URL=postgresql://postgres:admin1234@db:5432/supermarket_hot_deals_db
DB_USER=postgres
DB_PASSWORD=admin1234
DB_NAME=supermarket_hot_deals_db
```
## Dependencies (`requirements.txt`)

The following Python packages are required to run the API backend:

```txt
fastapi
uvicorn
python-dotenv
pytz
six
SQLAlchemy
typing_extensions
psycopg2
```
 ## 📁 API Endpoints

---

### 📌 Projects

#### ➕ `POST /projects`
Create a new project.

**Request Body:**
```json
{
  "project_id": 1,
  "project_name": "Homepage Ads",
  "project_description": "Test homepage ad designs",
  "number_of_bandits": 2
}
```

### 📥 GET /projects

Fetch all existing projects.

#### Response

```json
[
  {
    "project_id": 1,
    "project_name": "Homepage Ads",
    "project_description": "Test homepage ad designs",
    "number_of_bandits": 2
  }
]
```

### 🔍 GET /project/{project_id}

Get a specific project by its ID.

#### Response

```json
{
  "project_id": 1,
  "project_name": "Homepage Ads",
  "project_description": "Test homepage ad designs",
  "number_of_bandits": 2
}
```
### 📢 Ads / Bandits

#### ➕ POST /ads

Create a new ad (bandit) for a given project.

#### Request Body

```json
{
  "project_id": 1,
  "bandit_name": "Layout A"
}
```
## 🐳 Dockerfile Behavior
շ
