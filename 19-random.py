# Can we make truly random numbers?
# Yes. In order to generate a truly random number on our computers we need to get the random data from some outside source. This outside source is generally our keystrokes, mouse movements, data on network etc
import random as r

x = r.randint(100)

print(x)
