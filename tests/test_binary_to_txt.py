from genericpath import exists
from file_binary import binary_to_txt


def test_bin_to_txt():
    binary_to_txt.bin_to_txt("bin_matrix_test.bin", 2)
    matrix_exist = exists("bin_matrix_test.txt")
    binary_to_txt.bin_to_txt("bin_array_test.bin", 2)
    array_exist = exists("bin_array_test.txt")
    assert array_exist == True
    assert matrix_exist == True