# One Time Pad Encryption

**Author:** Matt Hartshorn

This project illustrates the use of [AES Encryption](https://en.wikipedia.org/wiki/Advanced_Encryption_Standard). The project is capable of creating a randomly generated encryption key, encrypting, and decrypting messages. This project utilizes file IO to read and write the input and output of the given commands. Any errors will be printed to the terminal and output files will be written as an empty file.

The input and output text will be encoded/decoded as UTF-8 and Base64. While encrypting a message the output will be encoded as Base64 and decoded as Bas64 when decrypting.



# Environment

The following information denotes the environment setup in which the code was written and tested.

**Language:** Python 3.5+

**Operating System:** Windows 10



# Prerequisites

The Python 3.5+ command line interface must be installed on the device. The download for Python can be found [here](https://www.python.org/downloads/).

**Cryptography** - Python encryption library
```bash
> pip install cryptography
```



# Usage
Navigate to the source directory `/src`. Run Python followed by the script `aes.py` then specify which command you want to run and any required arguments.

```bash
> cd ./src
> python aes.py <command> [args...]
```


# Commands

## Encyrpt
**Name:** `enc`

**Description:** Encrypts the provided plaintext using the given secret key. The encrypted text is written to the given output filepath. If encryption or reading fails, an empty output file will be written. The output is encoded in Base64.

**Options:**

| Char | Verbose     | Arg                     | Description
| ---- | ----------- | ----------------------- | ----------------------------------------- |
| `-k` | `--key`     | `KEY`                   | Encryption key or filepath
| `-m` | `--mode`    | `ECB`, `CBC`            | Encryption mode 
| `-i` | `--ifile`   | `FILE`                  | Filepath of the message to be encrypted
| `-o` | `--ofile`   | `FILE`                  | Filepath the output is written to
| `-v` | `--ivfile`  | `FILE`                  | Filepath of the initialization vector

**Mode:**

`ECB`: Electronic Code Book

`CBC` : Cipher Block Chaining

**Arguments:**

| Argument | Required | Description
| -------- | -------- | ---------------------------------------- |
| `key`    | No*      | Encryption key or filepath
| `ifile`  | No*      | Filepath of the message to be encrypted
| `ofile`  | No       | Filepath the output is written to

No* : Argument is not required if it's `option` counterpart is provided

**Usage:**
```bash
enc [-k KEY] [-m MODE] [-i FILE] [-o FILE] [-v FILE] [key] [ifile] [ofile]
```

**Examples:**
```bash
> python aes.py enc ../data/key ../data/plaintext ../data/cyphertext
```



## Decrypt
**Name:** `dec`

**Description:** Decrypts the provided cyphertext using the given secret key. The decrypted text is written to the given output filepath. If decryption or reading fails, an empty output file will be written. The input is decoded as Base64 and the output is encoded as UTF-8.

**Options:**

| Char | Verbose     | Arg                     | Description
| ---- | ----------- | ----------------------- | ------------------------------------------ |
| `-k` | `--key`     | `KEY`                   | Encryption key or filepath
| `-m` | `--mode`    | `ECB`, `CBC`            | Encryption mode 
| `-i` | `--ifile`   | `FILE`                  | Filepath of the message to be encrypted
| `-o` | `--ofile`   | `FILE`                  | Filepath the output is written to
| `-v` | `--ivfile`  | `FILE`                  | Filepath of the initialization vector

**Mode:**

`ECB`: Electronic Code Book

`CBC` : Cipher Block Chaining

**Arguments:**

| Argument | Required | Description
| -------  | -------- | ------------------------------ |
| `key`    | No*      | Encryption key or filepath
| `ifile`  | No*      | Filepath of the message to be encrypted
| `ofile`  | No       | Filepath the output is written to

No* : Argument is not required if it's `option` counterpart is provided

**Usage:**
```bash
dec [-k KEY] [-m MODE] [-i FILE] [-o FILE] [-v FILE] [key] [ifile] [ofile]
```

**Examples:**
```bash
> python aes.py dec ../data/key ../data/cyphertext ../data/plaintext
```


## Generate Key
**Name:** `keygen`

**Description:** Creates a randomly generated key based on the provided number of bits. In order to create a useable key, the number of bits in the key must be divisible by 8. This allows the key to be properly divided in 8-bit sized bytes.  

**Options:**

| Char | Verbose       | Arg    | Description
| ---- | ------------- | ------ | --------------------------------------- |
| `-o` | `--ofile`     | `FILE` | Filepath the key is written to

**Arguments:**

| Argument | Required | Description
| -------- | -------- | ---------------------------------------- |
| `size`   | Yes      | The size of the key in bits, 128, 192, or 256 (default)
| `ofile`  | No       | Filepath the key is written to

**Usage:**
```bash
keygen [-o FILE] [ofile] [size]
```

**Example:**
```bash
> python otp.py keygen ../data/key 128
```

# License

Copyright 2018 Matthew Hartshorn

[MIT License](./LICENSE)