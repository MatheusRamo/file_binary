from genericpath import exists
from file_binary import binary_matrix_file

def test_create_binary_matrix_file():
    binary_matrix_file.create_binary_matrix_file("bin_matrix_test.bin",2,2)
    file_exist = exists("bin_matrix_test.bin")
    assert file_exist == True