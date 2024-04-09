sp = [1,[1],[1,[2]], [], [2, [3, 4, [5]]]]

def flat_list_recur(lst):
    if lst == []:
        return lst
    if isinstance(lst[0], list):
        
        return flat_list_recur(lst[0]) + flat_list_recur(lst[1:])
    return lst[:1] + flat_list_recur(lst[1:])
print(sum(flat_list_recur(sp)))
