import random
import hashlib

result = "123456"
while result[:3] != "000":
    s = str(random.random())
    result = hashlib.sha256(s.encode()).hexdigest()

print(f'{s} - {result}')