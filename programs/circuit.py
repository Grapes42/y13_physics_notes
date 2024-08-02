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

    equation = f"{i_0}(I of row 1) + {i_1}(I of row 2) + {i_2}(I of row 3) = {voltage}"

    return equation



#
# Main
#
no_of_loops = 2
rows = []

letters = {1: "A", 2: "B", 3: "C"}

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
print(calculate_loop(rows, 0, 1))
print(calculate_loop(rows, 1, 2))
print("-1 + -1 + 1 = 0")