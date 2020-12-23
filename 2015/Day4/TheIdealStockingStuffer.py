import hashlib
import time

t1 = time.time()

number = 1
secretKey = "bgvyzdsv"
while(True):
    input = secretKey + str(number)
    hashResult = hashlib.md5(input.encode('utf-8'))
    if(hashResult.hexdigest().startswith("000000")):
        break;
    number += 1

print(number)
print("Time passed : ", end = "")
print(time.time() - t1)

