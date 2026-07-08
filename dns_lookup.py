import dns.resolver

def run_dns_lookup():

    domain = input("Enter a domain to resolve: ")   

    if not isinstance(domain, str) or not domain.endswith(".com"):
            print("Error, entered domain is not in the name.com format")
            return
    
    domain_to_resolve = domain.lower()

    try: 

        

        resolution = dns.resolver.resolve(domain_to_resolve)
        
        for x in resolution:
            print(x)

    except dns.resolver.NXDOMAIN:
        print(f"Error, The DNS query name {domain_to_resolve} does not exist.")




    
