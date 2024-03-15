from components.ai import HostileEnemy
from components import consumable, equippable
from components.equipment import Equipment
from components.fighter import Fighter
from components.inventory import Inventory
from components.level import Level
from entity import Actor, Item


player = Actor(
    char="@",
    color=(255, 255, 255),
    name="Player",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=2, base_power=5),
    inventory=Inventory(capacity=26),
    level=Level(level_up_base=200),
)

# MONSTERS
orc = Actor(
    char="o",
    color=(63, 127, 63),
    name="Orc",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=10, base_defense=0, base_power=3),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=35),
)
troll = Actor(
    char="T",
    color=(0, 127, 0),
    name="Troll",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=16, base_defense=1, base_power=4),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=100),
)
troll_commander = Actor(
    char="T",
    color=(0, 63, 0),
    name="Troll Commander",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=30, base_defense=3, base_power=6),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=1000),
)
ice_fiend = Actor(
    char="j",
    color=(0, 63, 255),
    name="Ice Fiend",
    ai_cls=HostileEnemy,
    equipment=Equipment(),
    fighter=Fighter(hp=1, base_defense=0, base_power=1),
    inventory=Inventory(capacity=0),
    level=Level(xp_given=0),
    flags=["dieOnAttack"],
    special="freezeAttack",
)

# CONSUMABLE ITEMS
health_potion = Item(
    char="!",
    color=(127, 0, 255),
    name="Health Potion",
    consumable=consumable.HealingConsumable(amount=4),
)
lightning_scroll = Item(
    char="?",
    color=(0, 255, 255),
    name="Scroll of Lightning",
    consumable=consumable.LightningDamageConsumable(damage=20, maximum_range=5),
)
confusion_scroll = Item(
    char="?",
    color=(255, 0, 255),
    name="Scroll of Confusion",
    consumable=consumable.ConfusionConsumable(number_of_turns=10),
)
fireball_scroll = Item(
    char="?",
    color=(255, 63, 0),
    name="Scroll of Flames",
    consumable=consumable.FireballDamageConsumable(damage=12, radius=3),
)
ice_scroll = Item(
    char="?",
    color=(127, 255, 255),
    name="Scroll of Ice",
    consumable=consumable.IceDamageConsumable(damage=1, number_of_turns=5),
)

# EQUIPMENT - WEAPONS
dagger = Item(
    char="/",
    color=(0, 191, 255),
    name="Dagger",
    equippable=equippable.Dagger(),
)
sword = Item(
    char="/",
    color=(0, 141, 205),
    name="Sword",
    equippable=equippable.Sword(),
)
ice_sword = Item(
    char="/",
    color=(0, 255, 255),
    name="Ice Sword",
    equippable=equippable.IceSword(),
    special="freezeAttack"
)

# EQUIPMENT - ARMORS
leather_armor = Item(
    char="[",
    color=(87, 43, 43),
    name="Leather Armor",
    equippable=equippable.LeatherArmor(),
)
chain_mail = Item(
    char="[",
    color=(69, 69, 69),
    name="Chainmail",
    equippable=equippable.Chainmail(),
)
ice_mail = Item(
    char="[",
    color=(0, 127, 255),
    name="Ice Armor",
    equippable=equippable.Chainmail(),
    special="resistFreeze"
)