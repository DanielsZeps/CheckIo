def index_power(array: list, n: int):
    try:
        return pow(array[n], n)
    except:
        return -1
