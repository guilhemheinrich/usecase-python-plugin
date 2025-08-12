import pkg_resources
from typing import List, Type
from .animal import Animal


def discover_animals() -> List[Animal]:
    """Découvre et instancie tous les animaux disponibles via les plugins."""
    animals = []

    # Découvrir tous les entry points pour les plugins d'animaux
    for entry_point in pkg_resources.iter_entry_points('core.plugins'):
        try:
            # Charger la classe depuis l'entry point
            animal_class = entry_point.load()

            # Vérifier que c'est bien une sous-classe d'Animal
            if isinstance(animal_class, type) and issubclass(animal_class, Animal):
                # Instancier l'animal
                animal = animal_class()
                animals.append(animal)
                print(f"Animal découvert: {animal.name}")
            else:
                print(
                    f"Attention: {entry_point.name} n'est pas une classe Animal valide")
        except Exception as e:
            print(f"Erreur lors du chargement de {entry_point.name}: {e}")

    return animals


def make_all_sounds() -> List[str]:
    """Fait émettre un son à tous les animaux découverts."""
    animals = discover_animals()
    sounds = []

    for animal in animals:
        sound = animal.sound()
        sounds.append(f"{animal.name}: {sound}")
        print(f"{animal.name}: {sound}")

    return sounds
