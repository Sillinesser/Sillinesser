def enough(cap, on, wait):
    if cap - on > wait:
        return 0
    else:
        return -(cap - on - wait)
print(enough(cap, on, wait))