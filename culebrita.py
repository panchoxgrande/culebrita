import curses
import random

def main(stdscr):
    curses.curs_set(0)
    sh, sw = stdscr.getmaxyx()
    win = curses.newwin(sh, sw, 0, 0)
    win.keypad(1)
    win.timeout(100)

    snake = [(sh//2, sw//4 + i) for i in range(3)][::-1]
    direction = curses.KEY_RIGHT
    food = (random.randint(1, sh - 2), random.randint(1, sw - 2))
    win.addch(*food, '🍎')

    while True:
        next_key = win.getch()
        direction = direction if next_key == -1 else next_key

        head_y, head_x = snake[0]
        if direction == curses.KEY_DOWN:
            head_y += 1
        elif direction == curses.KEY_UP:
            head_y -= 1
        elif direction == curses.KEY_LEFT:
            head_x -= 1
        elif direction == curses.KEY_RIGHT:
            head_x += 1

        new_head = (head_y, head_x)

        if (
            new_head in snake or
            head_y in [0, sh] or
            head_x in [0, sw]
        ):
            msg = "💀 Game Over! Presiona cualquier tecla para salir."
            win.addstr(sh//2, sw//2 - len(msg)//2, msg)
            win.nodelay(0)
            win.getch()
            break

        snake.insert(0, new_head)
        if new_head == food:
            food = (random.randint(1, sh - 2), random.randint(1, sw - 2))
            win.addch(*food, '🍎')
        else:
            tail = snake.pop()
            win.addch(*tail, ' ')

        win.addch(*new_head, '🟩')

curses.wrapper(main)
