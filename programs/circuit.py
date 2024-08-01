help_str = """- Separate each item with a ','
- Enter battery as '+' and '-' in respective poll order following your direction, followed by its voltage. E.g. a 5v battery flowing from pos to neg, would be: +-5"""

def string_to_maths(string):
    content = string.replace(" ", "").split(",")

    list = []

    for item in content:
        if item[:2] == "-+":
            list.append(float(item[2:])*(direction))
        elif item[:2] == "+-":
            list.append(float(item[2:])*(direction*-1))
        elif item == "N":
            list.append(0)
        else:
            list.append(int(item))

    return list
    
def combine(a, b):
    for i in range(len(b)):
        a.append(b[i])
    return a

rot_directions = {1: "clockwise", -1: "counter-clockwise"}
lin_directions = {1: "left to right", -1: "right to left"}
direction = int(input("Clockwise (1), Counter-clockwise (-1)\nChoose direction: "))

no_of_loops = int(input("Enter number of loops: "))

maths = []

outside_loop = str(input(f"Your direction is {rot_directions[direction]}. Enter the outside loop content: "))

bridges = {}

for i in range(no_of_loops-1):
    bridges[i] = str(input(f"Your direction is {lin_directions[direction]}. Enter the content of bridge {i}: "))

print(string_to_maths(outside_loop))
print(string_to_maths(bridges[i]))

