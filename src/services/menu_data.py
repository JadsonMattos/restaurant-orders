# Req 3.
import csv
from src.models.dish import Dish
from src.models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self._load_data(source_path)

    def _load_data(self, source_path: str) -> None:
        with open(source_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                dish_name, price, ingredient_name, recipe_amount = row
                dish = self._get_dish(dish_name, float(price))
                ingredient = Ingredient(ingredient_name)
                dish.add_ingredient_dependency(ingredient, int(recipe_amount))

    def _get_dish(self, name: str, price: float) -> Dish:
        for dish in self.dishes:
            if dish.name == name:
                return dish
        dish = Dish(name, price)
        self.dishes.add(dish)
        return dish
