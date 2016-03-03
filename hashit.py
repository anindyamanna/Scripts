#!/bin/sh

from hashlib import *
from sys import argv


if len(argv)<=2:
	print("Usage: python hashit.py [HASH_TYPE(SHA1/SHA512/MD5/SHA256/SHA224/SHA384)] [PHRASE_TO_HASH]")
	exit(0)

result = ()

hash_type = argv[1].lower()
hash_value = argv[2]

if hash_type == "md5":
	result = md5(hash_value.encode())
elif hash_type == "sha512":
	result = sha512(hash_value.encode())
elif hash_type == "sha1":
	result = sha1(hash_value.encode())
elif hash_type == "sha256":
	result = sha256(hash_value.encode())
elif hash_type == "sha224":
	result = sha224(hash_value.encode())
elif hash_type == "SHA384":
	result = SHA384(hash_value.encode())
else:
	print("Usage: python hashit.py [HASH_TYPE(SHA1/SHA512/MD5/SHA256/SHA224/SHA384)] [PHRASE_TO_HASH]")
	exit(0)

print(result.hexdigest())
