"""
Utility to read encrypted data
"""


def read_encrypted_file_data(path: str) -> bytes:
    """Function to read encrypted data

    :type path: str
    :param path: The full path including file name where the data is stored

    :rtype: bytes
    :returns: The encrypted data
    """
    with open(path, 'br+') as file:
        encrypted_data = file.read()

    return encrypted_data
