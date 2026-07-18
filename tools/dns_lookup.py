import dns.resolver

def Run_Dns_Lookup():

    domain = input("Enter a domain to resolve: ")   

    if not domain or "." not in domain:
            print("****Invalid domain format.")
            return
    
    domain_to_resolve = domain.lower()

    allowed_records = ["A","AAAA","CNAME","MX","NS","TXT","SOA"]

    print("available records: \n","  A. AAAA. CNAME. MX. TXT. SOA\n")

    record_selection = input("Select the type of record you want to consult, or if you want to consult all (<type>/all): ")                             

    if record_selection.upper() not in allowed_records and record_selection.upper() != "ALL":
        print("****Invalid selecction.")   
        return     
          

    try: 
        print(f"\nDomain: {domain_to_resolve}")        

        if record_selection.upper() == "ALL":
             for record_type in allowed_records: 

                try:
                    resolution = dns.resolver.resolve(domain_to_resolve, record_type)

                    if record_type == "A": #If statement for formatting after the "Domain: <domain.com>" print
                         print(f"---------\n{record_type} records:")
                         for record in resolution:
                            print(f"- {record}")
                    else:
                        print(f"\n{record_type} records:")
                        for record in resolution:
                            print(f"- {record}")
                
                except  dns.resolver.NoAnswer:
                     print(f"***Error, the selected domain does not have any {record_type} record registered.\n")
                
        
        else:
                          
            resolution = dns.resolver.resolve(domain_to_resolve, record_selection.upper())

            print(f"{record_selection.upper()} records:")
            for record in resolution:
                    print(f"- {record}")
            

        print("\nQuery executed successfully\n")


    except dns.resolver.NXDOMAIN:
        print(f"***Error, The DNS query name {domain_to_resolve} does not exist.\n")
    
    except dns.resolver.Timeout:
        print("***Error: DNS query timed out.\n")

    except dns.resolver.NoNameservers:
        print("***Error: No DNS servers available\n")

def PRT_Record():
     
    Ip_To_Resolve = input(str("Enter an IPv4 (x.x.x.x; from 0 to 255) address to check it's PRT record (associated domain name): ")) #the dns.resolver.resolve_address function only accepts strings as an argument.
     
    try:
        if Ip_To_Resolve == "":
            print("***Error, the entered IP address is blank.\n")

        elif isinstance(Ip_To_Resolve, str):

            Separated_Ip_Numbers = Ip_To_Resolve.split(".")

            if len(Separated_Ip_Numbers) != 4:
                print("***Error, the number of dot-separated segments that were introduced is not 4.\n")
                return

            for Ip in Separated_Ip_Numbers:
                if not Ip.isnumeric():
                    print("***Error, the IP segments are not numeric.\n")
                    return
                if int(Ip) < 0 or int(Ip) > 255:
                    print("***Error, the IP segments are not between 0 and 255.\n")
                    return
                
            PRT_Record_Resolution = dns.resolver.resolve_address(Ip_To_Resolve)

            print(f"PRT record for {Ip_To_Resolve} address:")
            for records in PRT_Record_Resolution:
                print(f"- {records}")

        else: 
            print("***Error, provided IP format is not valid.\n")
        
    except dns.resolver.NXDOMAIN:
        print(f"***Error, the IP {Ip_To_Resolve} does not have any PRT record registered.\n")
    
    except dns.resolver.Timeout:
        print("***Error: DNS query timed out.\n")
    
    except dns.resolver.NoNameservers:
        print("***Error: No DNS servers available\n")
        
    
     
    

     