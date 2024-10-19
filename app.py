from flask import Flask
from kasa import Discover, Module, Device
import requests

app = Flask(__name__)

@app.route("/white")
async def turnLightWhite():
    dev = await configureKasaLights()
    await dev.turn_on()
    await dev.update()
    light = dev.modules[Module.Light]
    await light.set_hsv(0, 0, 100)
#    await light.set_color_temp(4500) consider warmer white
    await dev.update()
    return "<p>WHITE!</p>"

@app.route("/red")
async def turnLightRed():
    dev = await configureKasaLights()
    await dev.turn_on()
    await dev.update()
    light = dev.modules[Module.Light]
    await light.set_hsv(0, 100, 100)
    await dev.update()
    return "<p>RED!</p>"

@app.route("/light_off")
async def turnLightOff():
    dev = await configureKasaLights()
    await dev.turn_off()
    await dev.update()
    return "<p>LIGHT OFF!</p>"

@app.route("/light_on")
async def turnLightOn():
    dev = await configureKasaLights()
    await dev.turn_on()
    await dev.update()
    print(dev.alias)
    return "<p>LIGHT ON!</p>"
    
async def configureKasaLights() -> Device:
    return await Discover.discover_single("192.168.0.137",username="sammyjaynecannillo@gmail.com",password="X35zjpenn123!")

@app.route("/plug_on")
async def turnPlugOn():
    response = requests.get("https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=c3d1918e-a61b-4a40-a85b-d660418bdd51&token=e09d2de6-c030-48a4-8574-2e9c39e9b6f1&response=json")
    print(response)
    return "<p>PLUG ON!</p>"
    
@app.route("/plug_off")
async def turnPlugOff():
    response = requests.get("https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=f4bec4e1-5283-4a1e-a12a-717be60dd5c6&token=be03fc96-1f23-48ef-ba07-16893e96f678&response=json ")
    print(response)
    return "<p>PLUG OFF!</p>"

#https://python-kasa.readthedocs.io/en/latest/guides/light.html FOR TOMORROW

# TODO: Why is dev.modules NIL
