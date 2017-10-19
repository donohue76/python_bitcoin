# import bitcoin
from bitcoin import *

# generate Private Key
my_private_key = random_key()
print("Private Key: %s\n" % my_private_key)

# generate Public key
my_public_key = privtopub(my_private_key)
print(my_public_key)

# create a bitcoin address (single use token)
my_address = pubtoaddr(my_public_key)
print(my_address)