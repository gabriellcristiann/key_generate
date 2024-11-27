"""
Gera um par de chaves pública e privada RSA de 2048 bits
a partir do nome fornecido pelo usuário.

Essas chaves são armazenadas em um arquivo .zip
"""

import os
import zipfile

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


def generate_key_pair(name_key: str = None):
    """Gerador de Chaves"""

    if not name_key:  # pragma: no cover
        name_key = input('Nome da chave para aplicação.: ')

    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048, backend=default_backend()
    )
    public_key = private_key.public_key()

    with open('private_key', 'wb') as file:
        file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )

    with open('public_key.pub', 'wb') as file:
        file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            )
        )

    def zip_file_keys():
        """Cria arquivo .zip com as chaves geradas"""

        with zipfile.ZipFile(f'{name_key}_keys.zip', 'w') as zip:
            zip.write('public_key.pub')
            zip.write('private_key')

    zip_file_keys()

    os.remove('public_key.pub')
    os.remove('private_key')


if __name__ == '__main__':  # pragma: no cover
    generate_key_pair()
    print('Chaves geradas e exportadas com sucesso!')
