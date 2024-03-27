# Gerador de Chaves RSA

Este script Python gera um par de chaves pública e privada RSA de 2048 bits e as exporta para arquivos no formato PEM.

## Requisitos

Certifique-se de ter o módulo `cryptography` instalado. Você pode instalar utilizando o seguinte comando:

```python
pip install cryptography
```

ou 

```python
pip install -r requirements.txt
```


## Uso

1. Execute o script `generate_key_pair.py` para gerar as chaves.

2. Após a execução, as chaves serão armazenadas nos arquivos `private_key.pem` (chave privada) e `public_key.pem` (chave pública).

## Exemplo de Uso

```python
from generate_key_pair import generate_key_pair

private_key, public_key = generate_key_pair()
print("Chaves geradas e exportadas com sucesso!")
```

Certifique-se de proteger adequadamente a chave privada (private_key.pem) e nunca compartilhá-la publicamente.

___

Autor: Gabriel Cristian

___

## Licença

Este projeto está licenciado sob os termos da [Licença MIT](LICENSE).