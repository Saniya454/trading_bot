import os
from dotenv import load_dotenv
from binance.client import Client

load_dotenv()


TESTNET_URL = "https://testnet.binancefuture.com"

def get_client():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")

    if not api_key or not api_secret:
        raise ValueError("API_KEY or API_SECRET not found in .env")

    client = Client(api_key, api_secret)

    # Point the client to the Futures Testnet
    client.FUTURES_URL = TESTNET_URL + "/fapi"

    return client