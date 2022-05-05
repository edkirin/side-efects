global_var = 42


def add_some_numbers(a: int, b: int):
    global global_var
    global_var = a + b
    return global_var


def main():
    assert global_var == 42
    add_some_numbers(3, 4)
    assert global_var == 42


if __name__ == "__main__":
    main()
