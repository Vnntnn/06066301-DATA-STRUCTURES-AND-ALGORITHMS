"""Hacker Changon"""
def cnt_recursion(f_num, l_num):
    """Counting number without Loop"""
    if f_num == l_num:
        print(f_num)
        return
    print(f_num)
    if f_num < l_num:
        cnt_recursion(f_num + 1, l_num)
    else:
        cnt_recursion(f_num - 1, l_num)

cnt_recursion(int(input()), int(input()))
