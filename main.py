import src
from pygame import display
        
def main():
    game = src.GameHandler()
    game.start_game()
    
if __name__ == "__main__":
    display.set_mode(src.GameHandler.RESOLUTION, vsync=1)
    main()