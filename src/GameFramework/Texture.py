#from GameFramework import Singleton
from GameFramework import pygame
from GameFramework import os


class TextureMNG :
    texture_list = {}

    @classmethod
    def TextureLoad(cls, path : str) -> pygame.Surface | None :
        if path in cls.texture_list :
            return cls.texture_list[path]

        if os.path.exists(path) :
            print(f"IMG LOAD : {path}")
            texture = pygame.image.load(path)
            cls.texture_list[path] = texture
            return texture
        else :
            print(f"IMG FAIL!!! : {path}")
            return None