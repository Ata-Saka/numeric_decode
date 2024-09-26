def menu():
    print("Decoding Menu")
    print("-------------")
    print("1. Decode hexadecimal")
    print("2. Decode binary")
    print("3. Convert binary to hexadecimal")
    print("4. Quit")
    ans = int(input("Please enter an option: "))
    return ans 

def hex_string_decode(hexx):
    let_val = {"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
    if hexx[0] =="0" and hexx[1] =="x":
        hexx = hexx[2:]
    bit_index = len(hexx)-1
    decimal_num=0
    
    for char in hexx:
        if char.isdigit():
            decimal_num += int(char)*(16**(bit_index))
        else:
            decimal_num+= let_val[char.upper()]*(16**(bit_index))
        bit_index -=1

    return decimal_num


def binary_string_decode(binary):
    if binary[0] == "0" and binary[1] == "b":
        binary = binary[2:]
    bit_index = len(binary)-1
    decimal_num=0

    for bin in binary:
        decimal_num += int(bin)*(2**(bit_index))
        bit_index -=1
    return decimal_num

def binary_to_hex(binary):
    decimal_num = binary_string_decode(binary)
    return hex(decimal_num)


if __name__ == "__main__":
    while True:
        ans = menu()
        if ans == 1:
            hexx = input("Please enter the numeric string to convert: ")
            result = hex_string_decode(hexx)
            print(f"Result: {result}")

        elif ans == 2:
            binary = input("Please enter the numeric string to convert: ")
            result = binary_string_decode(binary)
            print(f"Result: {result}")
    
        elif ans == 3:
            binary = input("Please enter the numeric string to convert: ")
            result = binary_to_hex(binary)
            print(f"Result: {result}")

        elif ans ==4:
            print("Goodbye!")
            break

        else:
            pass
    



