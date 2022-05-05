from dataclasses import dataclass


@dataclass
class Person:
    first_name: str
    last_name: str
    access_count: int = 0

    @property
    def formatted_name(self) -> str:
        self.access_count += 1
        return f"{self.first_name} {self.last_name}"

    def get_uppercase_first_name(self) -> str:
        # write something to db
        return self.first_name.upper()


def main():
    pero = Person(first_name="Pero", last_name="Perić")
    print(pero.formatted_name)
    print(pero.formatted_name)
    print(pero.formatted_name)
    print(f"{pero.access_count=}")


if __name__ == "__main__":
    main()
