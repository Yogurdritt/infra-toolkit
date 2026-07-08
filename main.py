while True:
   
    import tools.dns_lookup as dns_lookup

    print("====================\nInfra Toolkit\n====================\n")
    print("Available tools:\n")
    print("1. DNS Lookup:")
    print("Comming Soon...\n")

    seleccion = int(input("Select a tool from above: "))
    print("\n")

    match seleccion:
        case 1:
            dns_lookup.run_dns_lookup()
        case _:
            print("Not implemented yet")