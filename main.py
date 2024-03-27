from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


def generate_key_pair():
    """
    Gera um par de chaves pública e privada RSA de 2048 bits.

    Retorna:
        tuple: Uma tupla contendo a chave privada e a chave pública geradas.

    Exemplo:
        private_key, public_key = generate_key_pair()
    """

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend
    )
    public_key = private_key.public_key()

    with open('private_key.pem', 'wb') as file:
        file.write(
            private_key.private_bytes(
                enconding=serialization.Enconding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
        )

    with open('public_key.pem', 'wb') as file:
        file.write(
            public_key.public_bytes(
                enconding=serialization.Enconding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )

    return private_key, public_key

private_key, public_key = generate_key_pair()
print("Chaves geradas e exportadas com sucesso!")