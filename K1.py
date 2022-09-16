import random
import sys
import time
def mengetik(s):
  for c in s + '\n':
       sys.stdout.write(c)
       sys.stdout.flush()

       time.sleep(random.random() * 0.8)

mengetik('SELAMAT DATANG DI CYBER KAZE eror21\nSELAMAT DATANG KAZE CYBER\n.')
