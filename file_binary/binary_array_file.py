import numpy as np

def create_binary_array_file(name, n):
    """
    This function create a binary file of an array with n items
    """
    qualquer = np.arange(n, dtype=np.float32)
    qualquer.tofile(name)

if __name__=='__main__':
    pass
