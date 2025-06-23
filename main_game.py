import curses
import time
import sys
from field import Field
from snake import Snake


def main(screen):
    #configure screen
    screen.timeout(0)

    field = Field(10)
    snake = Snake("Dan")
    snake.set_field(field)

    while True:
        ch = screen.getch()
        if ch != -1:
            snake.set_direction(ch)

        snake.move()
        field.render(screen)
        screen.refresh()
        time.sleep(.4)

if __name__ == '__main__':
    curses.wrapper(main)