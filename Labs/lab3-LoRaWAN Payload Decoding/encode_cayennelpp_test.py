# file: encode_cayennelpp_test.py
# https://github.com/smlng/pycayennelpp
# pip3 install pycayennelpp
# consult some CayenneLPP docs as: 
# https://github.com/myDevicesIoT/cayenne-docs/blob/master/docs/LORA.md
# or the links in Learn
# Encoding
from cayennelpp import LppFrame
import binascii

# create empty frame
frame = LppFrame()
# add some sensor data
frame.add_temperature(1, 27.2)
frame.add_humitidy(2, 64.5)
frame.add_analog_output(3, 0.4)
frame.add_gps(4, 60.48726, 15.40954, 150)
# get byte buffer in CayenneLPP format
buffer = frame.bytes()
# will print the string / byte literal
# https://stackoverflow.com/questions/6269765/what-does-the-b-character-do-in-front-of-a-string-literal
print(buffer)
# to get the proper hexadecimal representation for C# use
print(binascii.hexlify(buffer))