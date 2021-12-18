import utils

def get_inpt():
    inpt = utils.read_input("16")
    decode = {
        "0" : "0000",
        "1" : "0001",
        "2" : "0010",
        "3" : "0011",
        "4" : "0100",
        "5" : "0101",
        "6" : "0110",
        "7" : "0111",
        "8" : "1000",
        "9" : "1001",
        "A" : "1010",
        "B" : "1011",
        "C" : "1100",
        "D" : "1101",
        "E" : "1110",
        "F" : "1111",
    }
    inpt_binary = "".join([decode[x] for x in inpt[0]])
    return inpt_binary

version_sum = 0

def parse(packet):
    if packet == "":
        return 0
    global version_sum
    version_sum += int(packet[:3],2)
    type_id = int(packet[3:6], 2)
    packet = packet[6:]
    if type_id == 4:
        return parse_literal(packet)
    else:
        contents, packet = parse_operator(packet)
        if type_id == 0:
            return sum(contents), packet
        elif type_id == 1:
            prod = 1
            for x in contents:
                prod *= x
            return prod, packet
        elif type_id == 2:
            return min(contents), packet
        elif type_id == 3:
            return max(contents), packet
        elif type_id == 5:
            return contents[0]>contents[1], packet
        elif type_id == 6:
            return contents[0]<contents[1], packet
        elif type_id == 7:
            return contents[0]==contents[1], packet
        

def parse_literal(packet):
    value = []
    while True:
        bits = packet[:5]
        packet = packet[5:]
        value.append(bits[1:])
        if bits[0] == "0":
            break
    return int("".join(value),2), packet

def parse_operator(packet):
    length_type_id = packet[0]
    packet = packet[1:]
    if length_type_id == "1":
        n_packets = int(packet[:11], 2)
        packet = packet[11:]
        contents = []
        for _ in range(n_packets):
            content, packet = parse(packet)
            contents.append(content)
    elif length_type_id == "0":
        packet_length = int(packet[:15], 2)
        operator_packet = packet[15: 15 + packet_length]
        packet = packet[15 + packet_length:]
        contents = []
        while "1" in operator_packet:
            content, operator_packet = parse(operator_packet)
            contents.append(content)

    return contents, packet

def get_first_solution():
    global version_sum
    version_sum = 0
    inpt = get_inpt()
    res = parse(inpt)
    print(version_sum)

def get_second_solution():
    inpt = get_inpt()
    print(parse(inpt))

if __name__ == "__main__":
    get_first_solution()
    get_second_solution()