import ast
from app.common.http_methods import GET
from flask import Blueprint, jsonify
from app.common.utils import _get_status_code
from app.controllers.order import OrderController

from app.controllers.report import ReportController

report = Blueprint('report', __name__)

@report.route('/', methods=GET)
def get_report():
    try:
        orders, error = OrderController.get_all()
        response = orders if not error else {'error': error}
        status_code = _get_status_code(orders, error)
    except Exception as e:
        error_msg = f"Failed to fetch orders for business report: {str(e)}"
        return jsonify({"error": error_msg}), 500
    
    try:
        orders_json_list = _parse_orders_json(response)
        business_report = _create_business_report(orders_json_list)
    except ValueError as e:
        error_msg = f"Failed to create business report: {str(e)}"
        return jsonify({"error": error_msg}), 500
    
    return jsonify(business_report), status_code


def _parse_orders_json(response):
    return ast.literal_eval(jsonify(response).data.decode())

def _create_business_report(orders_json_list):
    report_controller = ReportController(orders=orders_json_list)
    return report_controller.create()