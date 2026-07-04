import streamlit as st

st.set_page_config(
    page_title="Trading Bot",
    page_icon="📈",
    layout="centered"
)

st.title("📈 Binance Futures Testnet Trading Bot")

from bot.client import get_client
from bot.orders import place_order
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price,
)
symbol = st.text_input(
    "Trading Symbol",
    value="BTCUSDT"
)

side = st.selectbox(
    "Side",
    ["BUY", "SELL"]
)

order_type = st.selectbox(
    "Order Type",
    ["MARKET", "LIMIT"]
)

quantity = st.number_input(
    "Quantity",
    min_value=0.0,
    value=0.001,
    step=0.001,
    format="%.3f"
)
price = None

if order_type == "LIMIT":
    price = st.number_input(
        "Price",
        min_value=0.0,
        value=100000.0,
        step=100.0
    )
if st.button("Place Order"):
    try:

        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)

        if order_type == "LIMIT":
            price = validate_price(price)

        st.success("Validation Successful!")
        client = get_client()
        response = place_order(
                client,
                symbol,
                side,
                order_type,
                quantity,
                price
            )
        st.success("Order Placed Successfully!")
        st.subheader("Order Summary")

        st.write(f"**Symbol:** {symbol}")
        st.write(f"**Side:** {side}")
        st.write(f"**Type:** {order_type}")
        st.write(f"**Quantity:** {quantity}")

        if order_type == "LIMIT":
            st.write(f"**Price:** {price}")

        st.subheader("Order Response")

        st.write("**Order ID:**", response.get("orderId"))
        st.write("**Status:**", response.get("status"))
        st.write("**Executed Quantity:**", response.get("executedQty"))
        st.write("**Average Price:**", response.get("avgPrice"))

        with st.expander("Full API Response"):

            st.json(response)

    except Exception as e:

        st.error(str(e))