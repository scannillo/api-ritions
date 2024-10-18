from flask import Flask
from kasa import Discover, Module

app = Flask(__name__)

@app.route("/light_off")
async def hello_world():
    someThing()
    await lights()
    print("Hello, world!")
    return "<p>Hello, World!</p>"


@app.route("/light_on")
async def light_on2():
    someThing()
    dev = await Discover.discover_single("192.168.0.137",username="sammyjaynecannillo@gmail.com",password="X35zjpenn123!")
    await dev.turn_on()
    await dev.update()
    print(dev.alias)
    print("Hello, world!")
    return "<p>Hello, World!</p>"
    
@app.route("/light_red")
async def hello_red():
    dev = await Discover.discover_single("192.168.0.137",username="sammyjaynecannillo@gmail.com",password="X35zjpenn123!")
    print(dev.modules)
#    await light.set_color_temp(3000)
    await dev.update()
    print(dev.alias)
    return "<p>Hello, RED WORLD!</p>"
    
def someThing():
    print("More things")
    
async def lights():
    dev = await Discover.discover_single("192.168.0.137",username="sammyjaynecannillo@gmail.com",password="X35zjpenn123!")
    await dev.turn_off()
    await dev.update()
    print(dev.alias)

#https://python-kasa.readthedocs.io/en/latest/guides/light.html FOR TOMORROW
