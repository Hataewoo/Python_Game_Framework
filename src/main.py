from GameFramework import Director, Renderer, Mouse, pygame, Time
from Scenes import MainScene

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_COLOR = (255, 45, 255)

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

        elif event.type == pygame.QUIT:
            Exit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                Exit()
                running = False
        
def Update() :
    Time.frame_time_ms = Time.clock.tick(60)
    Director.ScreenFill(SCREEN_COLOR)
    Director.DirectorUpdate()

def Render() :
    Renderer.Render()

    pygame.display.flip()

def Exit() :
    Renderer.ClearNode()
    pygame.quit()


running = True
if __name__ == "__main__" :
    Setup()

    while running :
        Event()
        Update()
        Render()
    
    Exit()

