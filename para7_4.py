def raise_to_deg(number, max_degree):
    i = 0
    for _ in range(max_degree):
        yield number**i
        i += 1


res = raise_to_deg(12235, 500)
print(res)
for _ in res:
    print(_)
