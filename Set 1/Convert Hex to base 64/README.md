# Challenge 1: Convert hex to base64

## Objective
Convert a hex-encoded string to Base64 format, strictly operating on raw bytes.

## Approach
This first challenge can be efficiently solved using Python's standard `base64` library. The logic follows these steps:

1. **Hexadecimal Decoding:** We take the input string and convert it into raw bytes using the native `bytes.fromhex()` method. *(Note: If we print these raw bytes to the console, Python automatically attempts to decode them using ASCII, revealing the hidden plaintext message).*

2. **Base64 Encoding:** Once we have isolated the raw bytes, we apply the `base64.b64encode()` function to transform them into the target format.

3. **Output Formatting:** Since the encoded result is still a bytes object (indicated by Python's `b'...'` prefix), we use the `.decode('utf-8')` method to clean the output. This returns a standard string, exactly matching the expected output of the challenge.