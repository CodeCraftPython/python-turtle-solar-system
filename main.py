import turtle
import math
from PIL import Image
import json

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Solar System Animation")

turtle.setworldcoordinates(-350, -350, 350, 350)

sun_image = Image.open("Sun.gif")
resized_sun_image = sun_image.resize((60, 60))
resized_sun_image_filename = "sun_resized.gif"
resized_sun_image.save(resized_sun_image_filename, "GIF")
screen.register_shape(resized_sun_image_filename)

sun = turtle.Turtle()
sun.shape(resized_sun_image_filename)
sun.penup()

with open('json/planet_configs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    planet_images = data.get('planet_imgs')
    planets = data.get('configs')

resized_images = {}

for planet_name, image_filename in planet_images.items():
    original_image = Image.open(image_filename)
    if planet_name == 'Mercury' or planet_name == 'Venus':
        resized_image = original_image.resize((45, 30))
    elif planet_name == 'Mars':
        resized_image = original_image.resize((30, 30))
    else:
        resized_image = original_image.resize((40, 40))
    resized_images[planet_name] = resized_image
    resized_image_filename = f"{planet_name}_resized.gif"
    resized_image.save(resized_image_filename, "GIF")
    screen.register_shape(resized_image_filename)


for planet_name, planet_info in planets.items():
    planet_info["turtle"] = turtle.Turtle()
    planet_info["turtle"].shape(f"{planet_name}_resized.gif")
    planet_info["turtle"].color(planet_info["color"])
    planet_info["turtle"].penup()
    planet_info["turtle"].goto(planet_info["distance"], 1)
    planet_info["turtle"].pendown()
    planet_info["turtle"].pencolor("gray")
    planet_info["turtle"].write(planet_name)

while True:
    for planet_name, planet_info in planets.items():
        planet_turtle = planet_info["turtle"]
        distance = planet_info["distance"]
        angle = planet_info["angle"]
        size = planet_info["size"]
        x = distance * math.cos(math.radians(angle))
        y = distance * math.sin(math.radians(angle))
        planet_turtle.goto(x, y)
        planet_info["angle"] += planet_info["speed"]
        planet_turtle.goto(x, y)
        planet_turtle.shapesize(size)
