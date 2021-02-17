from src.game import Game

def main():
    game = Game(scale=2)
    while game.running:
        game.on_event()
        game.on_update()
        game.on_render()

    game.close()

if __name__ == '__main__':
    main()
