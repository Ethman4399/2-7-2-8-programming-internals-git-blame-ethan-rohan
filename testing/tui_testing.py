import curses
def main(stdscr):
    stdscr.clear() 
    stdscr.addstr(0,0, "Hello, I am using Curses!")
    stdscr.refresh()
    stdscr.getch()

if __name__ == "__main__":
    curses.wrapper(main)