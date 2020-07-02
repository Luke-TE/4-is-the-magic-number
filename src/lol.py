import sys
from num2words import num2words

def update_list(x):
    current_list = [x]
    while x != 4:
        name = num2words(x)
        fixed_name = name.replace(' ', '')
        fixed_name = name.replace(',', '')
        fixed_name = name.replace('-', '')
        x = len(fixed_name)
        current_list = current_list + [x]
    return current_list

if __name__ == "__main__":
    print(",".join(map(str,update_list(sys.argv[1]))))
