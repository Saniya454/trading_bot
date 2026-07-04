
def validate_side(side):
    """
    Validate the order side.
    """

    side = side.upper()

    if side not in ["BUY", "SELL"]:
        raise ValueError("Side must be BUY or SELL.")

    return side
def validate_order_type(order_type):
    """
    Validate order type.
    """

    order_type = order_type.upper()

    if order_type not in ["MARKET", "LIMIT"]:
        raise ValueError("Order type must be MARKET or LIMIT.")

    return order_type
def validate_quantity(quantity):
    """
    Validate quantity.
    """

    try:
        quantity = float(quantity)
    except ValueError:
        raise ValueError("Quantity must be a number.")

    if quantity <= 0:
        raise ValueError("Quantity must be greater than zero.")

    return quantity
def validate_price(price):
    """
    Validate price.
    """

    try:
        price = float(price)
    except ValueError:
        raise ValueError("Price must be a number.")

    if price <= 0:
        raise ValueError("Price must be greater than zero.")

    return price

def validate_symbol(symbol):
    """
    Validate the trading symbol.

    """
    print("Inside validate_symbol")
    if not symbol:
        raise ValueError("Symbol cannot be empty.")

    return symbol.upper()