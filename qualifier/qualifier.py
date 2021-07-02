from typing import Any, List, Optional

def create_lined_string(char_list, break_list):
    # char_list = [start, linefill, break, end]
    re_string = ''
    re_string += char_list[0]
    for i in range(len(break_list)-1):
        re_string += break_list[i]*char_list[1] + char_list[2]
    re_string += break_list[-1]*char_list[1] + char_list[3]

    re_string += '\n'
    return re_string

def create_char_string(char_list, break_list, centered):
    # char_list = [start, linefill, break, end]
    # linefill = row to print
    char_list[1] = list(map( str, char_list[1]))
    re_string = ''
    re_string += char_list[0]
    if centered:
        for i in range(len(break_list)-1):
            balance = break_list[i] - len(char_list[1][i])
            if balance%2 == 0:
                balance = balance//2
                re_string += (balance)*(' ') + char_list[1][i] + (balance)*(' ') + char_list[2]
            else:
                balance = balance//2
                re_string += (balance)*(' ') + char_list[1][i] + (balance+1)*(' ') + char_list[2]
        
        balance = break_list[-1] - len(char_list[1][-1])
        if balance%2 == 0:
            balance = balance//2
            re_string += (balance)*(' ') + char_list[1][-1] + (balance)*(' ') + char_list[2]
        else:
            balance = balance//2
            re_string += (balance)*(' ') + char_list[1][-1] + (balance+1)*(' ') + char_list[2]

    else:
        for i in range(len(break_list)-1):
            re_string += ' ' + char_list[1][i] + (break_list[i] - len(char_list[1][i]) -1)*(' ') + char_list[2]
        re_string += ' ' + char_list[1][-1] + (break_list[-1] - len(char_list[1][-1]) -1)*(' ') + char_list[3]
    re_string += '\n'
    return re_string

def val(i):
    i = list(map( str, i))
    i = list(map( len, i ))
    return max(i)+2

def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    """
    :param rows: 2D list containing objects that have a single-line representation (via `str`).
    All rows must be of the same length.
    :param labels: List containing the column labels. If present, the length must equal to that of each row.
    :param centered: If the items should be aligned to the center, else they are left aligned.
    :return: A table representing the rows passed in.
    """
    print_char = ['│', '─', '┌', '┬', '┐', '├', '┼', '┤', '└', '┴', '┘']
    #              0,   1,   2,   3,   4,   5,   6,   7,   8,   9,   10

    final_string = ''
    top_line_list = [print_char[2], print_char[1], print_char[3], print_char[4]]
    middle_line_list = [print_char[5], print_char[1], print_char[6], print_char[7]]
    bottom_line_list = [print_char[8], print_char[1], print_char[9], print_char[10]]
    break_list = []
    if labels is None:
        break_list = [ val(i) for i in zip(*rows)]
        # creating top line
        final_string += create_lined_string( top_line_list, break_list )
    else:
        nrow = zip(labels, *rows)
        break_list = [ val(i) for i in nrow]
        # creating top line
        final_string += create_lined_string( top_line_list, break_list )
        # printing labels
        charlist = [print_char[0], labels, print_char[0], print_char[0]]
        final_string += create_char_string( charlist, break_list, centered)
        # creating middle line
        final_string += create_lined_string( middle_line_list, break_list)
         
    for row_list in rows:
        charlist = [print_char[0], row_list, print_char[0], print_char[0]]
        final_string += create_char_string(charlist, break_list, centered)
         
    
    final_string+= create_lined_string( bottom_line_list, break_list )
    # print( '\n' + final_string)
    return final_string

        
