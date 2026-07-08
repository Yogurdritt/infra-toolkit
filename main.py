#while True:
   
import dns_lookup

print("====================\nInfra Toolkit\n====================\n")
print("Available tools:\n")
print("1. DNS Lookup:")
print("Comming Soon...")

seleccion = int(input("Select a tool from above: "))

match seleccion:
    case 1:
        dns_lookup.run_dns_lookup()
    case _:
        print("Not implemented yet")