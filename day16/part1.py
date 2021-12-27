
def hex2bin(c):
    mapping = {
        "0": "0000",
        "1": "0001",
        "2": "0010",
        "3": "0011",
        "4": "0100",
        "5": "0101",
        "6": "0110",
        "7": "0111",
        "8": "1000",
        "9": "1001",
        "A": "1010",
        "B": "1011",
        "C": "1100",
        "D": "1101",
        "E": "1110",
        "F": "1111",
    }

    return mapping[c]


def parseinput(file):

    with open(file, "r") as f:
        hexline = f.readline()

    return "".join([hex2bin(c) for c in hexline])


def parsepacket(binary):

    # otherwise there are more packets to process
    version = int(binary[0:3], 2)
    typeid = int(binary[3:6], 2)

    versionsum = version

    if typeid == 4:
        # parse literal value
        number, i = "", 0
        while True:
            number += binary[7 + 5 * i: 11 + 5 * i]
            if binary[6 + 5 * i] == "0":
                break

            # if not last subgroup, keep parsing
            i += 1

        # convert number to integer and calculate number of bits used
        packetvalue = int(number, 2)
        bitsused = 6 + 5 * (i + 1)
    else:
        # parse id
        lengthid = int(binary[6], 2)

        # depending on the id, get the limiting value and where the subpackets will start
        if lengthid == 0:
            substart = 22
            subLength = int(binary[7:22], 2)
            subCount = None
        else:
            substart = 18
            subCount = int(binary[7:18], 2)
            subLength = None

        # keep parsing subpackets until limiting value is reached
        subpacketValues = []
        while True:
            # check if limiting value is reached
            if (subLength is not None and subLength == 0) or subCount == 0:
                bitsused = substart
                break

            # parse the subpacket at that position
            packetvalue, subVersionSum, subBitsUsed = parsepacket(binary[substart:])

            # update values of this overall packet
            subpacketValues.append(packetvalue)
            versionsum += subVersionSum
            substart += subBitsUsed

            # update whatever length is being limited
            if subLength is not None:
                subLength -= subBitsUsed
            else:
                subCount -= 1

    return packetvalue, versionsum, bitsused


def main():
    binary = parseinput("hardinput.txt")

    _, versionsum, _ = parsepacket(binary)

    return versionsum


result = main()
print(result)
