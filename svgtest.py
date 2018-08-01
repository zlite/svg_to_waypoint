# Read SVG into a list of path objects and list of dictionaries of attributes
from svgpathtools import Path, Line, QuadraticBezier, CubicBezier, Arc, svg2paths, wsvg
#from pprint import pprint
import re

paths, attributes = svg2paths('blueprint.svg')
#pprint(paths)

path1 = paths[0][1]
path2 = paths[0][2]
path3 = attributes[1]
for key,val in path3.items():
    print (key, "=>", val)
line1 = path1.start
line_text = str(line1)
print (type(line1))
print ("Start ", line1)
test = [""]*100  # initialize the list
counter = 0
for z in line_text:
    if z == "+":
        counter = counter + 1
    if ((z != "(") and (z != ")") and (z != "j") and (z!="+")):
        test[counter] = test[counter] + z 
test[0] = float(test[0])
test[1] = float(test[1])
print("X =", test[0], "Y =", test[1])    
# x1 = re.findall([0-9],str(line_text[0]))
# print(redpath_attribs['stroke'])
