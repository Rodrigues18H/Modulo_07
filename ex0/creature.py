import abc
import typing


class Creature(abc.ABC):
    def __init__(self, nome: str, type_creature: str) -> None:
        self.nome = nome
        self.type_creature = type_creature

    @abc.abstractmethod
    def attack(self) -> typing.Any:
        pass

    def describe(self) -> str:
        return f"{self.nome} is a {self.type_creature} type Creature"


class Flameling(Creature):
    def __init__(self, nome: str, type_creature: str) -> None:
        super().__init__(nome, type_creature)

    def attack(self) -> str:
        return f"{self.nome} uses Ember!"


class Pyrodon(Creature):
    def __init__(self, nome: str, type_creature: str) -> None:
        super().__init__(nome, type_creature)

    def attack(self) -> str:
        return f"{self.nome} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self, nome: str, type_creature: str) -> None:
        super().__init__(nome, type_creature)

    def attack(self) -> str:
        return f"{self.nome} uses Water Gun!"


class Torragon(Creature):
    def __init__(self, nome: str, type_creature: str) -> None:
        super().__init__(nome, type_creature)

    def attack(self) -> str:
        return f"{self.nome} uses Hydro Pump!"
