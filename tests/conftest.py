import os, sys
import pytest
base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
sys.path.append(os.path.join(base_path))
from simple_encrypt.util.file_read import read_encrypted_file_data


@pytest.fixture
def data_a():
    return {'A': {'1': 'THING'}}


@pytest.fixture
def data_b():
    return {'B': {'2': 'THING'}}


@pytest.fixture
def data_should_be_after_add():
    return {'A': {'1': 'THING'}, 'B': {'2': 'THING'}}


@pytest.fixture
def data_b_update():
    return {'B': {'3': 'THING'}}



@pytest.fixture
def saved_key():
    return read_encrypted_file_data('./tests/data/key.txt')


@pytest.fixture
def saved_value():
    return read_encrypted_file_data('./tests/data/value.txt')
