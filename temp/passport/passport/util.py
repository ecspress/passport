"""Module containing utility methods"""
import os
import random
import string

def generate_random_bytes(length):
    """Generates random bytes by using OS sources.
    Input:
        length: number of bytes to generate
    Output:
        bytearray
    Raises:
        None
    """
    return os.urandom(length)

def generate_password(length=20):
    """Generates random password.
    Input:
        length: password length less than 42, default is 20
    Output:
        string containing generated password
    Raises:
        None
    """
    chars = [string.digits, string.ascii_lowercase, string.ascii_uppercase, string.punctuation]
    digits = []
    sample_size = length // len(chars)

    random.seed(generate_random_bytes(1))
    random.shuffle(chars)

    for elem in chars:
        digits.extend([x for x in random.sample(elem, sample_size)])
    digits.extend([elem for elem in random.sample(chars[-1], length - len(digits))])

    random.seed(generate_random_bytes(1))
    random.shuffle(digits)
    return "".join(digits)

def left_xor(input1, input2):
    """XORs two binary numbers until bits in smaller value runs out, then XORs against 0.
    Input:
        input1: string containing binary representation of data
        input2: string containing binary representation of data
    Output:
        string with length of largest input containing binary representation of input1 XOR input2
    Raises:
        TypeError: if input1/input2 is not of type string
        ValueError: if input1/input2 contains characters not (0, 1)
    """
    if type(input1) != str != type(input2):
        raise TypeError("Inputs must be of type str")

    digits = set(string.digits[2:])
    if len(digits.intersection(set(input1))) > 0 < len(digits.intersection(set(input2))):
        raise ValueError("Inputs must only contain binary characters (0, 1)")

    xor = "".join([str(int(x) ^ int(y)) for x, y in zip(input1, input2)])

    to_append = []
    if len(input1) > len(input2):
        to_append = input1[len(input2):]
    elif len(input1) < len(input2):
        to_append = input2[len(input1):]

    return xor + "".join(to_append)
