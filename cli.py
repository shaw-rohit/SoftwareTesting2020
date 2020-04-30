from hangman.__main__ import main
import sys

try:
    if __name__ == '__main__':
        main()

except KeyboardInterrupt:
    sys.exit(0)

except EOFError:
    sys.exit(0)
