import dns.resolver

import tools.icmp_tools as icmp_tools

def Run_Dns_Lookup():

    domain = input("Enter a domain to resolve: ")   

    if not domain or ("." not in domain and len(domain.split())):
            print("****Invalid domain format.")
            return

    allowed_records = ["A","AAAA","CNAME","MX","NS","TXT","SOA"]

    record_selection = input("Select the type of record you want to consult (A, AAAA, CNAME, MX, TXT, SOA, all): ")                             

    if record_selection.upper() not in allowed_records and record_selection.upper() != "ALL":
        print("****Invalid selecction.")   
        return     
          

    try: 
        print(f"\nDomain: {domain.lower()}")        

        if record_selection.upper() == "ALL":
            
            for record_type in allowed_records: 

                try:
                
                    resolution = dns.resolver.resolve(domain.lower(), record_type)

                    if record_type == "A": #If statement for formatting after the "Domain: <domain.com>" print
                            print(f"{record_type} records:\n--------")
                            for record in resolution:
                                print(f"- {record}")
                    else:
                        print(f"\n{record_type} records:\n--------")
                        for record in resolution:
                            print(f"- {record}")
                except dns.resolver.NoAnswer:
                    print(f"\n***Error, the selected domain does not have any {record_type} record registered.")
            
        else:

            try:                          
                resolution = dns.resolver.resolve(domain.lower(), record_selection.upper())

                print(f"{record_selection.upper()} records:")
                for record in resolution:
                        print(f"- {record}")       

            except  dns.resolver.NoAnswer:
                    print(f"\n***Error, the selected domain does not have any {record_type} record registered.")

        print("\nQuery executed successfully\n")


    

    except dns.resolver.NXDOMAIN:
        print(f"***Error, The DNS query name {domain.lower()} does not exist.\n")
    
    except dns.resolver.Timeout:
        print("***Error: DNS query timed out.\n")

    except dns.resolver.NoNameservers:
        print("***Error: No DNS servers available\n")

def PRT_Record():
     
    Ip_To_Resolve = input(str("Enter an IPv4 (x.x.x.x; from 0 to 255) address to check it's PRT record (associated domain name): ")) #the dns.resolver.resolve_address function only accepts strings as an argument.
     
    try:
        if not Ip_To_Resolve:
            print("***Error, the entered IP address is blank.\n")        

        if icmp_tools.IP_address_format_validation(Ip_To_Resolve) == False:
            return

            
        PRT_Record_Resolution = dns.resolver.resolve_address(Ip_To_Resolve)

        print(f"PRT record for {Ip_To_Resolve} address:")
        for records in PRT_Record_Resolution:
            print(f"- {records}")

        
    except dns.resolver.NXDOMAIN:
        print(f"***Error, the IP {Ip_To_Resolve} does not have any PRT record registered.\n")
    
    except dns.resolver.Timeout:
        print("***Error: DNS query timed out.\n")
    
    except dns.resolver.NoNameservers:
        print("***Error: No DNS servers available\n")