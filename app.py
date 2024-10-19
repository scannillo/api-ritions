from flask import Flask
from kasa import Discover, Module

app = Flask(__name__)

@app.route("/white")
async def turnLightWhite():
    dev = await Discover.discover_single("192.168.0.137",username="sammyjaynecannillo@gmail.com",password="X35zjpenn123!")
    await dev.turn_on()
    await dev.update()
    light = dev.modules[Module.Light]
    await light.set_hsv(0, 0, 100)
#    await light.set_color_temp(4500) consider warmer white
    await dev.update()
    return "<p>WHITE!</p>"

@app.route("/red")
async def turnLightRed():
    dev = await Discover.discover_single("192.168.0.137",username="sammyjaynecannillo@gmail.com",password="X35zjpenn123!")
    await dev.turn_on()
    await dev.update()
    light = dev.modules[Module.Light]
    await light.set_hsv(0, 100, 100)
    await dev.update()
    return "<p>RED!</p>"

@app.route("/light_off")
async def turnLightOff():
    dev = await Discover.discover_single("192.168.0.137",username="sammyjaynecannillo@gmail.com",password="X35zjpenn123!")
    await dev.turn_off()
    await dev.update()
    return "<p>LIGHT OFF!</p>"

@app.route("/light_on")
async def turnLightOn():
    dev = await Discover.discover_single("192.168.0.137",username="sammyjaynecannillo@gmail.com",password="X35zjpenn123!")
    await dev.turn_on()
    await dev.update()
    print(dev.alias)
    print("Hello, world!")
    return "<p>LIGHT ON!</p>"

#https://python-kasa.readthedocs.io/en/latest/guides/light.html FOR TOMORROW

# TODO: Why is dev.modules NIL
