from abc import ABC, abstractmethod


class Animal(ABC):
    """Classe abstraite pour définir un animal avec un son."""

    @abstractmethod
    def sound(self) -> str:
        """Retourne le son que fait l'animal."""
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        """Retourne le nom de l'animal."""
        pass
