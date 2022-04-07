from genericpath import exists
from file_binary import binary_array_file


def test_create_binary_array_file():
    binary_array_file.create_binary_array_file("./tests/bin_array_test.bin", 10)
    file_exist = exists("./tests/bin_array_test.bin")
    assert file_exist == True