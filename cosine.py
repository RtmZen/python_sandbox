# Program "Cosine"
# v.03

import math
from math import cos, pi

angle = raw_input ("Enter an angle in degrees: ")
angle = float(angle) * pi / 180
res = round(cos(angle), 3)

print "Cosine is %s" % (str(res))