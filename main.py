import formulas

print("Are you interested in")
print("1 Calculating the area of an circle")
print("2 Calculating the volume of an cube")
print("3 Calculating the area of an rectangle")

number = input("What do you want to do? ")

# Ad a loop so you can do multiple diffferent calculations

if int(number) == 1:
    r = input("What is the radius of your circle?")
    answer = formulas.areaOfCircle(float(r))
    print(f"Area of your circle is {answer}!")
if int(number) == 2:
    x = input("How long is one side of you cube?")
    answer = formulas.cubesVolume(float(x))
    print(f"Volume of your cube is {answer}")
if int(number) == 3:
    h = input("How high is your rectagle?")
    w = input("How wide is your rectangle?")
    answer = formulas.rectangleArea(float(h), float(w))
    print(f"Area of you rectangle is {answer}")