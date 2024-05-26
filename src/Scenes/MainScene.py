from GameFramework import Vec2, Scene, Sprite

class MainScene(Scene) :

    @classmethod
    def Setup(cls) :
        print("Setup")
        testimg = Sprite("assets/images/greenslime.png",Vec2(255,255))        


    @classmethod
    def Update(cls) :
        pass

    @classmethod
    def Exit(cls) :
        print("Exit")
