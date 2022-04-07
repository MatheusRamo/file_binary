from genericpath import exists
from file_binary import fb


def test_create_binary_array_file():
    fb.create_binary_array_file("./tests/bin_array_test.bin", 10)
    file_exist = exists("./tests/bin_array_test.bin")
    assert file_exist == True

def test_create_binary_matrix_file():
    fb.create_binary_matrix_file("./tests/bin_matrix_test.bin",2,2)
    file_exist = exists("./tests/bin_matrix_test.bin")
    assert file_exist == True

def test_average_file():
    assert fb.average_file("./tests/bin_array_test.bin") == 4.5
    assert fb.average_file("./tests/bin_matrix_test.bin") == 1.5


def test_bin_to_txt():
    fb.bin_to_txt("./tests/bin_matrix_test.bin", 2)
    fb.bin_to_txt("./tests/bin_array_test.bin", 2)
    matrix_exist = exists("./tests/bin_matrix_test.txt")
    array_exist = exists("./tests/bin_array_test.txt")
    assert array_exist == True
    assert matrix_exist == True