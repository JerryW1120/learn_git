def ins_sort_rec(seq, n):

    if n == 0:

        return

    ins_sort_rec(seq, n - 1)

    j = n

    while j > 0 and seq[j - 1] > seq[j]:

        seq[j - 1], seq[j]= seq[j], seq[j - 1] #交换位置

        j -= 1
    return seq

seq = [2,3,3456,12,3,34,24,6,5,2,41,142]
print(ins_sort_rec(seq, len(seq) - 1))
