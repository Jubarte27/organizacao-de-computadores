import re
def main():
    pattern = re.compile(r"(^[\da-z](?=[ \n])|(?<= )[\da-z]+(?=[ \n])|(?<= )[\da-z]+$|^[\da-z]+$)|((\b\d+\b)\*(\b[\da-z]+\b))")
    with open("mem") as mem_file:
        mem_file.readline()
        for line in mem_file.readlines():
            for cell in pattern.findall(line):
                if cell[0] != "":
                    print(f"{int(cell[0], 16):08b}", end=" ")
                elif cell[1] != "":
                    print(cell[1], end=" ") 
            print()


if __name__ == "__main__":
    main()