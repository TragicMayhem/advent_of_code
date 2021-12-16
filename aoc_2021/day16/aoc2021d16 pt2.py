# https://adventofcode.com/2021/day/16

'''
# data='D2FE28'                 (6, 4, 2021)
# data='38006F45291200'         (1, 6, [(6, 4, 10), (2, 4, 20)])
# data='EE00D40C823060'         (7, 3, [(2, 4, 1), (4, 4, 2), (1, 4, 3)])

Version sum examples
# data='8A004A801A8002F478'             Expect: 16 
# data='620080001611562C8802118E34'     Expect: 12  
# data='C0015000016115A2E0802F182340'   Expect: 23  
# data='A0016C880162017C3686B18A3D4780' Expect: 31  
'''
import pathlib
import time
from math import prod

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
        # print('loc++', self.location, 'adding', amount)
        self.location += amount


    def get_number(self, numbits):
        # replaced hard coded values to use the current position, moves along once processed
        answer = int(self.data[self.location:self.location+numbits], 2)
        self.increase_bit_location(numbits)
        # print('val', answer)
        return answer


    def process_single_packet(self):
        # replaced hard coded values to use the current position, the move along once processed
        packet_version = self.get_number(3)
        packet_type = self.get_number(3)
        packet_data = self.process_packet_data(packet_type)  # This is OTHER packets OR a value (type 4)

        # Return a tuple of the three parts of a packet
        return (packet_version, packet_type, packet_data)


    def calculate_type4_packet_value(self):
        # For Type 4 its a 5 bit integer
        # TODO learn bitwise comparators to get bits need???

        msg = []
        get_value = True

        while get_value:
            check_bit = self.data[self.location]
            msg.append(self.data[self.location+1:self.location+5])
            self.increase_bit_location(5)
            if check_bit == '0':
                get_value = False
            
        # print('msg list', msg)
        num = ''.join(msg)
        ans = int(num,2)
        # print('value', ans)
        # print('loc', self.location)

        return ans


    def process_num_of_packets(self, howMany):
        # ok replaced code with generator that calls other methods howMay times           
        return [self.process_single_packet() for _ in range(howMany)]


    def process_packet_data(self, typeid):
        # print('process_packet_data', typeid)
        
        if typeid == 4:
            return self.calculate_type4_packet_value()

        return self.process_operator_data()


    def process_packet_length(self, bit_length):
        # print('process_packet_length with bit length', bit_length)
        stop_target = self.location + bit_length
        packet_list = []

        # print('  loop starting', self.location, stop_target)

        while self.location < stop_target:
            # print('  looping', self.location, stop_target)
            packet_list.append(self.process_single_packet())

        return packet_list


    def process_operator_data(self):
        length_id = self.get_number(1)
        # print('process_operator_data length id:', length_id)

        if length_id == 0:
        # length type ID is 0,  next 15 bits = total length in bits of the sub-packets contained by this packet.
            return self.process_packet_length(self.get_number(15))
        else:
        # length type ID is 1, next 11 bits = the number of sub-packets immediately contained by this packet.
            return self.process_num_of_packets(self.get_number(11))


def parse(puzzle_input):
    """Parse input """

    with open(puzzle_input, 'r') as file:
        data = file.readlines()
    code= data[0]
    return code

def hex_to_binary(hex_number: str) -> str:
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
    
    # TODO turns out bytes.fromhex() does this??  bytes.fromhex('D2FE28')
    # DL's version "{0:0{width}b}".format(int(hex_value, 16), width=bin_len)
    return str(bin(int(hex_number, 16)))[2:].zfill(len(hex_number) * 4 )


# def returnPacketInfo(binary_input):

#     packet_version = int(binary_input[0:3],2)
#     packet_type = int(binary_input[3:6] ,2)
#     data = binary_input[6:]

#     return (packet_version, packet_type, data)


def add_up_all_versions(pk):
    ver, typeid, data = pk

    if typeid == 4:
        return ver

    # recursive bit
    return ver + sum(map(add_up_all_versions, data))


def calculate_root_value(pk):
    '''
    0 = sum
    1 = product
    2 = min
    3 = max
    4 = VALUE
    5 = will be 2 packets, 1 if 1st > 2nd else 0 
    6 = will be 2 packets, 1 if 1st < 2nd else 0
    7 = will be 2 packets, 1 if 1st = 2nd else 0
    '''
    ver, typeid, data = pk
    print('calculate_root_value', pk)

    # do this first because it is just a value, so return (and wont run the map without an iterable)
    if typeid == 4:
        return data

    nums = map(calculate_root_value, data)

    if typeid == 0: return sum(nums)
    if typeid == 1: return prod(nums)
    if typeid == 2: return min(nums)
    if typeid == 3: return max(nums)

    first_value, second_value = nums
    print('type', typeid, '1st', first_value, '2nd', second_value)

    if typeid == 5:
        return 1 if first_value > second_value else 0
    if typeid == 6:
        return 1 if first_value < second_value else 0
    if typeid == 7:
        return 1 if first_value == second_value else 0

    return 404


