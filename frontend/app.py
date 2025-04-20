import streamlit as st

st.set_page_config(page_title="Supermarket Hot Sales", layout="wide")

st.markdown("""
    <style>
    .top-nav {
        display: flex;
        justify-content: space-between;
        align-items: center;
        font-size: 18px;
        padding: 10px 0 0 0;
        margin-bottom: 10px;
    }
    .nav-links span {
        margin: 0 15px;
        cursor: pointer;
        color: #444;
    }
    .basket-btn {
        background-color: #5A7D42;
        padding: 8px 16px;
        border-radius: 6px;
        color: white;
        font-weight: bold;
    }
    </style>
    <div class="top-nav">
        <div style="font-size:26px; font-weight:bold; color:#4B6A24;">Supermarket</div>
        <div class="nav-links">
            <span>Shop</span><span>Newsstand</span><span>Who we are</span><span>My profile</span>
        </div>
        <div class="basket-btn">Basket (3)</div>
    </div>
""", unsafe_allow_html=True)

st.markdown("## Hot Sales")
st.caption("April 10, 2025")

products = [
    {
        "name": "Heirloom tomato",
        "price": "$5.99 / lb",
        "origin": "Grown in San Juan Capistrano, CA",
        "image": "images/tomato.png"
    },
    {
        "name": "Organic ginger",
        "price": "$12.99 / lb",
        "origin": "Grown in Huntington Beach, CA",
        "image": "images/ginger.png"
    },
    {
        "name": "Organic cucumber",
        "price": "$7.99 / lb",
        "origin": "Grown in Huntington Beach, CA",
        "image": "images/cucumber.png"
    },
    {
        "name": "Green bell pepper",
        "price": "$3.99 / lb",
        "origin": "Grown in Fresno, CA",
        "image": "images/pepper.png"
    },
    {
        "name": "Baby spinach",
        "price": "$2.49 / bag",
        "origin": "Grown in Salinas Valley, CA",
        "image": "images/spinach.png"
    },
    {
        "name": "Strawberries",
        "price": "$6.99 / box",
        "origin": "Grown in Watsonville, CA",
        "image": "images/strawberry.png"
    }
]

products_per_page = 3
max_page = len(products) 

if "page" not in st.session_state:
    st.session_state.page = 0

col_left, col_center, col_right = st.columns([1, 10, 1])

with col_left:
    if st.button("⬅️"):
        st.session_state.page = max(0, st.session_state.page - 1)

with col_right:
    if st.button("➡️"):
        st.session_state.page = min(max_page, st.session_state.page + 1)

start = st.session_state.page * products_per_page
end = start + products_per_page
current_products = products[start:end]

cols = st.columns(3)
for col, product in zip(cols, current_products):
    with col:
        st.image(product["image"], use_container_width=True)
        st.markdown(f"""
            <div style="text-align:center;">
                <h4 style="margin:0;">{product['name']}</h4>
                <p style="color:green; font-weight:bold; margin:5px 0;">{product['price']}</p>
                <p style="font-size:13px; color:#666;">{product['origin']}</p>
            </div>
        """, unsafe_allow_html=True)
