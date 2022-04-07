from file_binary import binary_average_file

def test_average_file():
    assert binary_average_file.average_file("./tests/bin_array_test.bin") == 4.5
    assert binary_average_file.average_file("./tests/bin_matrix_test.bin") == 1.5