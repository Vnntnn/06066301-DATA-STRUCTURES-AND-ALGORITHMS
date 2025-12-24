def mm_recursion():
    """Recursive input to list and loop it until it's end"""
    user_input = input()
    if user_input == "End":
        return []
    return [int(user_input)] + mm_recursion()

def main():
    """Main function"""
    lst = mm_recursion()
    mi_n = min(lst)
    ma_x = max(lst)
    print("Max: " + str(ma_x))
    print("Min: " + str(mi_n))

main()
