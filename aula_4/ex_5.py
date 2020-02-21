import random
import string
import re
import datetime


x =  [1,2,35,7,9,0,12,65,87,-1,0,7]

print(string.ascii_lowercase)
print(string.ascii_uppercase)

print(sorted(x))
print(sorted(x, reverse = True))
hoje = datetime.datetime.now()
daqui_trinta_dias = hoje + datetime.timedelta(days=30)
print(hoje)
print(daqui_trinta_dias)