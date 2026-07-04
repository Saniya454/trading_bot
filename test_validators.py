from bot.validators import *

try:
    validate_quantity("-5")
except Exception as e:
    print(e)

try:
    validate_side("hello")
except Exception as e:
    print(e)

try:
    validate_price("abc")
except Exception as e:
    print(e)