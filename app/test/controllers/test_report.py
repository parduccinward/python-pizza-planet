
import pytest

from app.controllers.report import ReportController
from scripts.seed_constants import BEVERAGE_CHOICES, INGREDIENT_CHOICES


def test_get_most_requested_items(fake_orders_with_mock_data):
    report_controller = ReportController(orders=fake_orders_with_mock_data)
    ingredient_dict = {ingredient[0]: ingredient[1] for ingredient in INGREDIENT_CHOICES}
    beverage_dict = {beverage[0]: beverage[1] for beverage in BEVERAGE_CHOICES}


    most_requested_ingredients_ids = report_controller.get_most_requested_items(search_for="ingredients")
    most_requested_ingredients = [ingredient_dict.get(x) for x in most_requested_ingredients_ids]

    most_requested_beverages_ids = report_controller.get_most_requested_items(search_for="beverages")
    most_requested_beverages = [beverage_dict.get(x) for x in most_requested_beverages_ids]

    pytest.assume(isinstance(most_requested_ingredients, list))
    pytest.assume(isinstance(most_requested_beverages, list))
    pytest.assume(all(isinstance(ingredient, str) for ingredient in most_requested_ingredients))
    pytest.assume(all(isinstance(beverage, str) for beverage in most_requested_beverages))


@pytest.mark.skip
def test_get_date_with_more_sales():
    pytest.assume(False)


@pytest.mark.skip
def test_get_n_best_customers():
    pytest.assume(False)
