'''Packages & Debugging
1.python packages & core package 
2.package manager & external package
3.debugging
'''

from PIL import Image
import math
import turtle
print("==== python packages & core package  ====")
# python packages/modules : core, file and external
# core packages > https://docs.python.org/3/library

# core packages
# t = turtle.Turtle()
# t.shape("turtle")
# t.speed(2)
# t.circle(150)

# turtle.done()


print("========  pizza chizamiz =====")

# # Setup screen
# screen = turtle.Screen()
# screen.title("Python Turtle Pizza")
# screen.bgcolor("#2b2b2b")
# screen.setup(width=700, height=700)

# t = turtle.Turtle()
# t.speed(0)
# t.hideturtle()


# def draw_circle(radius, color, border_color=None):
#     """Draws a filled circle centered at (0, 0)."""
#     t.penup()
#     t.goto(0, -radius)
#     t.pendown()
#     t.color(border_color if border_color else color, color)
#     t.begin_fill()
#     t.circle(radius)
#     t.end_fill()


# def draw_crust_and_cheese():
#     """Draws the main base of the pizza."""
#     # Outer Crust
#     draw_circle(250, "#D27D2D", "#8B4513")
#     # Inner Crust (Baking line)
#     draw_circle(230, "#E68A2E")
#     # Cheese Layer
#     draw_circle(215, "#FFD700", "#FFC107")


# def draw_pepperoni(x, y, radius=22):
#     """Draws a pepperoni slice at a specific (x, y) coordinate."""
#     t.penup()
#     t.goto(x, y - radius)
#     t.pendown()
#     t.color("#990000", "#C0392B")
#     t.begin_fill()
#     t.circle(radius)
#     t.end_fill()

#     # Pepperoni highlight/texture
#     t.penup()
#     t.goto(x - 5, y + 2)
#     t.pendown()
#     t.color("#E74C3C")
#     t.dot(6)


# def draw_slice_lines():
#     """Draws cut lines across the pizza."""
#     t.color("#D68910")
#     t.width(3)
#     num_slices = 8
#     for i in range(num_slices):
#         angle = i * (360 / num_slices)
#         rad = math.radians(angle)
#         x = 215 * math.cos(rad)
#         y = 215 * math.sin(rad)

#         t.penup()
#         t.goto(0, 0)
#         t.pendown()
#         t.goto(x, y)

# # --- Assemble the Pizza ---


# # 1. Base
# draw_crust_and_cheese()

# # 2. Slice Cuts
# draw_slice_lines()

# # 3. Pepperoni Placement (Inner ring and outer ring)
# pepperoni_positions = [
#     # Center
#     (0, 0),
#     # Inner Ring
#     (0, 90), (75, 45), (90, 0), (75, -45),
#     (0, -90), (-75, -45), (-90, 0), (-75, 45),
#     # Outer Ring
#     (0, 155), (110, 110), (155, 0), (110, -110),
#     (0, -155), (-110, -110), (-155, 0), (-110, 110)
# ]

# for pos in pepperoni_positions:
#     draw_pepperoni(pos[0], pos[1])

# # Keep the window open
# screen.mainloop()

print("======= pizza shu yergacha ")


my_life = open("material/message.txt", "r")
try:
    content = my_life.read()
    print("content:", content)
finally:
    my_life.close()

    # with
with open("material/message.txt", "r") as your_file:
    your_content = your_file.read()
    print("your_content:", your_content)

print("done")


print("==== package manager and external package ====")
'''Package Manager
Python > pip, pipenv
NodeJs > npm, yarn
PHP > composer
MacOS > brew
'''
# external package: https://pypi.org/

# with Image.open("material/nature.png") as img_obj:
#     resized_img = img_obj.resize((200, 200))
#     resized_img.show()
#     resized_img.save("material/sample.png")
