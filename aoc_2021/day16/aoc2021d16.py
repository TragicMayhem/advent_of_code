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

    def getNumber(self, numbits):
        # replaced hard coded values to use the current position, the move along once processed
        answer = int(self.data[self.location:self.location+numbits], 2)
        self.location += numbits
        return answer

    def returnSinglePacket(self):
        # replaced hard coded values to use the current position, the move along once processed
        packet_version = self.getNumber(3)
        packet_type = self.getNumber(3)
        
        # needs to change to get sub packet informaton
        packet_data = self.data[self.location:]

        return (packet_version, packet_type, packet_data)

    def increaseLocation(self, amount):
        self.location += amount

    def processPacketValue(self):
        # For Type 4 its a 5 bit integer
        msg = []

        # loop until end of group, but need to get the value and move the bit counters
        # 0 is the end of the group

        # TODO learn bitwise comparators to get bits need

        for i in range(0, len(self.data), 5):
            next = packet_data[i:i+5]
            if len(next) < 5:
                break
            msg.append(next[1:])

        print(msg)
        num = ''.join(msg)
        print(int(num,2))

        val = self.getNumber(5) 

        if packet_type == 4:
            for i in range(0, len(binary_input), 5):
                print(i)
                next = packet_data[i:i+5]
                print(next)
                if len(next) < 5:
                    break
                msg.append(next[1:])

        print(msg)
        num = ''.join(msg)
        print(int(num,2))

        return ''

    def readNumberOfPackets(self, howMany):
        # ok replaced code with generator that calls other methods howMay times           
        return [self.returnSinglePacket() for _ in range(howMany)]

    def processOperator(self):
        length_type = self.getNumber(1)

        if length_type == 1:
            pack_len = 15
        else:
            pack_len = 11

        return ''


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


def returnPacketInfo(binary_input):

    packet_version = int(binary_input[0:3],2)
    packet_type = int(binary_input[3:6] ,2)
    data = binary_input[6:]

    return (packet_version, packet_type, data)


def part1(data):
    """Solve part 1""" 
    data='D2FE28'
    # data='38006F45291200'
    # data='EE00D40C823060' 
    print(data)

    binary_input = hex_to_binary(data)
    print(binary_input)

    packet_version, packet_type, packet_data = returnPacketInfo(binary_input)
    print('ver',packet_version, 'type', packet_type, 'remaining', packet_data)

    # packet_version = int(binary_input[0:3],2)
    # packet_type = int(binary_input[3:6]  ,2)
    # print('ver',packet_version, 'type', packet_type)

    # remaining = binary_input[6:]
    # print('rem',remaining)
    print('-------')
    inputData = packets(binary_input)
    print('class',inputData.getData())
    print(inputData.returnPacketInfo())

    print('-------')
    processed = False
    msg = []

    # if type == 4

    if packet_type == 4:
        for i in range(0, len(binary_input), 5):
            print(i)
            next = packet_data[i:i+5]
            print(next)
            if len(next) < 5:
                break
            msg.append(next[1:])

        print(msg)
        num = ''.join(msg)
        print(int(num,2))

    if packet_type != 4:
        sub_packet_length = 15 if packet_data[0] == '0' else 11
        print(sub_packet_length)

        next = packet_data[1:sub_packet_length]
        print(next)

    tmp='1101000101'
    print(int(tmp,2))

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