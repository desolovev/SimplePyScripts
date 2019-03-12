#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# pip install pycryptodome
# OR:
# pip install pycryptodomex


from Crypto.PublicKey import RSA

secret_code = "Unguessable"
key = RSA.generate(2048)
encrypted_key = key.export_key(passphrase=secret_code)

with open("rsa_private_key.pem", "wb") as f:
    f.write(encrypted_key)

with open("rsa_public_key.pem", "wb") as f:
    f.write(key.publickey().export_key())
