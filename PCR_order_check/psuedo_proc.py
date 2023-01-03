import os
import binascii

def convertInputToHex(input_str, req_length):
    converted_output = ""
    # convert input to hex
    # L has to be stripped due to some weird python convention
    # [2:] as the first two are the hex prefix, 0x
    try:
        converted_output += ((hex(int(input_str, 16)))[2:]).strip("L")
    except ValueError:
        return 0
    # if input is still too short, pad with zeroes
    # if too long, truncate to appropriate length
    diff_length = req_length - len(converted_output)
    if (diff_length > 0):
        while (diff_length > 0):
            converted_output += "0"
            diff_length -= 1
    return converted_output[:req_length]



print("="*50)
print("PROCESS 1")

psuedo_log = input("Enter a psuedo log: ")
psuedo_log = binascii.hexlify(psuedo_log.encode())
print(f"Hexlify log: {psuedo_log}")

processed_psuedo_log = convertInputToHex(psuedo_log, 64) 
#print(f"Psuedo log: {psuedo_log}")
print(f"Processed log: {processed_psuedo_log}") 

os.system(f"tpm2 pcrextend 23:sha256={processed_psuedo_log}")
os.system("tpm2  pcrread sha256:23 ")