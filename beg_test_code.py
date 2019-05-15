#! python
# Create a message and print it out to the screen

filename = 'C:\\python scripts\\bmifile.txt'
with open(filename) as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line)


#convert to metrics
print(str(x))
print(str(y))

kilograms = int(x) / 2.2046
meters = int(y) / 39.370

#calculate BMI
BMI = kilograms / (meters * meters)

#print BMI
print(str(BMI))
