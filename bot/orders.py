from bot.logging_config import logger


def place_order(client, symbol, side, order_type, quantity, price=None):
    """
    Places a MARKET or LIMIT order on Binance Futures Testnet.
    """

    try:

        # Log request
        logger.info(
            f"Request -> Symbol={symbol}, Side={side}, "
            f"Type={order_type}, Quantity={quantity}, Price={price}"
        )

        params = {
            "symbol": symbol,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }

        # LIMIT orders require price and timeInForce
        if order_type == "LIMIT":
            params["price"] = price
            params["timeInForce"] = "GTC"

        response = client.futures_create_order(**params)

        logger.info(f"Response -> {response}")

        return response

    except Exception as e:

        logger.error(f"Order failed: {e}")

        raise