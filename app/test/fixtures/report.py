import pytest


@pytest.fixture
def report_uri():
    return '/report/'


@pytest.fixture
def fake_report_dict() -> dict:

    return {
        "popular_ingredients": [
            3
        ],
        "month_with_more_sales": "January",
        "best_customers": [
            {
                "client_name": "Casey Flores",
                "total_spending": 59.5
            },
            {
                "client_name": "Danielle Wheeler",
                "total_spending": 49.0
            },
            {
                "client_name": "Javier Logan",
                "total_spending": 31.0
            }
        ]
    }
