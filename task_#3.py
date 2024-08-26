import re 

def normalize_phone(phone_number) :
     
    pattern =  r"[^\d]"
    corrected_number = re.sub(pattern, '', phone_number)
    
    if corrected_number.startswith('38') :
        corrected_number = "+" + corrected_number
    else :
        corrected_number = "+38"+ corrected_number
    
    return corrected_number
    
