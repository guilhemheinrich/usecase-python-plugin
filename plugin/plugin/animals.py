from core import Animal


class Cow(Animal):
    """Implémentation d'une vache."""

    @property
    def name(self) -> str:
        """Retourne le nom de l'animal."""
        return "Vache"

    def sound(self) -> str:
        """Retourne le son que fait la vache."""
        return "MEEUUUH!"
