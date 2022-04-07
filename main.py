from file_binary import binary_matrix_file
from file_binary import binary_to_txt

binary_matrix_file.create_binary_matrix_file("matriz.bin", 4, 4)
binary_to_txt.bin_to_txt("matriz.bin", 4)