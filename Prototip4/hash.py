import hashlib

def hash_text(text):

    return hashlib.md5(text.encode('utf-8')).hexdigest()

print(hash_text("12345"))  