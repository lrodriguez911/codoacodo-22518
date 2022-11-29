# import a function

from saludos import saludar
saludar() 


#import all functions
""" from saludos import *

saludar_dos("Lucas") """


#import a one function that can access an another funtion
from saludos import saludar_tres

saludar_tres('Tucuman')