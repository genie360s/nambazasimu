# nambazasimu/carrier_identifier.py

def identify_carrier(phone_number):
    """Identify the carrier of a given Tanzanian phone number"""
    #Check if the number is in either of the following correct formats "255XXXXXXXXX", "0XXXXXXXXX", "+255XXXXXXXXX"
    if phone_number.startswith("+255"):
        phone_number = phone_number[4:]
    elif phone_number.startswith("255"):
        phone_number = phone_number[3:]
    elif phone_number.startswith("0"):
        phone_number = phone_number[1:]

    #Defines carrier prefixes
    prefixes = {
        'Airtel' : ["68", "69", "78"],
        'Vodacom' : ["74", "75", "76"],
        'Tigo' : ["71", "65", "67"],
        'Zantel' : ["77"],
        'Halotel' : ["62"],
        'TTCL' : ["73"],
        'Smile' : ["66"]
    }
    
    #check the carrier
    for carrier, prefix_list in prefixes.items():
        if any(phone_number.startswith(prefix) for prefix in prefix_list):
            return carrier
        
    return "Unknown"