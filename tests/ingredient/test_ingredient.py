import pytest
from src.models.ingredient import Ingredient, Restriction


def test_ingredient():
    ingredient1 = Ingredient("queijo mussarela")
    ingredient2 = Ingredient("queijo mussarela")
    ingredient3 = Ingredient("bacon")
    assert ingredient1.name == "queijo mussarela"
    assert ingredient1.restrictions == {Restriction.LACTOSE,
                                        Restriction.ANIMAL_DERIVED}
    assert repr(ingredient1) == "Ingredient('queijo mussarela')"
    assert ingredient1 == ingredient2
    assert ingredient1 != ingredient3
    assert hash(ingredient1) == hash(ingredient2)
    assert hash(ingredient1) != hash(ingredient3)
    with pytest.raises(AssertionError):
        assert hash(ingredient1) != hash(ingredient2)
    with pytest.raises(AssertionError):
        assert hash(ingredient1) == hash(ingredient3)
    with pytest.raises(AssertionError):
        assert ingredient1 != ingredient2
    with pytest.raises(AssertionError):
        assert ingredient1 == ingredient3
    with pytest.raises(AssertionError):
        assert repr(ingredient1) != "Ingredient('queijo mussarela')"
    with pytest.raises(AssertionError):
        assert ingredient1.name != "queijo mussarela"
        assert ingredient1.restrictions != {Restriction.LACTOSE,
                                            Restriction.ANIMAL_DERIVED}
