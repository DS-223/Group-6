
# Supermarket Hot Deals – Group Project
# Employee Management System

A Dockerized microservice project for managing employee records using FastAPI, Streamlit, PostgreSQL, and pgAdmin. This project also includes ETL processing and documentation hosted using MkDocs.

---

## Problem Definition  

### The Problem Area  
**A/B Testing** – Optimizing the online display of promotional content to improve customer engagement and sales in the e-commerce grocery and retail sector.  

### Defining the Specific Problem  
Supermarkets lack data-driven guidelines on the optimal sequence to display "Hot Sales" items on their website homepage. The absence of an optimized ordering may result in:  
- Lower click-through rates (CTR)  
- Missed sales opportunities  
- Suboptimal customer engagement
- 
## Expected Outcomes  
- **Higher CTR** on "Hot Sales" items.  
- **Increased revenue** from optimized product placement.  

## 🚀 Quick Links

- 🔗 **Streamlit UI**: [http://localhost:8501](http://localhost:8501)
- 🔗 **FastAPI Swagger Docs**: [http://localhost:8008/docs](http://localhost:8008/docs)
- 🔗 **pgAdmin Interface**: [http://localhost:5050](http://localhost:5050)
- 🔗 **Documentation**: https://ds-223.github.io/Group-6/

---

## 📂 Branches

- **main**: Complete integrated system
- **db-9**: Database & ETL process
- **backend**: FastAPI backend service
- **frontend**: Streamlit frontend interface
- **ds**: Jupyter notebook environment
- **gh-pages**: GitHub Pages documentation deployment

---

## 🧰 Installation & Setup

### Prerequisites

Ensure you have the following installed:

- [Docker](https://www.docker.com/)
- [Docker Compose](https://docs.docker.com/compose/)

### Clone and Run

```bash
git clone https://github.com/hovhannisyan91/pythonmicroservicedesign.git](https://github.com/DS-223/Group-6.git

cd Supermarket_Hot_Deals

docker-compose up --build
```

# Employee Management System Documentation

## 🌐 Access the Application

| Service                | URL                          | Description |
|------------------------|------------------------------|-------------|
| Streamlit UI           | http://localhost:8501        | Interactive employee management interface |
| FastAPI (Swagger)      | http://localhost:8008/docs   | API documentation and testing interface |
| pgAdmin                | http://localhost:5050        | Database management tool for PostgreSQL |

**pgAdmin Login:**

###Email: admin@admin.com
Password: admin

💡 You may need to add a server manually the first time in pgAdmin. Use PostgreSQL default port and credentials from your `.env`.

## 🏗️ Project Structure


├── .github/
│   └── workflows/
├── Supermarket_Hot_Deals/
│   ├── Database/
│   ├── backend/
│   ├── ds/
│   ├── frontend/
│   ├── pgadmin_data/
│   │   └── sessions/
│   ├── .env
│   ├── __init__.py
│   └── docker-compose.yml
├── docs/
├── feedback/
├── .gitignore
├── LICENSE
├── Problem Definition.pdf
├── Readme.md
└── mkdocs.yml


 ## 🧪 API Features (FastAPI)

### Endpoints

| Endpoint            | Method | Description            |
|---------------------|--------|------------------------|
| `/employees/`       | POST   | Add a new employee     |
| `/employees/{id}`   | GET    | Get employee by ID     |
| `/employees/{id}`   | PUT    | Update salary          |
| `/employees/{id}`   | DELETE | Remove employee        |

📎 **Interact with these endpoints at:** [http://localhost:8008/docs](http://localhost:8008/docs)

Here is the screenshot of the Swagger: 

<img width="1510" alt="Screenshot 2025-05-13 at 11 22 00" src="https://github.com/user-attachments/assets/caa8f1c9-9182-4207-9889-cc550d96d6f0" />
<img width="1504" alt="Screenshot 2025-05-13 at 11 22 21" src="https://github.com/user-attachments/assets/94faf586-bec4-4165-9d04-76f1b15fe06b" />

---

## 📊 Streamlit Web Application

This service (`app/`) is responsible for the frontend interface:

<img width="1173" alt="Screenshot 2025-05-13 at 11 14 00" src="https://github.com/user-attachments/assets/656a76ac-2c9f-4b33-a108-dcf9090b3b5a" />


🌐 **Access it at:** [http://localhost:8501](http://localhost:8501)

---

## 🗃️ Database (PostgreSQL + pgAdmin)

The database is connected to the backend API. You can visualize or modify data directly using **pgAdmin**.

💡 **Instructions:**
- Create a server using the credentials in your `.env` file.
- Use `pgAdmin` to inspect tables and run SQL queries.

###This is the ERD:

<img width="564" alt="Screenshot 2025-05-13 at 20 59 09" src="https://github.com/user-attachments/assets/fed90c56-469f-4bd6-933f-16829ab99157" />

# 📘 MkDocs: Documentation

MkDocs generates beautiful HTML documentation from Markdown files.

---

## ✅ Prerequisites

Install the required dependencies:

```bash
pip install mkdocs-material
pip install 'mkdocstrings[python]'
```

## 🚀 How to Use MkDocs


   To see the documentation, type 
   
   ```bash
   mkdocs serve

   ```
   and click on the browser connection to open it in your browser.


---
**Next Steps**:  
- Link to [methodology](model.md) for technical details.  
- Refer to [database schema](database.md) for data collection structure.  
