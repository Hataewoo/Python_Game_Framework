from GameFramework import pygame

class Time :
    scale = 1
    clock = None
    frame_time_ms = 0

    @classmethod
    def GetDeltaTime(cls) :
        """초 단위 시간 deltaTime(frame과 frame 사이의 시간) 반환"""
        if cls.clock == None : return 0
        frame_time_s = cls.frame_time_ms / 1000.0 * cls.scale  # 초 단위
        return frame_time_s

    @classmethod
    def SetTimeSpeed(cls, speed : float) :
        cls.scale = speed