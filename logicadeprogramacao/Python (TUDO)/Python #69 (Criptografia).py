import random
import string
import time

while True:
    senha = string.ascii_letters + string.hexdigits
    senhagerada = ''.join(random.choices(senha, k = 100))
    print(senhagerada)
    time.sleep(3)
    break
