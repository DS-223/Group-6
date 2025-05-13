import streamlit as st
import requests

st.set_page_config(page_title="Supermarket Hot Sales", layout="wide")

if "basket" not in st.session_state:
    st.session_state.basket = []

st.sidebar.title("Navigation")
st.sidebar.radio("Go to", ["Shop", "Newsstand", "Who we are", "My profile"])
st.sidebar.markdown(f"🧺 **Basket items**: {len(st.session_state.basket)}")

st.title("Supermarket Hot Sales")
st.caption("April 10, 2025")

project_id = 1 
try:
    response = requests.get("http://backend:8000/ads/sample", params={"project_id": project_id})
    if response.status_code == 200:
        data = response.json()
        products = [
            {
                "bandit_id": item["bandit_id"],
                "name": item["bandit_name"],
                "image": f"images/{item['bandit_name'].lower().replace(' ', '_')}.png"
            } for item in data
        ]
    else:
        st.error("⚠️ Failed to fetch ads from backend.")
        products = []
except Exception as e:
    st.error(f"🚫 Error connecting to backend: {e}")
    products = []

products_per_page = 3
if "page" not in st.session_state:
    st.session_state.page = 0

cols = st.columns(3)
for col, product in zip(cols, products):
    with col:
        st.image(product["image"], use_container_width=True)
        with st.expander(f"{product['name']}"):
            st.write("📍 No location info")
            if st.button(f"Add {product['name']} to basket"):
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

st.markdown("---")
st.markdown("© 2025 Supermarket Hot Sales — Built with ❤️ using Streamlit")
