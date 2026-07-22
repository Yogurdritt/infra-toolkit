while True:
   
    import tools.dns_lookup as dns_lookup

    print("====================\nInfra Toolkit\n====================\n")
    print("Available tools:\n")
    print("1. DNS Lookup")
    print("2. PRT Record lookup (Reverse DNS)")
    print("Comming Soon...\n")

    seleccion = int(input("Select a tool from above: "))
    print("\n")

    match seleccion:
        case 1:
            dns_lookup.Run_Dns_Lookup()
        case 2:
            dns_lookup.PRT_Record()            
        case _:
            print("Not implemented yet")