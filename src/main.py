from GameFramework import Director, Renderer, Mouse, pygame, Time
from Scenes import MainScene

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def Setup() :
    pygame.init()
    Director.SetScreenSize(SCREEN_WIDTH, SCREEN_HEIGHT)
    Director.DirectorInit("Game Tic-Tak-Toe")
    Time.clock = pygame.time.Clock()

    Director.ChangeScene(MainScene)


def Event() :
    for event in pygame.event.get() :
        if event.type == pygame.MOUSEBUTTONDOWN :
            Mouse.n_click = 1

        elif event.type == pygame.MOUSEBUTTONUP :
            Mouse.n_click = 3
        
def Update() :
    Time.frame_time_ms = Time.clock.tick(60)
    Director.DirectorUpdate()

def Render() :
    Renderer.Render()

def Exit() :
    pass


if __name__ == "__main__" :
    Setup()

    while True :
        Event()
        Render()
        Update()
    
    Exit()

