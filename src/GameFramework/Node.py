from GameFramework import Renderer, Vec2, pygame
from abc import ABC, abstractmethod


class Node(ABC) :
    def __init__(self) -> None :
        self.position : Vec2 = Vec2(0, 0)
        self.scale : Vec2 = Vec2(1, 1)
        self.collision_scale : Vec2 = Vec2(1, 1)
        self.pivot : Vec2 = Vec2(0.5, 0.5)

        self.rotation : float = 0

        self.visible : bool = true
        #self.isUI : bool = false

        self.layer : int = 0

        self.color = pygame.Color(255,255,255,255)
        self.rect = pygame.Rect(0,0,0,0)
        Renderer.AddNode(self)

    @abstractmethod
    def Update(self) : pass

    @abstractmethod
    def Render(self) : pass