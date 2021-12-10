
import pathlib
import sys

if sys.platform == "linux" or sys.platform == "linux2":
  dirpath = sys.path[0] + "/"
elif sys.platform == "darwin":
  dirpath = sys.path[0] + "/"
elif sys.platform == "win32":
  dirpath = sys.path[0] + "\\\\"

input_test = 'test.txt'  # 5 
input = 'input.txt'  #  

if __name__ == "__main__":
    print ('main')

    in_file_1 = pathlib.Path.cwd() / "in" / "input.xlsx"
    out_file_1 = pathlib.Path.cwd() / "out" / "output.xlsx"
    parts = ["in", "input.xlsx"]
    in_file_3 = pathlib.Path.cwd().joinpath(*parts)

    print(in_file_1)
    print(type(in_file_1))

    print('__file__:    ', __file__)
    script_path = pathlib.Path(__file__).parent
    print(script_path)
    print(pathlib.Path.cwd())

    file_in = pathlib.Path.cwd() / input_test
    #puzzle_input = pathlib.Path(file_in).read_text().strip()
    #print(puzzle_input)