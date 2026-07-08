#while True:
   
print("====================\nInfra Toolkit\n====================\n")
print("Available tools:\n")
print("1. DNS Lookup:")
print("Comming Soon...")

seleccion = int(input("Select a tool from above: "))

match seleccion:
    case 1:
        print("DNS Lookup working")
    case _:
        print("Not implemented yet")