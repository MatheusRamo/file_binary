from file_binary import binary_matrix_file
from file_binary import binary_array_file
from file_binary import binary_average_file


binary_matrix_file.create_binary_matrix_file("matrix.bin", 2, 2)
binary_array_file.create_binary_array_file("array.bin", 5)
average = binary_average_file.average_file("matrix.bin")
print(average)