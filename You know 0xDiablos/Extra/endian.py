import sys

def endian(endian, string):
    res = ''

    if endian:
        for i in range(0, len(string), 2):
            res += "\\x" + string[i:i + 2]
    else:
        for i in range(0, len(string), 2):
            res = "\\x" + string[i:i + 2] + res
    return res

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python endian.py <endian> <string>")
        sys.exit(1)

    endian_option = int(sys.argv[1])
    input_string = sys.argv[2]

    if endian_option != 0 and endian_option != 1:
        print("Endian option must be 0 or 1")
        sys.exit(1)

    result = endian(endian_option, input_string)
    print(result)

