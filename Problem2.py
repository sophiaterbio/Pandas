import pandas as pd

cars = pd.read_csv('cars.csv')
odd = cars.iloc[[0,1,2,3,4],[0,2,4,6,8,10]]
print (odd)

mazda = cars[:1]
print ('\nMazda RX4:\n')
print (mazda)

cyl = cars.loc[[23],['Model','cyl']]
print ('\nCylinders of Camaro Z28:\n')
print (cyl)

cylgear = cars.loc[[1,28,18],['Model','cyl','gear']]
print ('\nCylinders and Gear types of Mazda RX4, Ford Pantera L, and Honda Civic:\n')
print (cylgear)
