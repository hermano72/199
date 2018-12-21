def is_phone_number(text):
  if len(text) != 12:
    return False
  
  return True



# -------------------------
message = "My phone Number is 555-228-5358\n\
office number is 874-568-9636\n\
My second phon number is 412-588-96-01"

print(is_phone_number(message))



# -------------------------
input("\ndone!..")