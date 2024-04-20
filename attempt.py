#pythogras theorem
print('This is how you find hypotemuse of a triangle using pythogras theorem!')
side_a = float(input('the width of the triangle is:  ')) #entering the width
side_b = float(input('the height of the triangle is:  ')) #entering the height
hypotemuse = (float(side_a **2) + float(side_b**2))**0.5 #tried to put it a little diffrent to ive float numbers as well
print('Therefore the hypotemus of the tiangle is ' + str(hypotemuse))
if hypotemuse < 20:
    print('that is a small ass hypo')
else:
        print('pretty solid dude!')
