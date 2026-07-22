from icmplib import ping
import icmplib.exceptions 

def Ping_feature():

    Address_To_Ping = input(str("Enter an IPv4 (x.x.x.x; from 0 to 255) address or hostname to ping: ")) #the dns.resolver.resolve_address function only accepts strings as an argument.  

    if Address_To_Ping == "":
        print("***Error, the entered address is blank.\n")

    elif isinstance(Address_To_Ping, str):

        try:            

            if "." in Address_To_Ping: #Case for when address is IPv4
                Separated_Ip_Numbers = Address_To_Ping.split(".")

                if len(Separated_Ip_Numbers) != 4:
                    print("***Error, the number of dot-separated segments that were introduced is not 4.\n")
                    return

                for Ip in Separated_Ip_Numbers:
                    if not Ip.isnumeric():
                        print("***Error, one or more of the IP segments are not numeric.\n")
                        return
                    if int(Ip) < 0 or int(Ip) > 255:
                        print("***Error, the IP segments are not between 0 and 255.\n")
                        return
                       
            host = ping(Address_To_Ping)
            print("\n")

            if not host.is_alive:
                print("Destination cannot be reached.")
            else:
                print(host)
        
        except icmplib.exceptions.NameLookupError:
            print("The hostname or address entered cannot be resolved.")
            
#        except icmplib.exceptions.DestinationUnreachable:
#            print("****Error, the hostname or address entered cannot be reached.")

