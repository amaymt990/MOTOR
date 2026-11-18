import pyvisa

rm = pyvisa.ResourceManager("@py")

print("Available instruments:")
print(rm.list_resources())

rm.close()