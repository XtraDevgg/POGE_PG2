# engine_class.py
import pygame
from colorama import Fore
from pygame import *
from luaApi import *
class GameEngine:
    WIN_WIDTH = 800
    WIN_HEIGHT = 640
    DISPLAY = (WIN_WIDTH, WIN_HEIGHT)
    BACKGROUND_COLOR = "#004400"
    TITLE = "POGE"
    SCREEN_D = None
    def __init__(self):
        print(f"{Fore.GREEN}Python Optimized Game Engine v1!{Fore.RESET}")
        self.lua_api = LuaAPI(self)  # Передаем self в LuaAPI

    def start(self):
        pygame.init()
        screen = pygame.display.set_mode(self.DISPLAY)
        self.SCREEN_D = screen
        pygame.display.set_caption(self.TITLE)
        bg = Surface((self.WIN_WIDTH, self.WIN_HEIGHT))
        bg.fill(Color(self.BACKGROUND_COLOR))
        clock = pygame.time.Clock()
        running = True
        
        # Проверяем наличие on_start перед вызовом
        on_start = self.lua_api.lua.globals().on_start
        if on_start:
            try:
                on_start()
            except Exception as e:
                self.error(f"Lua on_start error: {e}")
        else:
            self.error("Lua function 'on_start()' not found!")

        while running:
            dt = clock.tick(60) / 1000
            for e in pygame.event.get():
                if e.type == QUIT:
                    running = False
            screen.blit(bg, (0, 0))
            # Проверяем наличие on_update
            on_update = self.lua_api.lua.globals().on_update
            if on_update:
                try:
                    on_update(dt)
                except Exception as e:
                    self.error(f"Lua on_update error: {e}")
            else:
                self.warn("Lua function 'on_update()' not found!")

            
            pygame.display.update()

    def error(self, text):
        print(f"{Fore.RED}[ERROR] {text}{Fore.RESET}")

    def warn(self, text):
        print(f"{Fore.YELLOW}[WARNING] {text}{Fore.RESET}")