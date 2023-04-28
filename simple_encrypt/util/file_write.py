"""
Utility to write encrypted data
"""


def write_encrypted_file_data(path: str, encrypted_data: bytes) -> None:
    """Function to write encrypted data

    :type path: str
    :param path: The full path including file name where the data is stored
    :type encrypted_data: bytes
    :param encrypted_data: The encrypted data

    :rtype: bytes
    :returns: The encrypted data
    """
    with open(path, 'bw+') as file:
        file.write(encrypted_data)
