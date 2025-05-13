"""
Supermarket Hot Sales - Streamlit Frontend

This Streamlit app displays current supermarket deals. Users can:
- Search for products
- Sort by price
- View paginated product listings with images
- Add items to a shopping basket

Built with ❤️ using Streamlit.
"""
import streamlit as st
import requests

# Set Streamlit page configuration
st.set_page_config(page_title="Supermarket Hot Sales", layout="wide")

# Add custom CSS styling for product images
st.markdown("""
    <style>
    img {
        height: 220px !important;
        object-fit: cover !important;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("Navigation")
st.sidebar.radio("Go to", ["Shop", "Newsstand", "Who we are", "My profile"])

# Initialize basket in session state
if "basket" not in st.session_state:
    st.session_state.basket = []

st.sidebar.markdown(f"🧺 **Basket items**: {len(st.session_state.basket)}")

# Page title and subtitle
st.title("Supermarket Hot Sales")
st.caption("April 10, 2025")

# Get products from backend (if available)
project_id = 1
products = []
try:
    response = requests.get("http://backend:8000/ads/sample", params={"project_id": project_id})
    if response.status_code == 200:
        data = response.json()
        products = [
            {
                "bandit_id": item["bandit_id"],
                "name": item["bandit_name"],
                "price": 5.0,  # Placeholder price
                "unit": "N/A",  # Add units if available
                "origin": "N/A",  # Add origin if available
                "image": f"images/{item['bandit_name'].lower().replace(' ', '_')}.png"
            } for item in data
        ]
    else:
        st.error("⚠️ Failed to fetch ads from backend.")
except Exception as e:
    st.error(f"🚫 Error connecting to backend: {e}")

# Search and sort inputs
search = st.text_input("🔍 Search for a product")
sort_option = st.selectbox("Sort by", ["Default", "Price Low to High", "Price High to Low"])

# Filter and sort
filtered = [p for p in products if search.lower() in p["name"].lower()]
if sort_option == "Price Low to High":
    filtered = sorted(filtered, key=lambda x: x["price"])
elif sort_option == "Price High to Low":
    filtered = sorted(filtered, key=lambda x: x["price"], reverse=True)

# Pagination setup
products_per_page = 3
max_page = (len(filtered) - 1) // products_per_page
if "page" not in st.session_state:
    st.session_state.page = 0

# Navigation buttons
col_left, _, col_right = st.columns([1, 10, 1])
with col_left:
    if st.button("⬅️"):
        st.session_state.page = max(0, st.session_state.page - 1)
with col_right:
    if st.button("➡️"):
        st.session_state.page = min(max_page, st.session_state.page + 1)

# Display current page's products
start = st.session_state.page * products_per_page
end = start + products_per_page
current_products = filtered[start:end]

cols = st.columns(3)
for col, product in zip(cols, current_products):
    with col:
        st.image(product["image"], use_container_width=True)
        with st.expander(f"{product['name']}"):
            st.write(f"📍 {product.get('origin', 'Unknown')}")
            st.write(f"💲 {product.get('unit', 'Price not available')}")
            if st.button(f"Add {product['name']} to basket", key=product['name']):
                st.session_state.basket.append(product["name"])
                try:
                    click_url = f"http://backend:8000/ads/{product['bandit_id']}/click"
                    click_response = requests.post(click_url, params={"project_id": project_id})
                    if click_response.status_code == 200:
                        st.success(f"{product['name']} added & click registered ✅")
                    else:
                        st.warning("Failed to register click.")
                except Exception as e:
                    st.error(f"Error posting click: {e}")

# Footer
st.markdown("---")
st.markdown("© 2025 Supermarket Hot Sales — Built with ❤️ using Streamlit")
