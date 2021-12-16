# https://adventofcode.com/2021/day/16

'''
0 = 0000
1 = 0001
2 = 0010
3 = 0011
4 = 0100
5 = 0101
6 = 0110
7 = 0111
8 = 1000
9 = 1001
A = 1010
B = 1011
C = 1100
D = 1101
E = 1110
F = 1111
'''
from os import getenv
import pathlib
import time

script_path = pathlib.Path(__file__).parent
input = script_path / 'input.txt'  # 
input_test = script_path / 'test.txt'  # 



class packets:
    def __init__(self, data) -> None:
        self.data = data
        self.location = 0 # used to locate where the parsing is currently
    
    # def getData(self):
    #     return self.data

    # def getLocation(self):
    #     return self.location
        
    # def getPacketVersion(self):
    #     return int(self.data[0:3],2)

    # def getPacketType(self):
    #     return int(self.data[3:6],2)


    def increase_bit_location(self, amount):
        self.location += amount


    def get_number(self, numbits):
        # replaced hard coded values to use the current position, moves along once processed
        answer = int(self.data[self.location:self.location+numbits], 2)
        print(answer)
        self.increase_bit_location(numbits)
        return answer


    def process_single_packet(self):
        # replaced hard coded values to use the current position, the move along once processed
        packet_version = self.get_number(3)
        packet_type = self.get_number(3)
        packet_data = self.readPacketData(packet_type)  # This is OTHER packets OR a value (type 4)

        # Return a tuple of the three parts of a packet
        return (packet_version, packet_type, packet_data)


    def calculate_type4_packet_value(self):
        # For Type 4 its a 5 bit integer
        # TODO learn bitwise comparators to get bits need

        # loop until end of group, but need to get the value and move the bit counters
        # # 0 is the end of the group

        msg = []
        get_value = True

        while get_value:
            check_bit = self.data[self.location]
            print(self.location)
            msg.append(self.data[self.location+1:self.location+5])
            print(msg)
            self.increase_bit_location(5)
            if check_bit == '0':
                get_value = False
            
        print(msg)
        num = ''.join(msg)
        ans = int(num,2)
        print(ans)

        return ans


    def readNumberOfPackets(self, howMany):
        # ok replaced code with generator that calls other methods howMay times           
        return [self.process_single_packet() for _ in range(howMany)]


    def readPacketData(self, typeid):
        if typeid == 4:
            return self.calculate_type4_packet_value()

        return self.processOperator()


    def processNumberPackets(self, bit_length):
        target = self.location + bit_length
        packet_list = []

        while self.location < target:
            packet_list.append(self.process_single_packet)

        return packet_list


    def processOperator(self):
        length_id = self.get_number(1)

        if length_id == 0:
        # length type ID is 0,  next 15 bits = total length in bits of the sub-packets contained by this packet.
            return self.readNumberOfPackets(self.get_number(11))
        else:
        # length type ID is 1, next 11 bits = the number of sub-packets immediately contained by this packet.
            return self.readNumberOfPackets(self.get_number(11))


def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        data = file.readlines()
    code= data[0]
    return code


def hex_to_binary(hex_number: str, num_digits: int = 8) -> str:
    """
    Converts a hexadecimal value into a string representation
    of the corresponding binary value
    Args:
        hex_number: str hexadecimal value
        num_digits: integer value for length of binary value.
                    defaults to 8
    Returns:
        string representation of a binary number 0-padded
        to a minimum length of <num_digits>
    """
    return str(bin(int(hex_number, 16)))[2:].zfill(len(hex_number) * 4 )


# def returnPacketInfo(binary_input):

#     packet_version = int(binary_input[0:3],2)
#     packet_type = int(binary_input[3:6] ,2)
#     data = binary_input[6:]

#     return (packet_version, packet_type, data)


def processVersions(pk):
    ver, typeid, data = packets

    if typeid == 4:
        return ver

    # recursive bit
    return ver + sum(map(processVersions, data))


def part1(data):
    """Solve part 1""" 
    # data='D2FE28'
    # # data='38006F45291200'
    # # data='EE00D40C823060' 
    # print(data)

    # binary_input = hex_to_binary(data)
    # print(binary_input)

    # packet_version, packet_type, packet_data = returnPacketInfo(binary_input)
    # print('ver',packet_version, 'type', packet_type, 'remaining', packet_data)
    # packet_version = int(binary_input[0:3],2)
    # packet_type = int(binary_input[3:6]  ,2)
    # print('ver',packet_version, 'type', packet_type)

    # remaining = binary_input[6:]
    # print('rem',remaining)

    print('-------')
    data='D2FE28'
    binary_input = hex_to_binary(data)
    stream = packets(binary_input)
    firstpacket = stream.process_single_packet()
    print(firstpacket)
    print('-------')
    
    # print('-------')
    # data='38006F45291200'
    # binary_input = hex_to_binary(data)
    # stream = packets(binary_input)
    # firstpacket = stream.processSinglePacket()
    # print(firstpacket)
    # print('-------')

    return 1


def part2(data):
    """Solve part 2"""   
   
    return 1
 

def solve(puzzle_input):
    """Solve the puzzle for the given input"""
    times=[]

    data = parse(puzzle_input)
    
    times.append(time.perf_counter())
    solution1 = part1(data)
    times.append(time.perf_counter())
    solution2 = part2(data)
    times.append(time.perf_counter())
    
    return solution1, solution2, times


def runTest(test_file):
    data = parse(test_file)
    test_solution1 = part1(data)
    test_solution2 = part2(data)
    return test_solution1, test_solution2


def runAllTests():
    
    print("Tests")
    a, b  = runTest(input_test)
    print(f'Test1.  Part1: {a} Part 2: {b}')


if __name__ == "__main__":    # print()

    runAllTests()

    # solutions = solve(input)
    # print('\nAOC')
    # print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    # print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    # print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")