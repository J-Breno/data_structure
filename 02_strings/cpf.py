def remove_non_digits(string):
    return string.replace(".", "").replace("-", "")

print(remove_non_digits("874.092.172-93"))