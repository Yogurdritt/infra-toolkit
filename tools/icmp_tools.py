import icmplib.exceptions 
import subprocess
import platform

from icmplib import ping, traceroute

def ip_address_format_validation(ip_add):

    separated_ip_numbers = ip_add.split(".")    

    for octet in separated_ip_numbers:
        if not octet.isnumeric():
            print(f"***Error, one or more of the IP segments are not numeric ({octet}).\n")
            return False
        if int(octet) < 0 or int(octet) > 255:
            print(f"***Error, one or more of the the IP segments are not between 0 and 255 ({octet}).\n")
            return False 

def ping_feature(address_to_validate):   
     
    try:

        if "." in address_to_validate and len(address_to_validate.split(".")) == 4:   
            if ip_address_format_validation(address_to_validate) == False:
                 return

        response = ping(address_to_validate)
        
        if not response.is_alive:
            print("Destination cannot be reached.")
        else:
            print(response)

    except icmplib.exceptions.NameLookupError:
        print("The hostname or address entered cannot be resolved.")

    except icmplib.exceptions.DestinationUnreachable:
        print("Destination cannot be reached.")

def traceroute_feature(address_to_validate):

    if "." in address_to_validate and len(address_to_validate.split(".")) == 4:   
        if ip_address_format_validation(address_to_validate) == False:
            return
    os_name = platform.system()
    subprocess.run(["tracert", address_to_validate] if os_name == "Windows" else ["traceroute", address_to_validate])
 

def icmp_tools(selection): # 3. ICMP IPv4 ping; 4. ICMP IPv4 traceroute

    match selection:
        case 3:
              option_print = "ping"
        case 4:
              option_print = "trace over route"

    address_to_validate = input(f"Enter an IPv4 (x.x.x.x; from 0 to 255) address or hostname to {option_print}: ") #the dns.resolver.resolve_address function only accepts strings as an argument.  

    if address_to_validate == "":
        print("***Error, the entered address is blank.\n")
        return  

    match selection:
        case 3: #Ping
                ping_feature(address_to_validate)
        case 4: #Traceroute
                traceroute_feature(address_to_validate)



