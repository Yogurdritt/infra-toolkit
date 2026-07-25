import tools.dns_tools as dns_tools
import tools.icmp_tools as icmp_tools

def main():
        

    while True:

        print("====================\nInfra Toolkit\n====================\n")
        print("Available tools:\n")
        print("1. DNS Lookup")
        print("2. PRT Record lookup (Reverse DNS)")
        print("3. ICMP IPv4 ping")
        print("4. ICMP IPv4 traceroute")
        try:

            seleccion = int(input("Select a tool from above: "))
            print("\n")

            match seleccion:
                case 1:
                    dns_tools.run_dns_lookup()
                case 2:
                    dns_tools.ptr_record()    
                case 3:
                    icmp_tools.icmp_tools(3)                
                case 4:
                    icmp_tools.icmp_tools(4)        
                case _:
                    print("Not implemented yet")
        except ValueError:
            print("***The entered option is not a valid number.\n")

if __name__ == "__main__":
    main()