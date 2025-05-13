# Supermarket Hot Deals – Group Project
# Employee Management System

A Dockerized microservice project for managing employee records using FastAPI, Streamlit, PostgreSQL, and pgAdmin. This project also includes ETL processing and documentation hosted using MkDocs.

---

## 🚀 Quick Links

- 🔗 **Streamlit UI**: [http://localhost:8501](http://localhost:8501)
- 🔗 **FastAPI Swagger Docs**: [http://localhost:8008/docs](http://localhost:8008/docs)
- 🔗 **pgAdmin Interface**: [http://localhost:5050](http://localhost:5050)
- 🔗 **Documentation**: [http://127.0.0.1:8000](http://127.0.0.1:8000](https://ds-223.github.io/Group-6/))

---

## 📂 Branches

- **main**: Complete integrated system
- **db-setup**: Database & ETL process
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

- ➕ Add new employees  
- 📋 View employee table  
- 📝 Update salaries  
- ❌ Delete records  

🌐 **Access it at:** [http://localhost:8501](http://localhost:8501)
<img width="1173" alt="Screenshot 2025-05-13 at 11 14 00" src="https://github.com/user-attachments/assets/656a76ac-2c9f-4b33-a108-dcf9090b3b5a" />

---

## 🗃️ Database (PostgreSQL + pgAdmin)

The database is connected to the backend API. You can visualize or modify data directly using **pgAdmin**.

💡 **Instructions:**
- Create a server using the credentials in your `.env` file.
- Use `pgAdmin` to inspect tables and run SQL queries.

![Uploading Screenshot 2025-05-13 at 12.16.54.png…]()


##  How to Run the Project



Make sure Docker is installed and running. Then, in the `Supermarket_Hot_Deals/` directory:

```bash
docker-compose up -d
```
