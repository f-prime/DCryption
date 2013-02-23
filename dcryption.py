import random, sys

def encrypt():
    file = sys.argv[2]
    output = sys.argv[3]
    key = output+".key"
    with open(file, 'rb') as file:
        with open(output, 'wb') as output:
            with open(key, 'wb') as key:
                for letter in file.read():
                    letter = ord(letter)
                    random_key = random.randint(100,10000)
                    letter += random_key
                    output.write(str(letter)+" ")
                    key.write(str(random_key)+" ")

def decrypt():
    file = sys.argv[2]
    output = sys.argv[3]
    key = sys.argv[4]
    with open(file, 'rb') as file:
        with open(output, 'wb') as output:
            with open(key, 'rb') as key:
                file = file.read().split()
                key = key.read().split()
                for x in range(len(file)):
                    output.write(str(chr(int(file[x]) - int(key[x]))))


if __name__ == '__main__':
    help = """ 
        Usage

        Encrypting:
        
        python dcryption.py encrypt <file> <output file>

        Decrypting:

        python dcryption.py decrypt <file> <output file> <key file>

        """
    try:
        cmds = {"encrypt":encrypt, "decrypt":decrypt}[sys.argv[1]]()
    except IndexError:
        print help
