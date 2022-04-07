from genericpath import exists
from file_binary import binary_to_txt


def test_bin_to_txt():
    binary_to_txt.bin_to_txt("./tests/bin_matrix_test.bin", 2)
    binary_to_txt.bin_to_txt("./tests/bin_array_test.bin", 2)
    matrix_exist = exists("./tests/bin_matrix_test.txt")
    array_exist = exists("./tests/bin_array_test.txt")
    assert array_exist == True
    assert matrix_exist == True