import tools.dns_tools as dns_tools
import tools.icmp_tools as icmp_tools


while True:
       

    print("====================\nInfra Toolkit\n====================\n")
    print("Available tools:\n")
    print("1. DNS Lookup")
    print("2. PRT Record lookup (Reverse DNS)")
    print("3. ICMP IPv4 ping")
    print("4. ICMP IPv4 traceroute")
    print("Comming Soon...\n")
    try:

        seleccion = int(input("Select a tool from above: "))
        print("\n")

        match seleccion:
            case 1:
                dns_tools.Run_Dns_Lookup()
            case 2:
                dns_tools.PRT_Record()    
            case 3:
                icmp_tools.ICMP_tools(3)                
            case 4:
                icmp_tools.ICMP_tools(4)        
            case _:
                print("Not implemented yet")
    except ValueError:
        print("***The entered option is not a valid number.\n")