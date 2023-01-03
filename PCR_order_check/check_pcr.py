import os


ans = "0xF01401C3F89652D2FDEEC9DC609F4971075395D17D4D3DFD8CE0B4F42F2266E5"

pcr_23 = os.popen("tpm2 pcrread sha256:23").read().replace("\n","").split(":")[-1].strip()


print("Checking PCR register 23 in sha256 bank") 
print(pcr_23)
print(ans)
if pcr_23 == ans :
  print("=================================")
  print("|                               |")
  print("|       PCR check passed!       |")
  print("|                               |")
  print("=================================")
else:

  print("=================================")
  print("|                               |")
  print("|     PCR check failed QAQ      |")
  print("|                               |")
  print("=================================")
