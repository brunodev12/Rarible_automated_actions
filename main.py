import os
import time
from services.get_wei_value import getWeiValue
from services.create_orders import createOrder
from services.generate_salt import generateSalt
from services.get_signature import getSignature
from services.get_value import getValue

address = os.environ.get('ADDRESS')

value = getValue()
value_in_wei = str(getWeiValue(value))
print("MY ORDER: ", value_in_wei)
salt = generateSalt()
salt_integer = int(salt, 16)
order_duration = int(time.time()) + 3600
signature = getSignature(address, value=value_in_wei,
                         order_duration=order_duration, salt=salt)

if signature == None:
    quit()

createOrder(salt_integer, signature, order_duration, value_in_wei)

