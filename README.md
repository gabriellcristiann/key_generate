# Gerador de Chaves RSA

Este script Python gera um par de chaves pública e privada RSA de 2048 bits a partir do nome fornecido pelo usuário e as exporta para um arquivo .zip.

## Requisitos

 - python 3.12
 - poetry

Certifique-se de ter o módulo `cryptography` instalado. Você pode instalar utilizando o seguinte comando:

```sh
poetry install
```

## Uso

1. Execute o script main.py para gerar as chaves.

2. Após a execução, as chaves serão armazenadas em um arquivo .zip com o nome fornecido pelo usuário.

## Exemplo de Uso

```sh
python key_generate/main.py
```
ou 

```sh
task run
```

Ao executar este comando o script ira perguntar o nome da aplicação para o qual as chaves serão geradas, o nome fornecido será utilizado na criação do arquivo `zip` com as chaves.

Pronto suas chaves estão criadas!

> Certifique-se de proteger adequadamente a chave privada e nunca compartilhá-la publicamente.

## Testes

Você pode rodar os testes utilizando o comando:

```sh
task test
```
Isso executará os testes definidos em tests/test_main.py.

___

Autor: Gabriel Cristian

___

## Licença

Este projeto está licenciado sob os termos da [Licença MIT](LICENSE).
