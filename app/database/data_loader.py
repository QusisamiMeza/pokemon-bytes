import os
from csv import DictReader
from app.database.models import (
    Pokemon,
    PokemonType,
    PokemonAbility,
    Ability,
    PokemonStat,
    Stat,
    EggGroup,
    PokemonEggGroup,
    Move,
    MoveName,
    MoveDamageClass,
    MoveEffect,
    PokemonMove,
    PokemonMoveMethod,
    Generation,
    Species,
    Type,
    Nature,
)


# file paths
POKEMON_FILE_PATH = os.path.join(os.getcwd(), "archivos", "pokemon.csv")
POKEMON_TYPES_FILE_PATH = os.path.join(os.getcwd(), "archivos", "pokemon_types.csv")
TYPES_NAMES_FILE_PATH = os.path.join(os.getcwd(), "archivos", "type_names.csv")
TYPES_FILE_PATH = os.path.join(os.getcwd(), "archivos", "types.csv")
POKEMON_EGG_GROUP_FILE_PATH = os.path.join(
    os.getcwd(), "archivos", "pokemon_egg_groups.csv"
)
EGG_GROUP_FILE_PATH = os.path.join(os.getcwd(), "archivos", "egg_groups.csv")
STATS_FILE_PATH = os.path.join(os.getcwd(), "archivos", "stats.csv")
POKEMON_STATS_FILE_PATH = os.path.join(os.getcwd(), "archivos", "pokemon_stats.csv")
ABILITY_NAMES_FILE_PATH = os.path.join(os.getcwd(), "archivos", "ability_names.csv")
ABILITIES_FILE_PATH = os.path.join(os.getcwd(), "archivos", "abilities.csv")
POKEMON_ABILITIES_FILE_PATH = os.path.join(
    os.getcwd(), "archivos", "pokemon_abilities.csv"
)
NATURE_NAMES_FILE_PATH = os.path.join(os.getcwd(), "archivos", "nature_names.csv")
NATURE_FILE_PATH = os.path.join(os.getcwd(), "archivos", "natures.csv")
MOVES_FILE_PATH = os.path.join(os.getcwd(), "archivos", "moves.csv")
MOVE_NAMES_FILE_PATH = os.path.join(os.getcwd(), "archivos", "move_names.csv")
MOVE_DAMAGE_CLASSES_FILE_PATH = os.path.join(
    os.getcwd(), "archivos", "move_damage_classes.csv"
)
MOVE_EFFECT_FILE_PATH = os.path.join(os.getcwd(), "archivos", "move_effect.csv")
POKEMON_MOVES_FILE_PATH = os.path.join(os.getcwd(), "archivos", "pokemon_moves.csv")
POKEMON_MOVE_METHODS_FILE_PATH = os.path.join(
    os.getcwd(), "archivos", "pokemon_move_methods.csv"
)
GENERATIONS_FILE_PATH = os.path.join(os.getcwd(), "archivos", "generations.csv")
SPECIES_FILE_PATH = os.path.join(os.getcwd(), "archivos", "pokemon_species.csv")
language_id = 7


def get_pokemon_data(file_path):
    """Creaa una lista de instancias de Pokemon con la informacion del csv."""
    pokemon_list = []

    with open(file_path, mode="r") as file:
        reader = DictReader(file)

        for row in reader:
            pokemon = Pokemon(
                id=int(row["id"]),
                identifier=row["identifier"],
                species_id=int(row["species_id"]),
                height=int(row["height"]),
                weight=int(row["weight"]),
                base_experience=int(row["base_experience"]),
                order=int(row["order"]),
                is_default=int(row["is_default"]),
            )
            pokemon_list.append(pokemon)

    return pokemon_list


def get_pokemon_types_id(file_path):
    """Crea una lista de instancias de PokemonType a partir del csv."""
    pokemon_types_list = []
    with open(file_path, mode="r") as file:
        reader = DictReader(file)
        for row in reader:
            pokemon_type = PokemonType(
                pokemon_id=int(row["pokemon_id"]),
                type_id=int(row["type_id"]),
                slot=int(row["slot"]),
            )
            pokemon_types_list.append(pokemon_type)

    return pokemon_types_list


def get_types(file_path):
    """Crea una lista de instancias de Type con la informacion el csv."""
    types_list = []
    with open(file_path, mode="r") as file:
        reader = DictReader(file)
        for row in reader:
            type = Type(
                id=int(row["id"]),
                identifier=row["identifier"],
                generation_id=int(row["generation_id"]),
                damage_class_id=int(row["damage_class_id"])
                if "damage_class_id" in row and row["damage_class_id"]
                else None,
            )
            types_list.append(type)

    return types_list


