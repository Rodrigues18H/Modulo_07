from ex0 import FlameFactory, AquaFactory


def verify_obeject(obeject: FlameFactory | AquaFactory, nome: str, typ: str) -> None:
    criatura = obeject.create_base(nome, typ)
    print(criatura.describe())
    print(criatura.attack())


if __name__ == "__main__":
    print("Testing factory")
    Flam = FlameFactory()
    verify_obeject(Flam, "Flameling", "Fire")
    verify_obeject(Flam, "Pyrodon",  "Fire/Flying")
