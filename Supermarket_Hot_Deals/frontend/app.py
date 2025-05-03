import streamlit as st

st.set_page_config(page_title="Supermarket Hot Sales", layout="wide")

st.markdown("""
    <style>
    img {
        height: 220px !important;
        object-fit: cover !important;
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.title("Navigation")
st.sidebar.radio("Go to", ["Shop", "Newsstand", "Who we are", "My profile"])

if "basket" not in st.session_state:
    st.session_state.basket = []

st.sidebar.markdown(f"🧺 **Basket items**: {len(st.session_state.basket)}")

st.title("Supermarket Hot Sales")
st.caption("April 10, 2025")

search = st.text_input("🔍 Search for a product")
sort_option = st.selectbox("Sort by", ["Default", "Price Low to High", "Price High to Low"])

products = [
    {"name": "Heirloom tomato", "price": 5.99, "unit": "$5.99 / lb", "origin": "San Juan Capistrano, CA", "image": "images/tomato.png"},
    {"name": "Organic ginger", "price": 12.99, "unit": "$12.99 / lb", "origin": "Huntington Beach, CA", "image": "images/ginger.png"},
    {"name": "Organic cucumber", "price": 7.99, "unit": "$7.99 / lb", "origin": "Huntington Beach, CA", "image": "images/cucumber.png"},
    {"name": "Green bell pepper", "price": 3.99, "unit": "$3.99 / lb", "origin": "Fresno, CA", "image": "images/pepper.png"},
    {"name": "Baby spinach", "price": 2.49, "unit": "$2.49 / bag", "origin": "Salinas Valley, CA", "image": "images/spinach.png"},
    {"name": "Strawberries", "price": 6.99, "unit": "$6.99 / box", "origin": "Watsonville, CA", "image": "images/strawberry.png"}
]

filtered = [p for p in products if search.lower() in p["name"].lower()]

if sort_option == "Price Low to High":
    filtered = sorted(filtered, key=lambda x: x["price"])
elif sort_option == "Price High to Low":
    filtered = sorted(filtered, key=lambda x: x["price"], reverse=True)

products_per_page = 3
max_page = (len(filtered) - 1) // products_per_page

if "page" not in st.session_state:
    st.session_state.page = 0

col_left, _, col_right = st.columns([1, 10, 1])
with col_left:
    if st.button("⬅️"):
        st.session_state.page = max(0, st.session_state.page - 1)
with col_right:
    if st.button("➡️"):
        st.session_state.page = min(max_page, st.session_state.page + 1)

start = st.session_state.page * products_per_page
end = start + products_per_page
current_products = filtered[start:end]

cols = st.columns(3)
for col, product in zip(cols, current_products):
    with col:
        st.image(product["image"], use_container_width=True)
        with st.expander(f"{product['name']} - {product['unit']}"):
            st.write(f"📍 Origin: {product['origin']}")
            if st.button(f"Add {product['name']} to basket"):
                st.session_state.basket.append(product["name"])
                st.success(f"{product['name']} added to basket ✅")

st.markdown("---")
st.markdown("© 2025 Supermarket Hot Sales — Built with ❤️ using Streamlit")
