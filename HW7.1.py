def count_positives_sum_negatives(arr):
    a = [0, 0]
    for i in arr:
        if i > 0:
            a[0] = a[0] + 1
        elif i < 0:
            a[1] = a[1] + int(i)
    if len(arr) == 0:
        a = []

    return a