def get_moves_data(moves_csv):
    """Crea una lista de instancias de Move con la informacion del archivo 'moves.csv'."""
    moves_list = []

    with open(moves_csv) as file:
        lines = DictReader(file)
        for line in lines:
            move = Move(
                id=int(line["id"]) if line["id"] != "" else None,
                identifier=line["identifier"] if line["identifier"] != "" else None,
                generation_id=int(line["generation_id"])
                if line["generation_id"] != ""
                else None,
                type_id=int(line["type_id"]) if line["type_id"] != "" else None,
                power=int(line["power"]) if line["power"] != "" else None,
                pp=int(line["pp"]) if line["pp"] != "" else None,
                accuracy=int(line["accuracy"]) if line["accuracy"] != "" else None,
                priority=int(line["priority"]) if line["priority"] != "" else None,
                target_id=int(line["target_id"]) if line["target_id"] != "" else None,
                damage_class_id=int(line["damage_class_id"])
                if line["damage_class_id"] != ""
                else None,
                effect_id=int(line["effect_id"]) if line["effect_id"] != "" else None,
                effect_chance=int(line["effect_chance"])
                if line["effect_chance"] != ""
                else None,
                contest_type_id=int(line["contest_type_id"])
                if line["contest_type_id"] != ""
                else None,
                contest_effect_id=int(line["contest_effect_id"])
                if line["contest_effect_id"] != ""
                else None,
                super_contest_effect_id=int(line["super_contest_effect_id"])
                if line["super_contest_effect_id"] != ""
                else None,
            )
            moves_list.append(move)

    return moves_list


def get_move_names_data(move_names_csv):
    """Crea una lista con las instancias de MoveName con la información de 'move_names.csv'."""
    move_names_list = []

    with open(move_names_csv) as file:
        lines = DictReader(file)
        for line in lines:
            move_name = MoveName(
                move_id=int(line["move_id"]),
                local_language_id=int(line["local_language_id"]),
                name=line["name"],
            )
            move_names_list.append(move_name)

    return move_names_list


def get_move_categories_data(move_damage_class_csv):
    """Crea una lista con las instancias de MoveDamageClass con la informacion del archivo 'move_damage_classes.csv'."""
    move_categories_list = []

    with open(move_damage_class_csv) as file:
        lines = DictReader(file)
        for line in lines:
            move_category = MoveDamageClass(
                id=int(line["id"]),
                identifier=line["identifier"],
            )
            move_categories_list.append(move_category)

    return move_categories_list


def get_move_effects_data(move_effect_prose_csv):
    """Crea una lista con las instancias de MoveEffect con la informacion del archivo 'move_effect_prose.csv'."""
    move_effects_list = []

    with open(move_effect_prose_csv) as file:
        lines = DictReader(file)
        for line in lines:
            move_effect = MoveEffect(
                move_effect_id=int(line["move_effect_id"]),
                local_language_id=int(line["local_language_id"]),
                short_effect=line["short_effect"],
                effect=line["effect "],
            )
            move_effects_list.append(move_effect)

    return move_effects_list


def get_pokemon_moves_data(pokemon_moves_csv):
    """Crea una lista de instancias de PokemonMove con la información de 'pokemon_moves.csv'."""
    pokemon_moves_list = []

    with open(pokemon_moves_csv) as file:
        lines = DictReader(file)
        for line in lines:
            pokemon_move = PokemonMove(
                pokemon_id=int(line["pokemon_id"]),
                version_group_id=int(line["version_group_id"]),
                move_id=int(line["move_id"]),
                pokemon_move_method_id=int(line["pokemon_move_method_id"]),
                level=int(line["level"]),
                order=int(line["order"]) if line["order"] != "" else None,
            )
            pokemon_moves_list.append(pokemon_move)

    return pokemon_moves_list


def get_pokemon_move_methods_data(pokemon_move_methods_csv):
    """Crea una lista de instancias de PokemonMoveMethod con la información de 'pokemon_move_methods.csv'."""
    pokemon_move_methods_list = []

    with open(pokemon_move_methods_csv) as file:
        lines = DictReader(file)
        for line in lines:
            move_method = PokemonMoveMethod(
                pokemon_move_method_id=int(line["pokemon_move_method_id"]),
                local_language_id=int(line["local_language_id"]),
                name=line["name"],
                description=line["description"],
            )
            pokemon_move_methods_list.append(move_method)

    return pokemon_move_methods_list


