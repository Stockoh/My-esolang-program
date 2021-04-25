import sys


def compiledeadfish(string, shell=False):

    def Deadfish():
        if shell:
            global acc
        else:
            acc = 0
        for command in string:
            if command == "i":  # Increment
                acc += 1
            if command == "d":  # Decrement
                acc -= 1
            if command == "s":  # Square
                acc *= acc
            if command == "o":  # Ouput
                print(acc, end="\n" * shell)
            if acc == -1 or acc == 256:
                acc = 0

    return Deadfish


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("usage : deadfish.py [-c cmd | file | -s]")

    if sys.argv[1] == "-c":    # Cmd Mode
        if len(sys.argv) == 2:
            print("There is not programme.")
            print("You must add a programme just after '-c'")
            sys.exit()
        function = compiledeadfish(sys.argv[2])
        function()

    if sys.argv[1] == "-s":    # Shell Mode
        print("(Stop with Ctrl-C)")
        acc = 0
        try:
            while True:
                function = input(">>")
                function = compiledeadfish(function, shell=True)
                function()
        except KeyboardInterrupt:
            pass

    else:                      # File mode
        with open(sys.argv[1], "r") as file:
            function = compiledeadfish(file.read())
            function()
