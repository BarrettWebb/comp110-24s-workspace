"""Some functions for my garden plan!"""


__author__ = "730544769"


def add_by_kind(plant: dict[str, list[str]], plant_type: str, plant_name: str) -> None:
    """Sorting by kind of plant."""
    if plant_type in plant:
        plant[plant_type].append(plant_name)
    else:
        plant[plant_type] = [plant_name]
    return None


def add_by_date(date: dict[str, list[str]], month: str, flower: str) -> None:
    """Organize by date."""
    if month in date:
        date[month].append(flower)
    else:
        date[month] = [flower]
    return None


def lookup_by_kind_and_date(plant_type: dict[str, list[str]], date: dict[str, list[str]], kind: str, month: str) -> str:
    """Look up if a type of plant is at that time and date."""
    if kind in plant_type and month in date:
        plants = [plant for plant in plant_type[kind] if plant in date[month]]
        if plants:
            return f"{kind} to plant in {month}: {plants}"
        else:
            return f"No {kind}s to plant in {month}."
    else:
        return f"{kind} or {month} does not exist in the garden."