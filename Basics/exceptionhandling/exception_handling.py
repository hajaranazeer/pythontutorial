try:
    print(25/0)
except OSError as e:
    print(e)
except Exception as e:
    print(e)
finally:
    print("this is finally")