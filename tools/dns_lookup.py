import dns.resolver

def Run_Dns_Lookup():

    domain = input("Enter a domain to resolve: ")   

    if not domain or "." not in domain:
            print("Invalid domain format.")
            return
    
    domain_to_resolve = domain.lower()

    allowed_records = ["A","AAAA","CNAME","MX","NS","TXT","SOA"]

    print("available records: \n","  A. AAAA. CNAME. MX. TXT. SOA\n")

    record_selection = input("Select the type of record you want to consult, or if you want to consult all (<type>/all): ")                             

    if record_selection.upper() not in allowed_records and record_selection.upper() != "ALL":
        print("Invalid selecction.")   
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
                     print(f"Error, the selected domain does not have any {record_type} record registered.\n")
                
        
        else:
                          
            resolution = dns.resolver.resolve(domain_to_resolve, record_selection.upper())

            print(f"{record_selection.upper()} records:")
            for record in resolution:
                    print(f"- {record}")
            

        print("\nQuery executed successfully\n")


    except dns.resolver.NXDOMAIN:
        print(f"Error, The DNS query name {domain_to_resolve} does not exist.\n")
    
    except dns.resolver.Timeout:
        print("Error: DNS query timed out.\n")

    except dns.resolver.NoNameservers:
        print("Error: No DNS servers available\n")

def Ip_Address_Resolver():
     return