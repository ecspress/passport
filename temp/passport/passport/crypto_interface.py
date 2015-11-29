"""Interface to the crypto module"""

from Crypto.Cipher import AES # pylint: disable=import-error
import hashlib
import passport.util as util

PAD_NEEDED = lambda data: AES.block_size - (len(data) % AES.block_size)
PAD = lambda data: data + PAD_NEEDED(data) * bytes([PAD_NEEDED(data)])
UNPAD = lambda data: data[:-ord(data[len(data)-1:])]

def encrypt(key, data, salt=None):
    """encrypts data using AES algorithm in CBC mode with the given key.
    Input:
        key: byte string of length (16, 24, 32)
        data: byte string containing data to be encrypted
              padding is used to meet convert data into AES blocksize (16)
        salt: (optional) byte string of length 16
    Output:
        byte string of IV + cipher_text
    Raises:
        TypeError:
        ValueError:
    """

    if not type(key) == bytes == type(data):
        raise TypeError("Key/data must be of type bytes")

    if len(key) not in AES.key_size:
        raise ValueError("key must be of length (16, 24, 32) bytes")

    data = PAD(data)
    if not salt:
        salt = util.generate_random_bytes(AES.block_size)
    encrypter = AES.new(key, AES.MODE_CBC, salt)
    return salt + encrypter.encrypt(data)

def decrypt(key, data):
    """decrypts data using AES algorithm in CBC mode with the given key.
    Input:
        key: byte string of length (16, 24, 32)
        data: byte string containing iv + data to be decrypted
              padded bytes will be removed as needed
    Output:
        byte string of plain text
    Raises:
        TypeError:
        ValueError:
    """

    if not type(key) == bytes == type(data):
        raise TypeError("Key/data must be of type bytes")

    if len(key) not in AES.key_size:
        raise ValueError("key must be of length (16, 24, 32) bytes")

    salt = data[:AES.block_size]
    data = data[AES.block_size:]
    decrypter = AES.new(key, AES.MODE_CBC, salt)
    return UNPAD(decrypter.decrypt(data))

def generate_hash(key, iterations, salt=None, length=None, hash_function="SHA512"):
    """Generates a key based on pass_phrase using PBKDF2 with default hash function of SHA512
    Input:
        key: byte string based on which hash will be generated
        iterations: Number of times hash_function is applied
        salt: byte string to randomize hash generation
        length: length of output hash (default being the length of hash function)
        hash_function: function that is able to generate hash i.e. sha128, sha256 (default: sha512)
    Output:
        byte string
    Raises:
        TypeError:
    """

    if not type(key) == bytes:
        raise TypeError("Key must be of type bytes")

    hash_function = "SHA512"
    if not salt:
        salt = util.generate_random_bytes(32)
    return hashlib.pbkdf2_hmac(hash_function, key, salt, iterations, dklen=length)
