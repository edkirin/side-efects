# from __future__ import unicode_literals
# import sideeffect
from teststring import TEST_STRING


def print_test_string_bytes():
    print([c for c in TEST_STRING])
    print([c for c in bytes(TEST_STRING.encode("utf-8"))])


def main():
    print_test_string_bytes()
    # print("TEST_STRING: {}".format(TEST_STRING))


if __name__ == "__main__":
    main()
