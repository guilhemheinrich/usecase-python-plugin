import importlib.metadata
from typing import List

from .animal import Animal


def discover_animals() -> List[Animal]:
    """Découvre et instancie tous les animaux disponibles via les plugins."""
    animals = []

    try:
        # Découvrir tous les entry points pour les plugins d'animaux
        entry_points = importlib.metadata.entry_points(group='core.plugins')

        for entry_point in entry_points:
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
    except Exception as e:
        print(f"Erreur lors de la découverte des plugins: {e}")

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
