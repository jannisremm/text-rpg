import random


def map_generator(width, height):
    map = []
    square1_x_start = random.randint(1, width // 2)
    square1_y_start = random.randint(1, height // 2)
    square1_size = random.randint(min(height, width) // 4, min(height, width) // 2)
    square2_x_start = random.randint(width // 2, width - 4)
    square2_y_start = random.randint(1, height // 2)
    square2_size = random.randint(min(height, width - 4) // 4, min(height, width) // 2)
    square3_x_start = random.randint(1, width // 2)
    square3_y_start = random.randint(height // 2, height - 4)
    square3_size = random.randint(min(height, width) // 4, min(height, width) // 2)
    square4_x_start = random.randint(width // 2, width - 4)
    square4_y_start = random.randint(height // 2, height - 4)
    square4_size = random.randint(min(height, width) // 4, min(height, width) // 2)

    for y in range(height):
        line = []
        for x in range(width):
            if (
                (
                    x in range(square1_x_start, square1_x_start + square1_size)
                    and y in range(square1_y_start, square1_y_start + square1_size)
                )
                or (
                    x in range(square2_x_start, square2_x_start + square2_size)
                    and y in range(square2_y_start, square2_y_start + square2_size)
                )
                or (
                    x in range(square3_x_start, square3_x_start + square3_size)
                    and y in range(square3_y_start, square3_y_start + square3_size)
                )
                or (
                    x in range(square4_x_start, square4_x_start + square4_size)
                    and y in range(square4_y_start, square4_y_start + square4_size)
                )
            ):
                line.append(" . ")
            else:
                line.append(" # ")
        map.append(line)

    for line in map:
        print("".join(line))


map_generator(30, 20)

# hier ist ein kommentar
# das ist aber ein sehr dürftiger Kommentar
