def is_majority(items: list):
    return False if items.count(False) >= items.count(True) else True
