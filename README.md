# Cryptic PowerShell Obscuration (CPSO)

Cryptic PowerShell Obscuration (CPSO) is a Python script that performs advanced obfuscation and compression techniques on PowerShell scripts, converting them into an encrypted and compressed form. It creates a new PowerShell script file that, when executed, will decrypt and decompress the original script back to its original state for execution.

## Key Features:
* **AES Encryption:** CPSO utilizes AES encryption in Cipher Block Chaining (CBC) mode, which ensures the confidentiality of data during transmission or storage. The AES key and initialization vector (IV) used for encryption are randomly generated and base64 encoded for easy integration into the PowerShell script.
* **Compression:** To further enhance the security of the encrypted script, CPSO compresses it using zlib's built-in compression function before encoding and embedding it in the final output file. This additional layer of obfuscation ensures that even if an attacker manages to obtain the encoded PowerShell script file, they would still need a way to decrypt and decompress it to understand its contents.
* **PowerShell Integration:** The output of CPSO is a new PowerShell script file that contains the base64-encoded AES key, IV, and compressed encrypted script in a format designed for easy integration into existing PowerShell environments. This allows users to execute the original, obfuscated script while ensuring its confidentiality and maintaining a high level of security throughout the process.
* **Advanced Obscuration:** CPSO combines advanced cryptographic techniques with compression methods to create an encrypted and compressed version of your PowerShell scripts that is virtually impossible to decipher without the correct key and context. This ensures that even if an attacker gains unauthorized access, they will be unable to exploit the script or extract sensitive information from it.
* **Easy to Use:** CPSO is designed with simplicity in mind, providing users with a straightforward command-line interface for executing the obfuscation process. This allows users of all skill levels to protect their PowerShell scripts without the need for extensive technical knowledge.
* **Platform Independent:** CPSO is built on top of Python, a widely used and platform-independent programming language. This ensures that users can easily run the script on any operating system with a working Python installation.

## Installation:
To install CPSO, follow these simple steps:
1. Clone or download this repository to your local machine.
2. Navigate to the directory containing the cloned repository using your preferred terminal/command prompt.
3. Install the required dependencies by running `pip install -r requirements.txt` in the command line.
4. Once installed, you can use CPSO as a standalone script or incorporate it into your existing Python projects.

## Usage:
To use CPSO, simply run the following command in your terminal/command prompt:
```bash
python cpso.py <input_file> <output_file>
