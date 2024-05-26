#슬프게도 버려진 ㅠ
"""class Singleton(type) :
    __instance = {}
    
    def __call__(cls, *args, **kwargs) :
        if cls not in cls.isinstance :
            cls.__instance[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        
        return cls.__instance[cls]
""" 