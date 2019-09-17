from Crypto.Cipher import AES
import base64

secret_key = '1234567890123456' # create new & store somewhere safe
a = []
def encrypt(msg):
    msg=msg.rjust(32)
    cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
    encoded = base64.b64encode(cipher.encrypt(msg))
    print (encoded)
    return encoded

def decrypt(msg):
    cipher = AES.new(secret_key,AES.MODE_ECB) # never use ECB in strong systems obviously
    decoded = cipher.decrypt(base64.b64decode(msg))
    print decoded.strip()
    print (decoded)
    return decoded


def validate_encrypt(ref_id):
    char=False
    capchar=False
    integer=False
    special=False
    length = len (ref_id)
    if (length ==12):
        for i in ref_id:
            if (i>="a" and i<="z"):
                char = True
            elif (i>="A" and i<="Z"):
                capchar = True
            elif ((i=="$") or (i=="@") or (i=="#")):
                special = True
            elif((i>="0") and (i<="9")) :
                integer = True
    else:
        print ("input is not valid ")
        return False
    if (capchar or char and integer):
        encrypt_id = encrypt(ref_id)
        decrypt_id = decrypt(encrypt_id)
        a.append(encrypt_id)
        print (a)
        return True
    else:
        return False

num_input = input ("Please enter how many refid you need to provide\n")
for i in range(num_input):
    ref_id = raw_input("Please enter the refid to contunue \n")
    if (validate_encrypt(ref_id) == True):
        print("Entered refid is fine")
    else:
        print("Entered refid is not good")


msg_text = 'test some plain text here'.rjust(32)

