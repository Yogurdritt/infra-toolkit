import dns.resolver

import tools.icmp_tools as icmp_tools

def run_dns_lookup():

    domain = input("Enter a domain to resolve: ")   
    domain = domain.lower()

    if not domain or ("." not in domain and len(domain.split(".")) != 4):
            print("****Invalid domain format.")
            return

    allowed_records = ["A","AAAA","CNAME","MX","NS","TXT","SOA"]

    record_selection = input("Select the type of record you want to consult (A, AAAA, CNAME, MX, TXT, SOA, all): ")       
    record_selection = record_selection.upper()                      

    if record_selection not in allowed_records and record_selection != "ALL":
        print("****Invalid selecction.")   
        return     
          

    try: 
        print(f"\nDomain: {domain}")        

        if record_selection == "ALL":
            
            for record_type in allowed_records: 

                try:
                
                    resolution = dns.resolver.resolve(domain, record_type)

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
                resolution = dns.resolver.resolve(domain, record_selection)

                print(f"{record_selection} records:")
                for record in resolution:
                        print(f"- {record}")       

            except  dns.resolver.NoAnswer:
                    print(f"\n***Error, the selected domain does not have any {record_selection} record registered.")

        print("\nQuery executed successfully\n")


    

    except dns.resolver.NXDOMAIN:
        print(f"***Error, The DNS query name {domain} does not exist.\n")
    
    except dns.resolver.Timeout:
        print("***Error: DNS query timed out.\n")

    except dns.resolver.NoNameservers:
        print("***Error: No DNS servers available\n")

def ptr_record():
     
    ip_to_resolve = input(str("Enter an IPv4 (x.x.x.x; from 0 to 255) address to check it's PTR record (associated domain name): ")) #the dns.resolver.resolve_address function only accepts strings as an argument.
     
    try:
        if not ip_to_resolve:
            print("***Error, the entered IP address is blank.\n")     


        if "." in ip_to_resolve and len(ip_to_resolve.split(".")) == 4:   
            if icmp_tools.ip_address_format_validation(ip_to_resolve) == False:
                    return   
    
            ptr_record_resolution = dns.resolver.resolve_address(ip_to_resolve)

            print(f"PTR record for {ip_to_resolve} address:")
            for records in ptr_record_resolution:
                print(f"- {records}")
        else:
            print("***Error, the entered IP address is not in the x.x.x.x format.")

        
    except dns.resolver.NXDOMAIN:
        print(f"***Error, the IP {ip_to_resolve} does not have any PTR record registered.\n")
    
    except dns.resolver.Timeout:
        print("***Error: DNS query timed out.\n")
    
    except dns.resolver.NoNameservers:
        print("***Error: No DNS servers available\n")