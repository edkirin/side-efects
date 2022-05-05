# -*- coding: utf-8 -*-

# from __future__ import unicode_literals

# import sideeffect
import codecs
from teststring import TEST_STRING


def test_print():
    print("{}".format(TEST_STRING))


def test_open_gibberish_file():
    with codecs.open("04-tc-boom/gibberish.txt", "r", "utf-8") as f:
        for n, line in enumerate(f.readlines()):
            print(u"{:02d}: {}".format(n, line.upper())),


def main():
    # test_print()
    test_open_gibberish_file()


if __name__ == "__main__":
    main()
