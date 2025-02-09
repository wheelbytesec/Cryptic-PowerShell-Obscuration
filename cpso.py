import argparse
from Crypto.Cipher import AES
from zlib import compress as zipfile
import base64
import random

def generate_key(size=16):
    return bytes([random.randrange(0, 255) for _ in range(size)])

def generate_iv():
    return bytes([random.randrange(0, 255) for _ in range(AES.block_size)])

def encrypt_script(script, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    return cipher.encrypt(pad(script.encode(), AES.block_size))

def obfuscate_script(input_file, output_file):
    with open(input_file, 'rb') as f:
        original_script = f.read()
    key = generate_key()
    iv = generate_iv()
    encrypted_script = encrypt_script(original_script, key, iv)
    compressed_script = zipfile(encrypted_script)
    base64_encoded_key = base64.b64encode(key).decode()
    base64_encoded_iv = base64.b64encode(iv).decode()
    return f'[System.Security.Cryptography.AesManaged]::Create() | ForEach-Object {{{{base64_encoded_key}}}}} -Key $_.IV | ForEach-Object {{Invoke-Expression -ScriptBlock {{{{base64_encoded_script}}}}} | Where-Object Length}'

def main():
    parser = argparse.ArgumentParser(description='Obfuscates a script file')
    parser.add_argument('input', help='Input file path')
    parser.add_argument('output', help='Output file path')
    args = parser.parse_args()
    try:
        obfuscated_script = obfuscate_script(args.input, args.output)
        print(obfuscated_script)
    except Exception as e:
        print(f'An error occurred: {e}')
if __name__ == '__main__':
    main()
