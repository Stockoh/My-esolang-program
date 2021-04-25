import sys


def compilebrainfuck(string):
    def brainfuck(*args):
        memory = [0] * 30000
        pointer = 0
        step = 0
        inputpointer = 0
        if len(args) == 1:  # To be able to do : brainfuck("Hello")
            args = args[0]  # instead of brainfuck("H","e","l","l","o")

        while step < len(string):
            if string[step] == ">":
                pointer += 1

            if string[step] == "<":
                pointer -= 1

            if string[step] == "+":
                memory[pointer] += 1
                if memory[pointer] == 256:
                    memory[pointer] = 0

            if string[step] == "-":
                memory[pointer] -= 1
                if memory[pointer] == -1:
                    memory[pointer] = 255

            if string[step] == ".":
                print(chr(memory[pointer]), end="")

            if string[step] == ",":
                try:
                    memory[pointer] = ord(args[inputpointer])
                except IndexError:
                    memory[pointer] = 0
                inputpointer += 1

            if string[step] == "[":
                if not memory[pointer]:
                    level = 0
                    for i in range(step + 1, len(string)):
                        if level == 0 and string[i] == "]":
                            step = i
                            break
                        if string[i] == "[":
                            level += 1
                        if string[i] == "]":
                            level -= 1

            elif string[step] == "]":
                if memory[pointer]:
                    level = 0
                    for i in range(step - 1, -1, -1):
                        if level == 0 and string[i] == "[":
                            step = i
                            break
                        if string[i] == "[":
                            level += 1
                        if string[i] == "]":
                            level -= 1
            step += 1

    return brainfuck


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("usage: brainfuck.py [-c cmd | file path] [-i input]")
        sys.exit()

    if sys.argv[1] == "-c":  # Cmd Mode
        if len(sys.argv) == 2 or sys.argv[2] == "-i:
            print("There is not programme.")
            print("You must add a programme just after '-c'")
            sys.exit()
        function = compilebrainfuck(sys.argv[2])
        input = ""
        if len(sys.argv) == 5:
            if sys.argv[3] == "-i":
                input = sys.argv[4]
        function(input)

    else:                    # File Mode
        try:
            with open(sys.argv[1], "r") as file:
                function = compilebrainfuck(file.read())
                input = ""
                if len(sys.argv) > 2:
                    if sys.argv[2] == "-i":
                        input = sys.argv[3]
                function(input)
        except FileNotFoundError as a:
            print("FileNotFoundError:", a)
