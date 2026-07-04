from bot.client import *
from bot.orders import *

client = get_client()

response = place_order(
    client=client,
    symbol="BTCUSDT",
    side="BUY",
    order_type="MARKET",
    quantity=0.001
)

print(response)
