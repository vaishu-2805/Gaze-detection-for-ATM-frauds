import pygame

pygame.mixer.init()

def play_alert_sound():
    try:
        sound = pygame.mixer.Sound("assets/alert.wav")
        sound.play()
    except Exception as e:
        print("[ERROR] Could not play alert sound:", e)
