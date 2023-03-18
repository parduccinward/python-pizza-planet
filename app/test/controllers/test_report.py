
import calendar
import pytest

from app.controllers.report import ReportController
from scripts.seed_constants import BEVERAGE_CHOICES, INGREDIENT_CHOICES


def test_create_report(fake_orders_with_mock_data):
    report_controller = ReportController(orders=fake_orders_with_mock_data, best_customers_count=4)

    business_report = report_controller.create()
    pytest.assume('popular_ingredients' in business_report)
    pytest.assume('month_with_more_sales' in business_report)
    pytest.assume('best_customers' in business_report)
    pytest.assume(len(business_report['best_customers']) == 4)
    for customer in business_report['best_customers']:
        pytest.assume('client_name' in customer)
        pytest.assume('total_spending' in customer)

def test_get_most_requested_items(fake_orders_with_mock_data):
    report_controller = ReportController(orders=fake_orders_with_mock_data)
    ingredient_dict = {ingredient[0]: ingredient[1] for ingredient in INGREDIENT_CHOICES}
    beverage_dict = {beverage[0]: beverage[1] for beverage in BEVERAGE_CHOICES}


    most_requested_ingredients_ids = report_controller.get_most_requested_items(search_for="ingredient_detail")
    most_requested_ingredients = [ingredient_dict.get(x) for x in most_requested_ingredients_ids]

    most_requested_beverages_ids = report_controller.get_most_requested_items(search_for="beverage_detail")
    most_requested_beverages = [beverage_dict.get(x) for x in most_requested_beverages_ids]

    pytest.assume(isinstance(most_requested_ingredients, list))
    pytest.assume(isinstance(most_requested_beverages, list))
    pytest.assume(all(isinstance(ingredient, str) for ingredient in most_requested_ingredients))
    pytest.assume(all(isinstance(beverage, str) for beverage in most_requested_beverages))


def test_get_month_with_more_sales(fake_orders_with_mock_data):
    report_controller = ReportController(orders=fake_orders_with_mock_data)
    string_month_with_more_sales = report_controller.get_month_with_more_sales()
    
    pytest.assume(isinstance(string_month_with_more_sales, str))
    pytest.assume(string_month_with_more_sales in calendar.month_name)

def test_get_n_best_customers(fake_orders_with_mock_data):
    report_controller = ReportController(orders=fake_orders_with_mock_data)
    best_3_customers = report_controller.get_n_best_customers(number_of_customers = 3)
    best_5_customers = report_controller.get_n_best_customers(number_of_customers = 5)

    pytest.assume(len(best_3_customers) == 3)
    unique_names = [client['client_name'] for client in best_3_customers]
    pytest.assume(len(unique_names) == len(set(unique_names)))

    pytest.assume(len(best_5_customers) == 5)
    unique_names = [client['client_name'] for client in best_5_customers]
    pytest.assume(len(unique_names) == len(set(unique_names)))
