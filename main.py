import os
try:
    import pygame
except:
    os.system("pip install pygame")
    import pygame
try:
    import lupa
except:
    os.system("pip install lupa")
    import lupa
try:
    import pystyle
except:
    os.system("pip install pystyle")
    import pystyle
from pystyle import Colors, Colorate
from pygame import *
from lupa import LuaRuntime



from engine_class import GameEngine

if __name__ == "__main__":
    engine = GameEngine()
    engine.lua_api.execute_script("game_scripts/game_script.lua")  # Укажите правильный путь
    engine.start()