import re
import sys

def main():
    ip = input("Ipv4 address:  ")

    print(validate(ip))    



def validate(ip):
    parts = ip.split(".")

    if len(ip) != 4:
        return False
    
    for part in parts:

        if not part.isdigit():
            return False
        
        num = int(part)

        if num < 0 or num > 255:
            return False
        
    return True


if __name__ == "__main__":
    main()
         
