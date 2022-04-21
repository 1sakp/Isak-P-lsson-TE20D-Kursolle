import ast

def file_read():
    with open ("C:\\Users\\isak.palsson1\\Documents\\code workshop\\Programering 1\\genetic_code.txt", "r") as file:
        content = file.read()
        dictionary = ast.literal_eval(content)
        ask = input("kodon eller aminosyror eller protein:    ")
        if "kodon" in ask.lower():
            print(dictionary.keys())
        elif "aminosyror" in ask.lower():
            print(dictionary.values())
        elif "protein" in ask.lower():
            listan = dictionary.values()
            print("".join(listan))
        
        file.close()
        
file_read()