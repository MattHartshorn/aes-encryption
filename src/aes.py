import sys
import argparse
import base64
import aescypher
import keygenerator
import actions

# Run execution
def main(args = None):
    parser = getParser()
    run(parser, parser.parse_args())

def run(parser, args):
    if (args.cmd == "enc" or args.cmd == "dec"):
        cypher(args, args.cmd == "enc")
    elif (args.cmd == "keygen"):
        keygen(args)
    else:
        parser.print_help()


# Encrypt & decrypt methods
def cypher(args, isEncrypt):
    cypher_validate_args(args)
    ofile = args.ofile[0] if isinstance(args.ofile, list) else args.ofile

    try:
        try:
            # Load data
            mode = args.mode[0] if isinstance(args.mode, list) else args.mode
            key = cypher_loadkey(args)
            msg = cypher_loadmsg(args, isEncrypt)
            iv = cypher_loadIV(args, mode)

            # Encrypt/decrypt
            output = cypher_execute(msg, key, mode, iv, isEncrypt)
        except Exception as e:
            cypher_write(args, "".encode(), ofile, isEncrypt)
            error(e)

        # Write data
        cypher_write(args, output, ofile, isEncrypt)
    except IOError as e:
        error(e)

def cypher_validate_args(args):
    requiredArgs = []
    if (args.key == None and args.keyOpt == None):
        requiredArgs.append("key")
    if (args.ifile == None and args.input == None):
        requiredArgs.append("ifile/message")
    if (args.key == None and args.keyOpt[0] == None):
        requiredArgs.append("")
    if (len(requiredArgs) > 0):
        error("the following arguments are required: {0}".format(", ".join(requiredArgs)))

def cypher_loadkey(args):
    keyfile = args.key if args.key != None else args.keyOpt[0]
    return bytes.fromhex(readText(keyfile))
        
def cypher_loadmsg(args, isEncrypt):
    filename = args.input[0] if args.input != None else args.ifile
    return readText(filename) if isEncrypt else readBase64(filename)

def cypher_loadIV(args, mode):
    if (mode == None or mode == "ECB"): return None

    ivfile = "../data/iv.txt" if args.iv == None else args.iv[0]
    return bytes.fromhex(readText(ivfile))

def cypher_write(args, output, filename, isEncrypt):
    if (isEncrypt):
        output = base64.b64encode(output)

    if (filename != None):
        write(output, filename)
    elif (output != ""):
        print(output.decode("utf-8"))

def cypher_execute(msg, key, mode, iv, isEncrypt):
    if (isEncrypt):
        if (mode == None):
            return aescypher.encrypt(msg.encode("utf-8"), key)
        else:
            return aescypher.encrypt(msg.encode("utf-8"), key, mode, iv)
    else:
        if (mode == None):
            return aescypher.decrypt(msg, key)
        else:
            return aescypher.decrypt(msg, key, mode, iv)
    

# Key gen methods
def keygen(args):
    ofile = args.output[0] if args.output != None else args.ofile
    try:
        try:
            # Generate key
            key = keygenerator.generate(args.size).hex()
        except Exception as e:
            keygen_write(args, key, ofile)
            error(e)

        keygen_write(args, key, ofile)

    except IOError as e:
        error(e)

def keygen_write(args, key, filename):
    try:
        # Attempt to write the file
        if (filename != None):
            write(key, filename, False)
        elif (key != ""):
            # Print key
            print(key)
    except Exception as e:
        error(e)


# Read/write methods
def readText(filename, decode = True):
    with open(filename, "rb") as fs:
        content = fs.read()
        if (decode): return content.decode("utf-8")
        return content

def readBase64(filename):
    with open(filename, "rb") as fs:
        content = fs.read()
        return base64.b64decode(content)

def write(content, filename, binary = True):
    with open(filename, "wb" if binary else "w") as fs:
        fs.write(content)


# Print errors
def error(content):
    print("error: {0}".format(content))
    sys.exit(1)

# Create parser
def getParser():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument("-h", "--help", help="Shows this help message or command help and exit", nargs="?", const="", default="", action=actions.HelpAction, metavar="CMD")
    subparsers = parser.add_subparsers(help="Commands", dest="cmd")
    setupCypherParser(subparsers, "enc", "Encrypts a message using the provided key", "encrypted")
    setupCypherParser(subparsers, "dec", "Decrypts a message using the provided key", "decrypted")
    setupKeyGenParser(subparsers)
    return parser

def setupCypherParser(subparsers, title, help_txt, func):
    parser = subparsers.add_parser(title, help=help_txt)
    parser.add_argument("-k", "--key", dest="keyOpt", help="Encryption key or filepath", nargs=1, metavar="KEY")
    parser.add_argument("-m", "--mode", dest="mode", help="Encryption mode", nargs=1, metavar="MODE", choices=["ECB", "CBC"], default="ECB")
    parser.add_argument("-i", "--ifile", dest="input", help="Filepath of the message to be {0}".format(func), nargs=1, metavar="FILE")
    parser.add_argument("-o", "--ofile", dest="output", help="Filepath the output is written to", nargs=1, metavar="FILE")
    parser.add_argument("-v", "--ivfile", dest="iv", help="Filepath of the initialization vector", nargs=1, metavar="FILE")
    parser.add_argument("key", help="Encryption key or filepath", nargs="?")
    parser.add_argument("ifile", help="Filepath of the message to be {0}".format(func), nargs="?")
    parser.add_argument("ofile", help="Filepath the output is written to", nargs="?")

def setupKeyGenParser(subparsers):
    parser = subparsers.add_parser("keygen", help="Generates a pseudorandom encryption key of size 128, 192, or 256")
    parser.add_argument("-o", "--ofile", dest="output", help="Filepath the key is written to", nargs=1, metavar="FILE")
    parser.add_argument("ofile", help="Filepath the key is written to", nargs="?")
    parser.add_argument("size", help="The size of the key, default in bits", type=int, nargs="?", default=256, choices=[128, 192, 256])




# Execute the program
if (__name__ == "__main__"):
    main(sys.argv)