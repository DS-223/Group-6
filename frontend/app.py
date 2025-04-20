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

col1, col2, col3 = st.columns([1, 1, 2])
with col1:
    st.button("Default")
with col2:
    st.button("A-Z")
with col3:
    st.button("List view")

st.markdown("---")

products = [
    {
        "name": "Heirloom tomato",
        "price": "$5.99 / lb",
        "origin": "Grown in San Juan Capistrano, CA",
        "image": "https://upload.wikimedia.org/wikipedia/commons/8/89/Tomato_je.jpg"
    },
    {
        "name": "Organic ginger",
        "price": "$12.99 / lb",
        "origin": "Grown in Huntington Beach, CA",
        "image": "https://upload.wikimedia.org/wikipedia/commons/9/9c/Zingiber_officinale_Roscoe.JPG"
    },
    {
        "name": "Organic cucumber",
        "price": "$7.99 / lb",
        "origin": "Grown in Huntington Beach, CA",
        "image": "https://upload.wikimedia.org/wikipedia/commons/e/e0/Cucumber_BDL.jpg"
    },
]

cols = st.columns(3)

for col, product in zip(cols, products):
    with col:
        st.image(product["image"], use_column_width=True)
        st.markdown(f"**{product['name']}**")
        st.markdown(f"<span style='color:green; font-weight:bold'>{product['price']}</span>", unsafe_allow_html=True)
        st.caption(product["origin"])
