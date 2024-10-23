from flask import Flask, request
from kasa import Discover, Module, Device
import requests
import random
import time
from pygame import mixer
import playsound

app = Flask(__name__)

@app.route("/white")
async def turnLightWhite():
    devices = await configureKasaLights()
    for dev in devices.values():
        await dev.turn_on()
        await dev.update()
        light = dev.modules[Module.Light]
        await light.set_color_temp(2700)
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
    
async def turnLightOff():
    devices = await configureKasaLights()
    print(devices)
    for dev in devices.values():
        await dev.turn_off()
        await dev.update()
    return "<p>LIGHTS OFF!</p>"
    
async def configureKasaLights() -> [Device]:
#    return await Discover.discover(username="sammyjaynecannillo@gmail.com",password="X35zjpenn123!")
    ip1 = "192.168.0.28"
    light1 = await Discover.discover_single(ip1,username="sammyjaynecannillo@gmail.com",password="X35zjpenn123!")
    
    ip2 = "192.168.0.136"
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
    
shortAudioClips = {
    "audio/horns.mp3": 5,
    "audio/longsweep.wav": 5,
    "audio/scream_1.wav": 4,
    "audio/stab.mp3": 5,
    "audio/string_tension.mp3": 7
}

longAudioClips = {
    "audio/hearbeat.mp3": 22,
    "audio/jumpscare.mp3": 19,
    "audio/psycho.mp3": 12,
    "audio/spotted.wav": 12
}

@app.route("/horror_tease")
async def triggerHorrorTease():
    allAudioClips = shortAudioClips | longAudioClips
    randomClipTitle = random.choice(list(allAudioClips.keys()))

    mixer.init()
    mixer.music.load(randomClipTitle)

    await turnLightRed()
    mixer.music.play()
    await turnPlugOn()
    time.sleep(allAudioClips[randomClipTitle])
    await turnPlugOff()
    await turnLightWhite()
    return "<p>HORROR TEASED!</p>"
    
@app.route("/murder_tease")
async def triggerMurderTease():
    randomClipTitle = random.choice(list(shortAudioClips.keys()))
    
    mixer.init()
    mixer.music.load(randomClipTitle)

    await turnPlugOn()
    mixer.music.play()

    await turnLightOff()

    time.sleep(shortAudioClips[randomClipTitle])
    await turnPlugOff()
    await turnLightWhite()
    return "<p>MURDER TEASED!</p>"
    
@app.route("/baby_tease")
async def triggerBabyTease():
    randomClipTitle = random.choice(list(longAudioClips.keys()))

    mixer.init()
    mixer.music.load(randomClipTitle)

    await turnLightRed()
    mixer.music.play()
    time.sleep(longAudioClips[randomClipTitle])
    await turnLightWhite()
    return "<p>HORROR TEASED!</p>"
    
@app.route("/reset")
async def reset():
    await turnPlugOff()
    await turnLightWhite()
    return "<p>RESET!</p>"

app.run(host='192.168.0.55', port=5000)

# Public IP: Command `ifconfig`: en0 > inet
