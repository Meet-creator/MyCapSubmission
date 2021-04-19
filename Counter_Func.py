counter_var = input("Pls input a string : ")

def counter_func(string : str):
    out_dict = {}
    for char in string:
        if char in out_dict:
            out_dict[char] += 1
        else:
            out_dict[char] = 1
    return out_dict

print(counter_func(counter_var))
