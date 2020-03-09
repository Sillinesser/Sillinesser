def filter_words(st):
    st1 = st.lower()
    st2 = st1.upper()[0] + st1[1:]
    st3 = st2.split()
    st4 = " ".join(st3)
    return st4