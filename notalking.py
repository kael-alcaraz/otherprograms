import random
import time

x = random.uniform(0.0, 10.0)
y = random.uniform(0.0, 10.0)
print('"..."')
time.sleep(x)
print(f"[\x1B[3mYou waited {x :.0f} seconds for the character that doesn't talk, expecting them to talk.\x1B[0m]")
time.sleep(2)
print('"..."')
time.sleep(y)
print(f"[\x1B[3mYou waited {y :.0f} seconds for the character that doesn't talk, expecting them to talk.\x1B[0m]")