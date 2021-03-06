from origin import data_types
import random
import struct
import string

def random_data( dtype ):
    if dtype.find("int") != -1:
        x = long(random.randint(0,2**32-1))
        x *= 2**32
        x += random.randint(0,2**32-1)
        size = data_types[dtype]["size"]
        data = struct.pack("!Q", x)[8-size:]
        return struct.unpack("!"+data_types[dtype]["format_char"], data)[0]
        
    elif (dtype == "float") or (dtype == "double"):
        return random.random() # not sure how to make a double
    elif dtype == "string":
        length = int(data_types["string"]["numpy"][1:])
        return ''.join(random.choice(string.lowercase) for i in range(length))
    else:
        return None
