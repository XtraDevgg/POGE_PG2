# luaApi.py
from lupa import LuaRuntime
from Entity import *
import pygame
import os

class LuaAPI:
    def __init__(self, engine):  # Принимаем engine из GameEngine
        self.lua = LuaRuntime(unpack_returned_tuples=True)
        self.engine = engine
        
        lua_globals = self.lua.globals()
        # Экспортируем движок и утилиты

        lua_globals.FRAMEWORK = pygame
        lua_globals.POGE = self.engine
        lua_globals.Entity = Entity
        lua_globals.Vector2 = Vector2
        lua_globals.POGE_SCREEN = self.engine.SCREEN_D
        # Экспорт функций ввода
        def py_get_input(key):
            pygame.event.pump()  # Обновляем состояние клавиатуры
            return pygame.key.get_pressed()[key]
        lua_globals.py_get_input = py_get_input
        lua_globals.sprite = pygame.sprite.Sprite
        # Экспорт констант Pygame
        lua_globals.py = {
    "KEY_SPACE": pygame.K_SPACE,
    "KEY_W": pygame.K_w,
    "KEY_S": pygame.K_s,
    "KEY_A": pygame.K_a,
    "KEY_D": pygame.K_d,
    "KEY_ESC": pygame.K_ESCAPE
}

    def execute_script(self, script_path):
        """Загружает и выполняет Lua-скрипт"""
        try:
            if not os.path.exists(script_path):
                self.engine.error(f"Script not found: {script_path}")
                return
            
            with open(script_path, "r", encoding="utf-8") as f:
                code = f.read()
            
            self.lua.execute(code)
            print(f"Скрипт {script_path} успешно загружен")
        except Exception as e:
            self.engine.error(f"Ошибка выполнения скрипта: {str(e)}")