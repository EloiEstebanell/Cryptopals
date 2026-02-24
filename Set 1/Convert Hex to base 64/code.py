import base64

# 1. Initial message
hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

# 2. We convert the hexadecimal to raw bytes
raw_bytes = bytes.fromhex(hex_string)


# 3. We convert the raw bytes to Base64.
b64_bytes = base64.b64encode(raw_bytes)

# 4. We print the result, decoding the byte string to obtain a text string (str).
print(b64_bytes.decode('utf-8'))

if b64_bytes.decode('utf-8') =="SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t":
    print("It's the same string")