### Set the correct state
import os
import binascii
import hashlib

os.system("tpm2_startup -c")

file_correct = "correct_boot.log"
file_wrong = "wrong_boot.log"
with open(file_correct, 'r') as f1, open(file_wrong, 'r') as f2:
    lines = [line[15:].strip() for line in f1.readlines()[:100]]
    concat_str_correct = "".join(lines)
    lines = [line[15:].strip() for line in f2.readlines()[:100]]
    concat_str_wrong = "".join(lines)
    concat_str_correct = hashlib.sha256(concat_str_correct.encode('utf-8')).hexdigest()
    concat_str_wrong = hashlib.sha256(concat_str_wrong.encode('utf-8')).hexdigest()
    os.system(f'tpm2_pcrextend 10:sha256={concat_str_correct}')
    print(os.system("tpm2  pcrread sha256:10 "))
    os.system(f'tpm2_pcrextend 11:sha256={concat_str_wrong}')
    print(os.system("tpm2  pcrread sha256:11 "))

