# Solar System Animation

This Python script uses the Turtle graphics library to create an animated representation of the solar system. Planets orbit around the sun, and their positions are calculated based on their distances, angles, and speeds.

## Setting Up the Environment
To run the solar system animation script, it's recommended to set up a virtual environment to isolate the dependencies. Here's how you can do it:

1. Create a virtual environment:
```bash
python -m venv venv
```

2. Activate the virtual environment:
```bash
# On Windows:
python -m venv venv

# On macOS and Linux:
source venv/bin/activate
```
## Installing Dependencies
Once your virtual environment is active, you can install the required dependencies using the **requirements.txt** file provided:
```shell
pip install -r requirements.txt
```

## Code Explanation

### Importing Required Libraries
```python
import turtle
import math
from PIL import Image
import json
```

* **turtle**: Provides a graphics window and turtle graphics for drawing.
* **math**: Used for mathematical calculations.
* **PIL.Image**: Part of the Pillow library, used for image manipulation.
* **json**: Used to read planet configuration data from a JSON file.

### Setting Up the Graphics Window
```python
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=800)
screen.title("Solar System Animation")
turtle.setworldcoordinates(-350, -350, 350, 350)
```

* Creates a turtle graphics window with a black background and a size of 800x800 pixels.
* Sets up the title of the window to "Solar System Animation".
* Defines the coordinate system with a range from -350 to 350 in both x and y directions.

### Loading and Registering Sun Image
```python
sun_image = Image.open("Sun.gif")
resized_sun_image = sun_image.resize((60, 60))
resized_sun_image_filename = "sun_resized.gif"
resized_sun_image.save(resized_sun_image_filename, "GIF")
screen.register_shape(resized_sun_image_filename)
```

* Loads an image of the sun from the file "Sun.gif".
* Resizes the sun image to 60x60 pixels.
* Saves the resized sun image as "sun_resized.gif".
* Registers the resized sun image as a custom turtle shape.

### Loading Planet Configurations from JSON
```python
with open('json/planet_configs.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    planet_images = data.get('planet_imgs')
    planets = data.get('configs')
```

* Opens the JSON file "planet_configs.json" to read planet configuration data.
* Parses the JSON data to extract planet images and configurations.

### Resizing and Registering Planet Images

```python
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
```

* Loops through planet images and resizes them based on specific criteria.
* Saves the resized planet images with appropriate filenames.
* Registers each resized planet image as a custom turtle shape

### Creating and Initializing Planet Turtles

```python
for planet_name, planet_info in planets.items():
    planet_info["turtle"] = turtle.Turtle()
    planet_info["turtle"].shape(f"{planet_name}_resized.gif")
    planet_info["turtle"].color(planet_info["color"])
    planet_info["turtle"].penup()
    planet_info["turtle"].goto(planet_info["distance"], 1)
    planet_info["turtle"].pendown()
    planet_info["turtle"].pencolor("gray")
    planet_info["turtle"].write(planet_name)
```

* Creates a turtle for each planet and sets its shape, color, and initial position.
* The planet's distance from the sun is determined by the configuration data.
* The planet's name is displayed next to its initial position.

### Animating Planet Orbits
```python
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
```

* Enters an infinite loop to continuously update the positions of planets.
* Calculates the new position of each planet based on its distance, angle, and speed.
* Updates the planet's angle for the next iteration to simulate orbiting.
* Updates the planet's position and size in the graphics window.


## Contributing

Contributions to this solar system animation project are welcome! If you'd like to contribute, follow these steps:

1. Fork this repository.

2. Clone your forked repository to your local machine:

```bash
git clone https://github.com/CodeCraftPython/python-turtle-solar-system.git
```

#### Create a new branch for your feature or bug fix:
```bash
git checkout -b feature/your-feature-name
```

* Make your changes to the code.
* Test your changes thoroughly to ensure they work as expected. 

##### Commit your changes:
```bash
git commit -m "Add your meaningful commit message here"
```

##### Push your changes to your forked repository:
```bash
git push origin feature/your-feature-name
```

* Create a pull request from your forked repository's branch to the original repository's main branch.

* Provide a clear and descriptive title for your pull request, along with a detailed description of the changes you've made.

* Submit the pull request, and your changes will be reviewed by the maintainers.