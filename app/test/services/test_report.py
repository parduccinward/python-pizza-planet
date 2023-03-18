import pytest


from pytest_mock import mocker


def test_get_report_service(client, report_uri, fake_orders_with_mock_data, fake_report_dict, mocker):

    fake_orders = fake_orders_with_mock_data
    fake_report = fake_report_dict
    mock_get_all = mocker.patch(
        'app.controllers.order.OrderController.get_all',
        return_value=(fake_orders, None)
    )
    mock_business_report = mocker.patch(
        'app.controllers.report.ReportController.create',
        return_value=(fake_report, None)
    )

    response = client.get(report_uri)

    response_has_status_200 = response.status.startswith('200')
    response_json = response.get_json()[0]
    expected_keys = {'best_customers',
                     'month_with_more_sales', 'popular_ingredients'}

    pytest.assume(response_has_status_200)
    pytest.assume(isinstance(response_json, dict))
    pytest.assume((response_json.keys()) == expected_keys)
    mock_get_all.assert_called_once()
    mock_business_report.assert_called_once()
    
