def reverse(st):
    a, b = st.split()
    return b + " " + a
print(reverse('Hello world'))
print(reverse('Hi There.'))