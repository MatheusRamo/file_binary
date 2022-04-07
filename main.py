from file_binary import binary_average_file
from file_binary import binary_array_file
from file_binary import binary_matrix_file
from file_binary import binary_to_txt

binary_array_file.create_binary_array_file("array.bin", 4)
binary_to_txt.bin_to_txt("array.bin", 2)