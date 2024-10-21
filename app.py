from flask import Flask, request
from kasa import Discover, Module, Device
import requests
import random
import time
from pygame import mixer

app = Flask(__name__)

@app.route("/flicker")
async def flickerLights():
    dev = await configureKasaLights()
    await dev.turn_on()
    await dev.update()
    light = dev.modules[Module.Light]
    for flicker in [0,50,100,0,100,0,100,0,50,100]:
#        OPTION 1
#        time.sleep(random.uniform(0, 0.4))
        await light.set_brightness(flicker)
        
#        OPTION 2
#        await dev.turn_on()
#        await dev.turn_off()
    await dev.update()
    return "<p>FLICKERED!</p>"

@app.route("/white")
async def turnLightWhite():
    devices = await configureKasaLights()
    for dev in devices.values():
        await dev.turn_on()
        await dev.update()
        light = dev.modules[Module.Light]
        await light.set_hsv(0, 0, 100)
    #    await light.set_color_temp(4500) consider warmer white
        await dev.update()
    return "<p>WHITE!</p>"

@app.route("/red")
async def turnLightRed():
    devices = await configureKasaLights()
    print(devices)
    for dev in devices.values():
        await dev.turn_on()
        await dev.update()
        light = dev.modules[Module.Light]
        await light.set_hsv(0, 100, 100)
        await dev.update()
    return "<p>RED!</p>"
    
async def configureKasaLights() -> [Device]:
    # Why does host change?
#    return await Discover.discover(username="sammyjaynecannillo@gmail.com",password="X35zjpenn123!")
    ip1 = "192.168.0.137"
    light1 = await Discover.discover_single(ip1,username="sammyjaynecannillo@gmail.com",password="X35zjpenn123!")
    
    ip2 = "192.168.0.28"
    light2 = await Discover.discover_single(ip2,username="sammyjaynecannillo@gmail.com",password="X35zjpenn123!")
    return {ip1:light1, ip2:light2}

async def turnPlugOn():
    response = requests.get("https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=c3d1918e-a61b-4a40-a85b-d660418bdd51&token=e09d2de6-c030-48a4-8574-2e9c39e9b6f1&response=json")
    print(response)
    return "<p>PLUG ON!</p>"
    
async def turnPlugOff():
    response = requests.get("https://www.virtualsmarthome.xyz/url_routine_trigger/activate.php?trigger=f4bec4e1-5283-4a1e-a12a-717be60dd5c6&token=be03fc96-1f23-48ef-ba07-16893e96f678&response=json ")
    print(response)
    return "<p>PLUG OFF!</p>"

@app.route("/horror_tease")
async def triggerHorrorTease():
    length = request.args.get("length")

    mixer.init()
    mixer.music.load("long_sweep.wav")

    print(length)
    await turnLightRed() # if this fails, strobe doesn't turn off.
    await turnPlugOn()
    mixer.music.play()
    if length:
        print("123")
        time.sleep(int(length))
    else:
        print("345")
        time.sleep(random.randint(2, 5))
    await turnPlugOff()
    await turnLightWhite()
    return "<p>HORROR TEASED!</p>"
    
@app.route("/reset")
async def reset():
    await turnPlugOff()
    await turnLightWhite()
    return "<p>RESET!</p>"
    
@app.route("/off_chime")
async def triggerOffChime():
    dev = await configureKasaLights()
    await dev.turn_on()
    await dev.update()
    light = dev.modules[Module.Light]
    
    mixer.init()
    mixer.music.load("chime_incorrect.wav")
    mixer.music.play()
    await light.set_brightness(0)
    await dev.update()
    time.sleep(1)
    await light.set_brightness(100)
    await dev.update
    return "<p>HORROR TEASED!</p>"

#https://python-kasa.readthedocs.io/en/latest/guides/light.html FOR TOMORROW

# TODO: Why is dev.modules NIL

# TODO: Consolidate use of Device across app
