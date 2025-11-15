"""Demonstrates method resolution order in multiple inheritance."""


class Flyer:
    def action(self) -> str:
        return "fly"


class Swimmer:
    def action(self) -> str:
        return "swim"


class Duck(Flyer, Swimmer):
    pass


if __name__ == "__main__":
    duck = Duck()
    print("Duck action:", duck.action())
    print("MRO:", Duck.mro())
