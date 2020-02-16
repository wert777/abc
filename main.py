import time
import random


codes = [31, 32, 33, 34, 35, 36, 37, 91, 92, 93, 94, 95, 96, 97]
a = ord("А")
print()


def tr(a):
    time.sleep(0.3)
    tr = f"{chr(155)}{random.choice(codes)};1m{chr(i)}"
    return tr


for i in range(a, a + 32):
    res = tr(a)
    print(res, end=" ", flush=True)
print("\x1b[0m")
