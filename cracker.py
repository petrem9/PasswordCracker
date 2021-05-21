import hashlib

type_of_hash = str(input('enter the hash type: '))
file_path = str(input('enter path to the file: '))
hash_to_decrypt = str(input('enter hash to decrypt: '))

with open(file_path, 'r') as file:
    for line in file.readlines():
        if type_of_hash == 'md5':
            hash_object = hashlib.md5(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('found md5 password: ' + line.strip())
                exit(0)
        if type_of_hash == 'sha1':
            hash_object = hashlib.sha1(line.strip().encode())
            hashed_word = hash_object.hexdigest()
            if hashed_word == hash_to_decrypt:
                print('found sha1 password: ' + line.strip())
                exit(0)
    print('password not in file')