def get_pokemon_abilities(file):
    """Crea una lista de instancias de las habilidades de un pokemon."""
    pokemon_abilities = []
    with open(file, mode="r") as file_csv:
        content = DictReader(file_csv)
        for row in content:
            pokemon_ability = PokemonAbility(
                pokemon_id=int(row["pokemon_id"]),
                ability_id=int(row["ability_id"]),
                is_hidden=int(row["is_hidden"]),
                slot=int(row["slot"]),
            )
            pokemon_abilities.append(pokemon_ability)
    return pokemon_abilities


def get_abilities(file):
    """Crea una lista de instancias de las habilidades."""
    abilities = []
    with open(file, mode="r") as file_csv:
        content = DictReader(file_csv)
        for row in content:
            ability = Ability(
                id=int(row["id"]),
                identifier=row["identifier"],
                generation=int(row["generation_id"]),
                is_main_series=int(row["is_main_series"]),
            )
            abilities.append(ability)
    return abilities


def get_pokemon_stats(file):
    """Crea una lista de instancias de las estadísticas de un pokemon."""
    pokemon_stats = []
    with open(file, mode="r") as file_csv:
        content = DictReader(file_csv)
        for row in content:
            pokemon_stat = PokemonStat(
                pokemon_id=int(row["pokemon_id"]),
                stat_id=int(row["stat_id"]),
                base_stat=int(row["base_stat"]),
                effort=int(row["effort"]),
            )
            pokemon_stats.append(pokemon_stat)
    return pokemon_stats


def get_stats(file):
    """Crea una lista de instancias de las estadísticas."""
    stats = []
    with open(file, mode="r") as file_csv:
        content = DictReader(file_csv)
        for row in content:
            try:
                stat = Stat(
                    id=int(row["id"]),
                    damage_class_id=int(row["damage_class_id"]),
                    identifier=row["identifier"],
                    is_battle_only=int(row["is_battle_only"]),
                    game_index=int(row["game_index"]),
                )
            except ValueError:
                stat = Stat(
                    id=int(row["id"]),
                    damage_class_id=int(0),
                    identifier=row["identifier"],
                    is_battle_only=int(row["is_battle_only"]),
                    game_index=int(0),
                )
            stats.append(stat)
    return stats


def get_pokemon_egg_group(file):
    """Crea una lista de instancias de los grupos de huevo de los pokemones."""
    pokemon_egg_groups = []
    with open(file, mode="r") as file_csv:
        content = DictReader(file_csv)
        for row in content:
            pokemon_egg_group = PokemonEggGroup(
                species_id=int(row["species_id"]), egg_group_id=int(row["egg_group_id"])
            )
            pokemon_egg_groups.append(pokemon_egg_group)
    return pokemon_egg_groups


def get_egg_groups(file):
    """Crea una lista de instancias de los grupos de huevo."""
    egg_groups = []
    with open(file, mode="r") as file_csv:
        content = DictReader(file_csv)
        for row in content:
            egg_group = EggGroup(
                id=int(row["id"]),
                identifier=row["identifier"],
            )
            egg_groups.append(egg_group)
    return egg_groups


def get_nature(file):
    """Devuelve todas las naturalezas."""
    natures = []
    with open(file, mode="r") as file_csv:
        content = DictReader(file_csv)
        for row in content:
            nature = Nature(
                id=int(row["id"]),
                identifier=row["identifier"],
                decreased_stat_id=int(row["decreased_stat_id"]),
                increased_stat_id=int(row["increased_stat_id"]),
                hates_flavor_id=int(row["hates_flavor_id"]),
                likes_flavor_id=int(row["likes_flavor_id"]),
                game_index=int(row["game_index"]),
            )
            natures.append(nature)
    return natures


def get_generations_data(file):
    """Devuelve las generaciones."""
    generations = []
    with open(file, mode="r") as file_csv:
        content = DictReader(file_csv)
        for row in content:
            generations.append(Generation(id=int(row["id"])))
    return generations


def get_species_data(file):
    """Devuelve las especies."""
    species = []
    with open(file, mode="r") as file_csv:
        content = DictReader(file_csv)
        for row in content:
            specie = Species(id=int(row["id"]), generation_id=int(row["generation_id"]))
            species.append(specie)
    return species


generations = get_generations_data(GENERATIONS_FILE_PATH)


def normalizar_move_name(name):
    """
    Recibe el nombre de un movimiento, reemplaza guiones (que pueda tener de medio) por
    espacios, y devuelve el nombre capitalizado.
    """

    name.split("-")
    " ".join(name)
    return name.capitalize()


# TODO quizas es mejor moves esto a un settings.py o algo asi
MIN_MOVES_PER_MEMBER = 1
MAX_MOVES_PER_MEMBER = 4
MIN_TEAM_MEMBERS = 1
MAX_TEAM_MEMBERS = 6
MAX_STAT_VALUE = 255
MAX_STATS_TOTAL = 510
