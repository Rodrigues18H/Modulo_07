import abc
import typing
from .creature import Aquabub, Pyrodon, Flameling, Torragon, Creature


class CreatureFactory(abc.ABC):
    @abc.abstractmethod
    def create_base(self, nome: str, type_Cre: str) -> typing.Any:
        pass

    @abc.abstractmethod
    def create_evolved(self, nome: str, type_Cre: str) -> typing.Any:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self, nome: str, type_Cre: str) -> Creature:
        self.Flam = Flameling(nome, type_Cre)
        return self.Flam

    def create_evolved(self, nome: str, type_Cre: str) -> Creature:
        self.Pyro = Pyrodon(nome, type_Cre)
        return self.Pyro


class AquaFactory(CreatureFactory):
    def create_base(self, nome: str, type_Cre: str) -> Creature:
        self.Aqua = Aquabub(nome, type_Cre)
        return self.Aqua

    def create_evolved(self, nome: str, type_Cre: str) -> Creature:
        self.Torra = Torragon(nome, type_Cre)
        return self.Torra
