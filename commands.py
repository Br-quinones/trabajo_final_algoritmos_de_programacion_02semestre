import sys
import time

def clean_buffer():
    if sys.platform == 'win32':
        import msvcrt
        while msvcrt.kbhit():
            msvcrt.getch()
    else:
        import termios
        termios.tcflush(sys.stdin, termios.TCIFLUSH)

def task_complete():
    print("Complete!")
    time.sleep(0.35)