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

## ✅ Create a Project

**Response:**

- Returns the newly created project including the generated project ID.

**Status Codes:**

- `200 OK`: Success
- `400 Bad Request`: Invalid input

---

## 🔍 Get a Project

**Endpoint:** `GET /project/{project_id}`

**Description:**  
Retrieves a single project by its ID.

**Parameters:**

- `project_id` (int, path): The unique ID of the project.

**Response:**

- Returns the project details.

**Status Codes:**

- `200 OK`: Success
- `404 Not Found`: Project not found

---

## 📥 Get All Projects

**Endpoint:** `GET /projects`

**Description:**  
Retrieves all projects.

**Response:**

- Returns a list of all projects.

**Status Codes:**

- `200 OK`: Success
- `404 Not Found`: No projects found

---

# 📢 Ads (Bandits)

---
## 🆕 Create an Ad

**Response:**

- Returns the newly created ad.

**Status Codes:**

- `200 OK`: Success  
- `404 Not Found`: Project not found

---

## 📋 Get Ads for Project

**Endpoint:** `GET /ads`

**Description:**  
Retrieves all ads for a specific project.

**Query Parameters:**

- `project_id` (int): The ID of the project

**Response:**

- Returns a list of ads for the project.

**Status Code:**

- `200 OK`: Success

---

## 🖱️ Register Ad Click

**Endpoint:** `POST /ads/{bandit_id}/click`

**Description:**  
Registers a click event for a specific ad.

**Parameters:**

- `project_id` (int, query): The ID of the project  
- `bandit_id` (int, path): The ID of the ad

**Response:**

- Returns confirmation message.

**Status Codes:**

- `200 OK`: Success  
- `404 Not Found`: Ad not found

---

## 🎯 Sample Top 3 Ads

**Endpoint:** `GET /ads/sample`

**Description:**  
Returns the top 3 ads sampled from their Beta distributions using Thompson Sampling.

**Query Parameters:**

- `project_id` (int): The ID of the project

**Response:**

- Returns a list of 3 sampled ads.

**Status Codes:**

- `200 OK`: Success  
- `404 Not Found`: No ads found

## 🐳 Dockerfile Behavior

The Dockerfile is used to set up a Docker container for running a FastAPI application. 
