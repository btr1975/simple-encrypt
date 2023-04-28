"""
simple-encrypt main application
"""
import json
from typing import Optional, Dict, Tuple
from cryptography.fernet import Fernet


class EncryptDecrypt:
    """Class to encrypt/decrypt data

    :type encryption_key: Optional[bytes] = None
    :param encryption_key: The encryption key
    :raises TypeError: if encryption_key is supplied but is not of type bytes
    """
    def __init__(self, encryption_key: Optional[bytes] = None) -> None:
        if encryption_key:
            if not isinstance(encryption_key, bytes):
                raise TypeError(f'encryption_key must be of type bytes but received {type(encryption_key)}!')

        self.encryption_key = encryption_key

    def generate_encrypted_data(self, data: Dict[str, Dict[str, str]]) -> Tuple[bytes, bytes]:
        """Method to generate encrypted data

        :type data: Dict[str, Dict[str, str]]
        :param data: The data to encrypt

        :rtype: Tuple[bytes, bytes]
        :returns: (encryption_key, encrypted_value)
        :raises KeyError: If encryption_key is already known
        """
        if self.encryption_key:
            raise KeyError('encryption key already known!')

        self.encryption_key = Fernet.generate_key()
        fernet_object = Fernet(self.encryption_key)
        encrypted_value = fernet_object.encrypt(json.dumps(data).encode())

        return self.encryption_key, encrypted_value

    def add_encrypted_data(self, data: Dict[str, Dict[str, str]], encrypted_value: bytes) -> bytes:
        """Method to add encrypted data

        :type data: Dict[str, Dict[str, str]]
        :param data: The data to encrypt
        :type encrypted_value: bytes
        :param encrypted_value: The current encrypted data to add to

        :rtype: bytes
        :returns: encrypted_value

        :raises KeyError: If encryption_key is not known
        :raises KeyError: If data key already exists
        """
        if not self.encryption_key:
            raise KeyError('encryption_key is not known!')

        current_data = self.decrypt_data(encrypted_value)

        for key, value in data.items():
            if key not in self.get_current_keys(encrypted_value):
                current_data[key] = value

            else:
                raise KeyError(f'data already exists with key {key}!')

        fernet_object = Fernet(self.encryption_key)
        encrypted_value = fernet_object.encrypt(json.dumps(current_data).encode())

        return encrypted_value

    def update_encrypted_data(self, data_key: str, data_value: Dict[str, str], encrypted_value: bytes) -> bytes:
        """Method to update a single keys data

        :type data_key: String
        :param data_key: The key to update
        :type data_value: Dict[str, str]
        :param data_value: The value to update to

        :rtype: bytes
        :returns: encrypted_value

        :raises KeyError: If encryption_key is not known
        :raises KeyError: If data key does not exist exists
        """
        if not self.encryption_key:
            raise KeyError('encryption_key is not known!')

        current_data = self.decrypt_data(encrypted_value)

        if current_data.get(data_key):
            current_data[data_key] = data_value

        else:
            raise KeyError(f'data not found with key {data_key}!')

        fernet_object = Fernet(self.encryption_key)
        encrypted_value = fernet_object.encrypt(json.dumps(current_data).encode())

        return encrypted_value

    def get_current_keys(self, encrypted_value: bytes) -> list:
        """Method to get the current keys from the encrypted data

        :type encrypted_value: bytes
        :param encrypted_value: The current encrypted data

        :rtype: list
        :returns: A list of keys

        :raises KeyError: If encryption_key is not known
        """
        if not self.encryption_key:
            raise KeyError('encryption_key is not known!')

        current_data = self.decrypt_data(encrypted_value)

        return list(current_data.keys())

    def decrypt_data(self, encrypted_value: bytes) -> Dict[str, Dict[str, str]]:
        """Method to decrypt data

        :type encrypted_value: bytes
        :param encrypted_value: The current encrypted data

        :rtype: Dict[str, Dict[str, str]]
        :returns: The decrypted data

        :raises KeyError: If encryption_key is not known
        """
        if not self.encryption_key:
            raise KeyError('encryption_key is not known!')

        fernet_object = Fernet(self.encryption_key)

        return json.loads((fernet_object.decrypt(encrypted_value).decode('utf-8')))
