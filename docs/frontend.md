# 📘 Frontend Documentation

## 🚀 Setup & Configuration

### 📦 Environment Variables (`.env`)

The `.env` file is used to store environment variables that are required to connect to the backend and database. It contains:

```python
DATABASE_URL=postgresql://postgres:admin1234@db:5432/supermarket_hot_deals_db
DB_USER=postgres
DB_PASSWORD=admin1234
DB_NAME=supermarket_hot_deals_db
```
- **DATABASE_URL**: The connection string to connect to the PostgreSQL database.
- **DB_USER**: The database user (default is `postgres`).
- **DB_PASSWORD**: The password for the database user.
- **DB_NAME**: The name of the database (`supermarket_hot_deals_db`).
- **PGADMIN_EMAIL**: The email used to access pgAdmin (do not change).
- **PGADMIN_PASSWORD**: The password for pgAdmin (do not change).

## Dependencies (`requirements.txt`)

The `requirements.txt` file contains the dependencies for the frontend:

- **streamlit**: The main dependency for building the web application.
- **requests**: A library for making HTTP requests (though not used in `app.py`, it might be used elsewhere).


### 🐳 `Dockerfile`
This Dockerfile is used to set up the frontend container to run a Streamlit application. Here's a breakdown of its contents:

   - Specifies the base image for the container, which is Python 3.9 in a slim variant to keep the image lightweight.

   - Sets the working directory inside the container to `/app`.

   - Copies the `requirements.txt` file into the `/app` directory of the container.


   - Installs the required Python dependencies listed in `requirements.txt` without caching to reduce the image size.


   - Copies all the files from the local directory into the container’s `/app` directory.

   - Defines the command to run the Streamlit application using `streamlit run app.py`, binding the server to all network interfaces (`0.0.0.0`).


### `app.py`
This is the main application file for the frontend. It uses **Streamlit** to build an interactive web page for browsing supermarket products.

- **Page Configuration**: The app's title is set to "Supermarket Hot Sales" with a wide layout.
- **Sidebar**: 
  - The sidebar allows users to navigate between pages such as "Shop", "Newsstand", "Who we are", and "My profile".
  - It displays the current number of items in the basket.
  
- **Product Search & Sorting**:
  - Users can search for products by name and sort them by price (low to high or high to low).
  - The products are displayed in a grid format, with 3 products per page. Users can navigate between pages using the "⬅️" and "➡️" buttons.
  
- **Product Display**:
  - Products are shown with their image, name, price, and origin.
  - Each product has an option to add it to the basket. When added, a success message appears.

- **Pagination**: 
  - The app supports pagination to display products in chunks of 3.
  
- **Footer**: 
  - The footer displays the copyright notice and credits for the app.


### General Workflow:
- When the frontend container is started, it runs the Streamlit app, allowing users to browse and add items to their basket in the "Supermarket Hot Sales" application.
- The app displays products with filtering and sorting capabilities, with pagination to navigate through multiple products.
