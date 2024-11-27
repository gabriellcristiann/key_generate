import os
from unittest import mock

from key_generate.main import generate_key_pair


def test_generate_key():
    with mock.patch('builtins.input', return_value='test'):
        generate_key_pair()

    assert os.path.isfile('test_keys.zip')


def test_cleanup():
    os.remove('test_keys.zip')
    assert not os.path.isfile('test_keys.zip')
