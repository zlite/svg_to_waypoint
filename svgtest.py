# Read SVG into a list of path objects and list of dictionaries of attributes
from svgpathtools import Path, Line, QuadraticBezier, CubicBezier, Arc, svg2paths, wsvg
import re, csv

paths, attributes = svg2paths('blueprint.svg')
path = attributes[1]  # get the attributes (data) from the path object
data = path['d'] # do a dictionary lookup for the data following the 'd'
data = str(data) # convert it to a string
print('Data = ', data)
x = re.findall('\d*\.\d*(?=L)', data)  # regex finds data before the L (x's)
print('Xs: ', x)
y = re.findall('(?<=L)\d*\.?\d*', data)  # regex finds data after the L (y's)
print('Ys: ', y)
print('Sample waypoint: ',x[3],y[3])
with open('waypoint.csv','w') as data:   # write the waypoints to a file
    data.write(str(x))
    data.write(str(y))
print("Done")
