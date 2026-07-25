import icmplib.exceptions 
import subprocess
import platform

from icmplib import ping, traceroute

def IP_address_format_validation(ip_add):

    Separated_Ip_Numbers = ip_add.split(".")    

    for Ip in Separated_Ip_Numbers:
        if not Ip.isnumeric():
            print(f"***Error, one or more of the IP segments are not numeric ({Ip}).\n")
            return False
        if int(Ip) < 0 or int(Ip) > 255:
            print(f"***Error, one or more of the the IP segments are not between 0 and 255 ({Ip}).\n")
            return False 

def Ping_Feature(Address_To_Validate):   
     
    try:

        if "." in Address_To_Validate and len(Address_To_Validate.split(".")) == 4:   
            if IP_address_format_validation(Address_To_Validate) == False:
                 return

        response = ping(Address_To_Validate)
        
        if not response.is_alive:
            print("Destination cannot be reached.")
        else:
            print(response)

    except icmplib.exceptions.NameLookupError:
        print("The hostname or address entered cannot be resolved.")

    except icmplib.exceptions.DestinationUnreachable:
        print("Destination cannot be reached.")

def Traceroute_feature(Address_To_Validate):

    if "." in Address_To_Validate and len(Address_To_Validate.split(".")) == 4:   
        if IP_address_format_validation(Address_To_Validate) == False:
            return
    os_name = platform.system()
    subprocess.run(["tracert", Address_To_Validate] if os_name == "Windows" else ["traceroute", Address_To_Validate])
 

def ICMP_tools(selection): # 3. ICMP IPv4 ping; 4. ICMP IPv4 traceroute

    match selection:
        case 3:
              option_print = "ping"
        case 4:
              option_print = "trace over route"

    Address_To_Validate = input(f"Enter an IPv4 (x.x.x.x; from 0 to 255) address or hostname to {option_print}: ") #the dns.resolver.resolve_address function only accepts strings as an argument.  

    if Address_To_Validate == "":
        print("***Error, the entered address is blank.\n")
        return  

    match selection:
        case 3: #Ping
                Ping_Feature(Address_To_Validate)
        case 4: #Traceroute
                Traceroute_feature(Address_To_Validate)



