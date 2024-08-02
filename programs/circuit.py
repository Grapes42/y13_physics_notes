"""
Steps to solve 2 loop circuit:

- Get user input for circuit content
- Calculate voltage and resistance of each row
- Determine direction of each row
- Determine loop equation
"""

class Row():
    def __init__(self, input_string) -> None:
        content = input_string.replace(" ", "").split(",")

        self.voltage = 0
        self.resistance = 0
        self.direction = 0

        for item in content:
            if item[:2] == "-+":
                self.voltage += float(item[2:])
            elif item[:2] == "+-":
                self.voltage += float(item[2:])*-1
            else:
                self.resistance += float(item)

#
# Functions
#
def return_currents(i_0=0, i_1=0, i_2=0):
    return i_0, i_1, i_2

def calculate_loop(rows, a, b):
    currents = {0:"i_0", 1:"i_1", 2:"i_2"}

    voltage_a = rows[a].voltage * rows[a].direction
    voltage_b = rows[b].voltage * rows[b].direction * -1

    voltage = voltage_a + voltage_b

    resistance_a = rows[a].resistance * rows[a].direction * -1
    resistance_b = rows[b].resistance * rows[b].direction

    i_0, i_1, i_2 = eval(f"return_currents({currents[a]}=resistance_a, {currents[b]}=resistance_b)")

    return [i_0, i_1, i_2, voltage]



#
# Main
#
no_of_loops = 2
rows = []

# Get all inputs
for i in range(no_of_loops+1):
    rows.append(
        Row(str(input(f"Enter row {i+1}: ")))
    )

#
# Finding direction
#

avg_direction = 0

# Determine all easy to find directions,
# and create an average direction
for row in rows:
    if row.voltage < 0:
        row.direction = -1
    elif row.voltage > 0:
        row.direction = 1

    avg_direction += row.direction

# Find any row that has no direction, and use 
# Kirchoff's law to determine its direction
for row in rows:
    if row.direction == 0:
        if avg_direction < 0:
            row.direction = 1
        else:
            row.direction = -1

# Calculate loops
loops = []
for i in range(no_of_loops):
    loops.append(calculate_loop(rows, i, i+1))

print("\nHere are your equations: ")
for loop in loops:
    print(f"{loop[0]}(I of row 1) + {loop[1]}(I of row 2) + {loop[2]}(I of row 3) = {loop[3]}")
print("-1 + -1 + 1 = 0")

print("\nHere is what you put in your calculator:")
for loop in loops:
    print(f"{loop[0]}, {loop[1]}, {loop[2]}, {loop[3]}")
print("-1, -1, 1, 0")

print("""\nYour outputs will be:
x = I of first row
y = I of second row
z = I of third row""")