help_str = """- Separate each item with a ','
- Enter battery as '+' and '-' in respective poll order following your direction, followed by its voltage. E.g. a 5v battery flowing from pos to neg, would be: +-5"""

def sum_of_list(list):
    sum = 0

    for item in list:
        sum += item

    return sum

def flip_list(list):
    for i in range(len(list)):
        list[i] = list[i] * -1
    return list

def string_to_parts(str):
    content = str.replace(" ", "").split(",")

    voltage = 0
    resistance = 0

    for item in content:
        if item[:2] == "-+":
            voltage += float(item[2:])
        elif item[:2] == "+-":
            voltage += float(item[2:])*-1
        else:
            resistance += float(item)

    return voltage, resistance


def find_directions(rows):
    row_directions = []

    for row in rows:
        voltage, resistance = string_to_parts(row)

        row_directions.append(voltage)

    avg_dir = 0

    for direction in row_directions:
        avg_dir += direction

    for i in range(len(row_directions)):
        if row_directions[i] == 0:
            row_directions[i] = avg_dir * -1

    return row_directions

def calculate_loop(row_a, row_b, direction_a, direction_b):
    a_voltage, a_resistance = string_to_parts(row_a)
    b_voltage, b_resistance = string_to_parts(row_b)

    if direction_a > 0:
        a_voltage = abs(a_voltage) * -1
        a_resistance = abs(a_resistance) * -1
    
    if direction_b > 0:
        b_voltage = abs(b_voltage) * -1
        b_resistance = abs(b_resistance) * -1

    

    voltage = a_voltage + b_voltage
    resistance = a_resistance + b_resistance

    return voltage, resistance

#
# Main
#     

no_of_loops = 2

rows = []

for i in range(no_of_loops+1):
    rows.append(str(input(f"Enter row {i+1}: ")))

row_directions = find_directions(rows)

voltage, resistance = calculate_loop(
    row_a=rows[0], direction_a=row_directions[0],
    row_b=rows[1], direction_b=row_directions[1]
)

print(voltage)
print(resistance)