import pytest
from simple_encrypt import EncryptDecrypt


def test_generate_encrypted_data(data_a):
    obj = EncryptDecrypt()
    encryption_key, encryption_value = obj.generate_encrypted_data(data_a)

    assert isinstance(encryption_key, bytes)
    assert isinstance(encryption_value, bytes)


def test_generate_encrypted_data_bad(saved_key, data_a):
    obj = EncryptDecrypt(saved_key)
    with pytest.raises(KeyError):
        obj.generate_encrypted_data(data_a)


def test_add_encrypted_data(saved_key, saved_value, data_b, data_should_be_after_add):
    obj = EncryptDecrypt(saved_key)
    new_encrypted_data = obj.add_encrypted_data(data_b, saved_value)

    assert isinstance(new_encrypted_data, bytes)

    data = obj.decrypt_data(new_encrypted_data)

    assert data == data_should_be_after_add


def test_add_encrypted_data_bad_key():
    with pytest.raises(TypeError):
        EncryptDecrypt('bad-key')


def test_add_encrypted_data_bad_no_key(saved_value, data_b, data_should_be_after_add):
    obj = EncryptDecrypt()
    with pytest.raises(KeyError):
        obj.add_encrypted_data(data_b, saved_value)


def test_add_encrypted_data_bad_key_value_exists(saved_key, saved_value, data_a):
    obj = EncryptDecrypt(saved_key)
    with pytest.raises(KeyError):
        obj.add_encrypted_data(data_a, saved_value)


def test_update_encrypted_data(saved_key, saved_value, data_b, data_b_update):
    obj = EncryptDecrypt(saved_key)
    new_encrypted_data = obj.add_encrypted_data(data_b, saved_value)

    assert isinstance(new_encrypted_data, bytes)

    new_new_encrypted_data = obj.update_encrypted_data('B', {'3': 'THING'}, new_encrypted_data)

    assert isinstance(new_new_encrypted_data, bytes)


def test_update_encrypted_data_bad_no_key(saved_value, data_b, data_b_update):
    obj = EncryptDecrypt()
    with pytest.raises(KeyError):
        obj.update_encrypted_data('B', {'3': 'THING'}, saved_value)


def test_update_encrypted_data_bad_data_not_found(saved_key, saved_value, data_b, data_b_update):
    obj = EncryptDecrypt(saved_key)
    with pytest.raises(KeyError):
        obj.update_encrypted_data('B', {'3': 'THING'}, saved_value)


def test_get_current_keys_bad_no_key(saved_value):
    obj = EncryptDecrypt()
    with pytest.raises(KeyError):
        obj.get_current_keys(saved_value)


def test_decrypt_data_bad_no_key(saved_value):
    obj = EncryptDecrypt()
    with pytest.raises(KeyError):
        obj.decrypt_data(saved_value)
