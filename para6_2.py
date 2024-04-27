try:
    print("Start")
    print(10/0)
    print("after error")
except NameError:
    print("We have a name error")
except ZeroDivisionError:
    print("Impossble")
else:
    print("No problem")
finally:
    print("Last")
print("Code")

