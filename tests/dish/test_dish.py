from src.models.dish import Dish
from src.models.ingredient import Ingredient, Restriction
import pytest


# Req 2
def test_dish():
    dish1 = Dish("Lasanha", 20.0)
    dish2 = Dish("Lasanha", 20.0)
    dish3 = Dish("Pizza", 30.0)
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo parmesão")
    assert dish1.name == "Lasanha"
    assert dish1.price == 20.0
    assert repr(dish1) == "Dish('Lasanha', R$20.00)"
    assert dish1 == dish2
    assert dish1 != dish3
    assert hash(dish1) == hash(dish2)
    assert hash(dish1) != hash(dish3)
    with pytest.raises(AssertionError):
        assert dish1.name != "Lasanha"
    with pytest.raises(AssertionError):
        assert hash(dish1) != hash(dish2)
    with pytest.raises(AssertionError):
        assert hash(dish1) == hash(dish3)
    with pytest.raises(AssertionError):
        assert dish1 != dish2
    with pytest.raises(AssertionError):
        assert dish1 == dish3
    with pytest.raises(AssertionError):
        assert repr(dish1) != "Dish('Lasanha', R$20.00)"
    with pytest.raises(TypeError):
        Dish("Lasanha", "20.00")
    with pytest.raises(ValueError):
        Dish("Lasanha", 0)
    dish1.add_ingredient_dependency(ingredient1, 2)
    assert ingredient1 in dish1.recipe
    assert dish1.recipe.get(ingredient1) == 2
    dish1.add_ingredient_dependency(ingredient2, 3)
    assert dish1.get_restrictions() == {Restriction.LACTOSE,
                                        Restriction.ANIMAL_DERIVED}
    assert dish1.get_ingredients() == {ingredient1, ingredient2}
