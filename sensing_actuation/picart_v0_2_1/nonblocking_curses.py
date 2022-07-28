import curses
import datetime
import time

stdscr = curses.initscr()
curses.noecho()
stdscr.nodelay(1) # set getch() non-blocking

stdscr.addstr(0,0,"Press \"p\" to show count, \"q\" to exit...")
line = 1
i = 0
try:
    while 1:
        c = stdscr.getch()
        if c == ord('p'):
            stdscr.addstr(line,0,"Some text here")
            line += 1
        #elif c == ord('q'): break

        elif c == ord('q'):  # x1b is ESC
            print(i)
            time.sleep(2)
            break
        i += 1

finally:
    curses.endwin()
