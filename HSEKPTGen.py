#  Explicit KPOINTS file generator for HSE calculations using VASP

import numpy as np

sym_points = [[0,0,0], [0,0,0.5]]
num_line = 40

input_file_name = "IBZKPT"
output_file_name = "KPOINTS"

header_string = "Explicit k-points list"

def get_input_file():
    with open(input_file_name, 'r') as a:
        returnable = a.read().split('\n')
        returnable.pop() # Gets rid of a blank entry at end of file
        return returnable
    
def KPOINTS_writer():
    line_list = get_input_file()
        
    line_sym_points = np.linspace(sym_points[0],sym_points[1],num_line)
    for point in line_sym_points:
        line = ''
        for num in point:
            line += '{:20.14f}'.format(num)
        line += '{:14}'.format(0)
        line_list.append(line)

    line_list[0] = header_string # Change header
    line_list[1] = '{:8}'.format(int(line_list[1]) + num_line)
            
    with open(output_file_name, 'w', newline='') as a:
        for x in line_list:
            a.write(x + '\n')
    
def main():
    KPOINTS_writer()
    
main()
