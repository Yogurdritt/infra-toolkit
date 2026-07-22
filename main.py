while True:
   
    import tools.dns_tools as dns_tools
    import tools.icmp_tools as icmp_tools

    print("====================\nInfra Toolkit\n====================\n")
    print("Available tools:\n")
    print("1. DNS Lookup")
    print("2. PRT Record lookup (Reverse DNS)")
    print("3. ICMP IPv4 ping")
    print("Comming Soon...\n")

    seleccion = int(input("Select a tool from above: "))
    print("\n")

    match seleccion:
        case 1:
            dns_tools.Run_Dns_Lookup()
        case 2:
            dns_tools.PRT_Record()    
        case 3:
            icmp_tools.Ping_feature()                
        case _:
            print("Not implemented yet")