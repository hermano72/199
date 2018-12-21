
# 555-822-5959
#1545665

def is_phone_number(text):
  if len(text) != 12:
    return False
  
  if not text[:3].isdecimal():
    return False
  
  if text[3] != '-':
    return False
  
  if not text[4:7].isdecimal():
    return False
  
  if text[7] != '-':
    return False
  
  if not text[8:].isdecimal():
    return False
  
  return True



# -------------------------
message = "My phone Number is 555-228-5358\n\
office number is 874-568-9636\n\
My second phon number is 412-588-9601"

for i in range(len(message)):
  chunk = message[i:i+12]
  
  if is_phone_number(chunk):
    print("Found phone number:", chunk)



# -------------------------
input("\ndone!..")