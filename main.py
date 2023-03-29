from game import Game
from menu import Menu
from start_screen import start_screen
import asyncio
import time

async def main():
    await start_screen()
    menu = Menu()  
    while True:
        difficulty = await menu.main()
        game = Game(difficulty)
        await game.main()
        time.sleep(1)
        await asyncio.sleep(0)

if __name__ == "__main__":
    asyncio.run(main())