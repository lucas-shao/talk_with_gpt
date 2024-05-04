import pygame


def play_audio(filename):
    print("Playing audio...")
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy() == True:
        continue


if __name__ == "__main__":
    play_audio("answer.mp3")
