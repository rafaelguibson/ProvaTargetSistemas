def inverter_string(s):
    if len(s) <= 1:
        return s
    return inverter_string(s[1:]) + s[0]

def main():

    string_original = input("Digite uma string: ")

    string_invertida = inverter_string(string_original)

    print("String invertida:", string_invertida)

if __name__ == "__main__":
    main()