def part1(data):
    """Solve part 1""" 
    
    binary_input = hex_to_binary(data)
    stream = packets(binary_input)
    packet_information = stream.process_single_packet()
    version_sum = add_up_all_versions(packet_information)

    return version_sum


def part2(data):
    """Solve part 2"""   
   
    binary_input = hex_to_binary(data)
    stream = packets(binary_input)
    packet_information = stream.process_single_packet()
    root_value = calculate_root_value(packet_information)

    return root_value
 

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


def runAllTests(test_file):
    data = parse(test_file)
    
    print("TESTS PART1")

    print('\n-------')
    data='D2FE28'
    binary_input = hex_to_binary(data)
    stream = packets(binary_input)
    packet_information = stream.process_single_packet()
    print(packet_information)

    version_sum = add_up_all_versions(packet_information)
    print("Version sum = ",version_sum)

    print('\n-------')
   
    data='38006F45291200'
    binary_input = hex_to_binary(data)
    stream = packets(binary_input)
    packet_information = stream.process_single_packet()
    print(packet_information)
    version_sum = add_up_all_versions(packet_information)
    print("Version sum = ",version_sum)

    print('\n-------')
    data='EE00D40C823060'
    binary_input = hex_to_binary(data)
    stream = packets(binary_input)
    packet_information = stream.process_single_packet()
    print(packet_information)
    version_sum = add_up_all_versions(packet_information)
    print("Version sum = ",version_sum)

    print('\n------- Just sums using Part1 function')

    data='8A004A801A8002F478'             # Expect: 16 
    print(part1(data))

    data='620080001611562C8802118E34'     # Expect: 12  
    print(part1(data))

    data='C0015000016115A2E0802F182340'   # Expect: 23  
    print(part1(data))

    data='A0016C880162017C3686B18A3D4780' # Expect: 31  
    print(part1(data))

    data='A0016C880162017C3686B18A3D4780' # Expect: 31  
    print(part1(data))

    print('\n------- Checking part 2 (first with part 1)')

    data='C200B40A82' # Sum packet 1 + 2 = 3
    binary_input = hex_to_binary(data)
    stream = packets(binary_input)
    packet_information = stream.process_single_packet()
    print(packet_information)
    print('root = ', calculate_root_value(packet_information))


    data='04005AC33890' # product 6*9 = 54
    binary_input = hex_to_binary(data)
    stream = packets(binary_input)
    packet_information = stream.process_single_packet()
    print(packet_information)
    print('root = ', calculate_root_value(packet_information))

    data='880086C3E88112' # min of 7,8,9 = 7
    binary_input = hex_to_binary(data)
    stream = packets(binary_input)
    packet_information = stream.process_single_packet()
    print(packet_information)
    print('root = ', calculate_root_value(packet_information))
    
    data='CE00C43D881120' # max of 7,8,9 = 9
    binary_input = hex_to_binary(data)
    stream = packets(binary_input)
    packet_information = stream.process_single_packet()
    print(packet_information)
    print('root = ', calculate_root_value(packet_information))

    data='D8005AC2A8F0' # less than 5<15 -> 1
    binary_input = hex_to_binary(data)
    stream = packets(binary_input)
    packet_information = stream.process_single_packet()
    print(packet_information)
    print('root = ', calculate_root_value(packet_information))

    data='F600BC2D8F' #  more than 5<15 -> 0
    binary_input = hex_to_binary(data)
    stream = packets(binary_input)
    packet_information = stream.process_single_packet()
    print(packet_information)
    print('root = ', calculate_root_value(packet_information))

    data='9C005AC2F8F0' # eq 5!=15 = 0
    binary_input = hex_to_binary(data)
    stream = packets(binary_input)
    packet_information = stream.process_single_packet()
    print(packet_information)
    print('root = ', calculate_root_value(packet_information))

    data='9C0141080250320F1802104A08' # 1+3 = 2*2 -> 1
    binary_input = hex_to_binary(data)
    stream = packets(binary_input)
    packet_information = stream.process_single_packet()
    print(packet_information)
    print('root = ', calculate_root_value(packet_information))


if __name__ == "__main__":    # print()

    runAllTests(input_test)

    solutions = solve(input)
    print('\nAOC')
    print(f"Solution 1: {str(solutions[0])} in {solutions[2][1]-solutions[2][0]:.4f}s")
    print(f"Solution 2: {str(solutions[1])} in {solutions[2][2]-solutions[2][1]:.4f}s")
    print(f"\nExecution total: {solutions[2][-1]-solutions[2][0]:.4f} seconds")