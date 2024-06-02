# For HSE band structure calculations. Removes all blocks from EIGENVALS except for the zero weight
# blocks added in KPOINTS before running.

kpt_grid = 8 # k-point grid size used

input_file_name = 'EIGENVAL'
output_file_name = 'EIGENVAL_OUT'

# Returns the EIGANVAL file as a list of strings, each element as a new line
def get_input_file():
    with open(input_file_name, 'r') as a:
        returnable = a.read().split('\n')
        returnable.pop() # Gets rid of a blank entry at end of file
        return returnable

# Edit line 6 info, slice out the kpt blocks we don't want
def eigen_edit(string_list):

    # Line 6 editing
    temp = string_list[5].split()
    e_num = int(temp[0].strip())
    kpt_num = int(temp[1].strip()) - kpt_grid # Remove non-zero weighted k-points from k-point count
    band_num = int(temp[2].strip())
    
    # Recombine line 6 (magic)
    string_list[5] = '{:6}'.format('') + ''.join('{:7}'.format(str(x)) for x in [e_num, kpt_num, band_num])
    
    # Starting at line 7, remove (block #) * (line 7 + 2 whitespace lines + band # per block)
    del string_list[7:("""replaceable""" * (7 + 2+ band_num))]
    
    return string_list
            
# Write out the new EIGENVAL file line by line
def eigen_write(writeable):
    with open(output_file_name, 'w', newline='') as a:
        for x in writeable:
            a.write(x + '\n')
		
def main():
	eigen_write(eigen_edit(get_input_file()))

main()
