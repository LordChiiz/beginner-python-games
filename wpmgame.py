# Want to know how fast you can type? Try this simple python game :)

import curses
from curses import wrapper
import time
import random

def start_screen(stdscr):
    stdscr.clear()
    stdscr.addstr("Welcome to the a Typing speed test",)
    stdscr.addstr("\nPress any key to start",)
    stdscr.refresh()
    stdscr.getkey()

def load_text():
    with open("text.txt", "r")as f:
        lines = f.readlines()
        return random.choice(lines).strip() #strip remove \n


def display_wrtext(stdscr, target, current, wpm = 0):
    stdscr.addstr(target)
    stdscr.addstr(1, 0, f"WPM:{wpm}")

    for i, char in enumerate(current):
        correct_char = target[i]
        color = curses.color_pair(1)
        if char != correct_char:
            color = curses.color_pair(2)
        stdscr.addstr(0, i, char, color)
    



def wpm_text(stdscr):
    typ_text = load_text
    user_text = []
    wpm = 0
    start_time = time.time()
    stdscr.nodelay(True)

    while True:
        time_elapsed = time.time() - start_time
        wpm = round((len(user_text)/(time_elapsed/60))/5)

        stdscr.clear()
        display_wrtext(stdscr, typ_text, user_text, wpm)
        stdscr.refresh()

        if "".join(user_text) == typ_text:
            stdscr.nodelay(False)
            break

        try:
            key = stdscr.getkey()
        except:
            continue

        if ord(key) == 27:
            break
        if key in ("KEY_BACKSPACE", "\b", "\x7f"):
            if len(user_text) > 0:
                user_text.pop()

        elif len(user_text) < len(typ_text):
            user_text.append(key)
     

    


def main(stdscr):
    curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
    
    start_screen(stdscr)

    while True:
        wpm_text(stdscr)

        stdscr.addstr(2,0, 'You completed the test. Press any key to play again. Press escape to quit.' )
        key = stdscr.getkey()

        if ord(key) == 27:
            break

wrapper(main)