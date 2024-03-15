from __future__ import annotations

from typing import TYPE_CHECKING

from components.base_component import BaseComponent
from equipment_types import EquipmentType

if TYPE_CHECKING:
    from entity import Item


class Equippable(BaseComponent):
    parent: Item

    def __init__(
        self,
        equipment_type: EquipmentType,
        power_bonus: int = 0,
        defense_bonus: int = 0,
    ):
        self.equipment_type = equipment_type

        self.power_bonus = power_bonus
        self.defense_bonus = defense_bonus

# WEAPONS
class Dagger(Equippable):
    def __init__(self) -> None:
        super().__init__(EquipmentType.WEAPON, power_bonus=2)

class Sword(Equippable):
    def __init__(self) -> None:
        super().__init__(EquipmentType.WEAPON, power_bonus=4)
class IceSword(Equippable):
    def __init__(self) -> None:
        super().__init__(EquipmentType.WEAPON, power_bonus=3)
        
# ARMORS
class LeatherArmor(Equippable):
    def __init__(self) -> None:
        super().__init__(EquipmentType.ARMOR, defense_bonus=1)

class Chainmail(Equippable):
    def __init__(self) -> None:
        super().__init__(EquipmentType.ARMOR, defense_bonus=3)