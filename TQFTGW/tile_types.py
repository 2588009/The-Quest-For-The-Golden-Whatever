from typing import Tuple

import numpy as np  # type: ignore

# Tile graphics structured type compatible with Console.tiles_rgb.
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.
        ("fg", "3B"),  # 3 unsigned bytes, for RGB colors.
        ("bg", "3B"),
    ]
)

# Tile struct used for statically defined tile data.
tile_dt = np.dtype(
    [
        ("walkable", bool),  # True if this tile can be walked over.
        ("transparent", bool),  # True if this tile doesn't block FOV.
        ("dark", graphic_dt),  # Graphics for when this tile is not in FOV.
        ("light", graphic_dt),  # Graphics for when the tile is in FOV.
    ]
)


def new_tile(
    *,  # Enforce the use of keywords, so that parameter order doesn't matter.
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
    light: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining individual tile types """
    return np.array((walkable, transparent, dark, light), dtype=tile_dt)


# SHROUD represents unexplored, unseen tiles
SHROUD = np.array((ord(" "), (255, 255, 255), (0, 0, 0)), dtype=graphic_dt)

floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord("."), (127, 127, 127), (0, 0, 0)),
    light=(ord("."), (255, 255, 255), (0, 0, 0)),
)
wall = new_tile(
    walkable=False,
    transparent=False,
    dark=(ord("#"), (63, 63, 63), (0, 0, 0)),
    light=(ord("#"), (195, 195, 195), (0, 0, 0)),
)
boss_floor = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord("."), (127, 63, 63), (0, 0, 0)),
    light=(ord("."), (255, 63, 63), (0, 0, 0)),
)
boss_wall = new_tile(
    walkable=True,
    transparent=False,
    dark=(ord("#"), (20, 0, 0), (0, 0, 0)),
    light=(ord("#"), (70, 0, 0), (0, 0, 0)),
)
down_stairs = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(">"), (196, 196, 196), (0, 0, 0)),
    light=(ord(">"), (255, 255, 255), (0, 0, 0)),
)
boss_stairs = new_tile(
    walkable=True,
    transparent=True,
    dark=(ord(">"), (255, 0, 0), (0, 0, 0)),
    light=(ord(">"), (255, 0, 0), (0, 0, 0)),
)