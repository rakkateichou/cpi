# Cubiomes Python Interface (CPI) Documentation

This is an updated fork of the original [cubiomespi](https://github.com/Languste27/cpi) package. It wraps the [Cubiomes](https://github.com/Cubitect/cubiomes) library and introduces a clean, object-oriented API in Python to find structures, spawn points, and biomes in Minecraft seeds.

**Key Features of this Fork:**
- Adds support for Minecraft 1.21 features (`Trial_Chambers`, etc.).
- Complete standard Python `IntEnum` integration for cleaner Data/Enum interactions.
- Added Object-Oriented wrapper (`Generator` class API).
- Cross-platform dynamic compilation via `setuptools`.

---

## Installation

You can install this fork directly via pip:

```bash
pip install cubiomespi-fork
```

*(Note: Requires Python 3.11+)*

## Usage / Quick Start

```python
from cubiomespi import Generator, MCVersion, Dimension, BiomeID, Structure

# 1. Initialize a Generator with a specific MC Version, Seed, and Dimension
generator = Generator(MCVersion.MC_1_21, -2197368822535229394, Dimension.DIM_OVERWORLD)

# 2. Get the Biome at 0, 0, 0
biome = generator.get_biome_at(0, 0, 0)
print(f"Biome at 0,0,0: {biome.label}") # "River"

# Comparison is direct and Pythonic!
if biome == BiomeID.plains:
    print("Found Plains!")

# 3. Find Spawn Position
spawn_x, spawn_z = generator.get_spawn_pos()
print(f"Spawn: ({spawn_x}, {spawn_z})")

# 4. Find the closest Village within a given range
closest_village = generator.find_closest_structure(Structure.Village, 0, 0, limit=100)
print("Closest Village:", closest_village)
```

## API Documentation

### Enum Classes
All core types (`BiomeID`, `Structure`, `MCVersion`, `Dimension`, `BastionType`) are standard Python `IntEnum` classes. This means they are evaluated as interoperable integers in C, while carrying `.name` and `.label` descriptors in Python.

- **`MCVersion`**: `MC_1_21`, `MC_1_20`, `MC_1_19`, etc.
- **`Dimension`**: `DIM_OVERWORLD`, `DIM_NETHER`, `DIM_END`.
- **`BiomeID`**: `plains`, `desert`, `ocean`, `river`, `lush_caves`, etc.
- **`Structure`**: `Village`, `Mansion`, `Desert_Pyramid`, `Trial_Chambers`, etc.
- **`BastionType`**: `HOUSING`, `STABLES`, `TREASURE`, `BRIDGE`.

### The `Generator` Class

Provides the primary interface for running calculations and looking up seed data.

- `__init__(mc_version: MCVersion, seed: int, dimension: Dimension)`
- `get_spawn_pos() -> tuple[int, int]` - Gets the default world spawn point.
- `get_biome_at(x: int, y: int, z: int) -> BiomeID` - Gets the Biome at specific X/Y/Z coords.
- `get_structure_pos(structure: Structure, rx: int, rz: int) -> tuple[int, int]` - Given region coordinates, returns exact coordinates of the structure.
- `is_viable_structure_pos(structure: Structure, x: int, z: int) -> bool` - Validates if a proposed structure position is structurally viable in that biome.
- `find_closest_structure(structure: Structure, cx: int, cz: int, limit: int) -> tuple[int, int]` - Locates the absolute closest structure starting from coordinates (cx, cz).
- `find_structure_in_range(structure: Structure, srx: int, srz: int, erx: int, erz: int) -> list[tuple[int, int]]` - Checks a rectangular region for any generated instances of a structure.
- `get_stronghold_pos(count=3) -> list[tuple[int, int]]` - Returns coordinates of the nearest strongholds.
- `get_bastion_variant(x: int, z: int) -> BastionType` - Determines the variant geometry of a bastion at coordinates.
- `get_end_y_height(x: int, z: int) -> int` - Returns surface height mapping in the End dimension.

### Utility Functions (from `cubiomespi.util`)

- `distance_between_structures(s1, s2)` - Fast math calc.
- `distance_from_00(c1)` - Fast origin calc.
- `distance_between_points(x1, y1, x2, y2)` - Quick cartesian distance mapping.
