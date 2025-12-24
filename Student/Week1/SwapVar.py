"""Swap string in tuple"""
def convert_string_to_tuples(text_in):
    """Convert string to list"""
    values = text_in.strip('()').split(', ')
    return tuple(map(float, values))

def main(tup):
    """main function"""
    lst = convert_string_to_tuples(tup)

    print(f"({lst[1]}, {lst[0]})")

main(input())
