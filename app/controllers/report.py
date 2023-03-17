
from collections import defaultdict
import datetime


class ReportController():
    def __init__(self, orders: list, best_customers_count: int = 3):
        self.orders = orders
        self.best_customers_count = best_customers_count

    def create(self) -> dict:
        return {
            'popular_ingredients': self.get_most_requested_items(search_for='ingredients'),
            'month_with_more_sales': self.get_month_with_more_sales(),
            'best_customers': self.get_n_best_customers(number_of_customers=self.best_customers_count)
        }

    def get_most_requested_items(self, search_for: str) -> list:
        counts = {}
        for order in self.orders:
            for item in order[search_for]:
                item_id = item[0]
                if item_id not in counts:
                    counts[item_id] = 0
                counts[item_id] += 1
        max_count = max(counts.values())
        most_requested_items = [item_id for item_id,
                                count in counts.items() if count == max_count]

        return most_requested_items

    def get_month_with_more_sales(self) -> str:
        monthly_sales = defaultdict(float)

        for order in self.orders:
            month = order['date'].month
            monthly_sales[month] += order['total_price']

        best_month = max(monthly_sales, key=monthly_sales.get)

        return datetime.date(1900, best_month, 1).strftime('%B')

    def get_n_best_customers(self, number_of_customers) -> list[dict]:
        client_totals = {}
        for order in self.orders:
            client = order['client_name']
            total = order['total_price']
            if client in client_totals:
                client_totals[client] += total
            else:
                client_totals[client] = total
        sorted_clients = sorted(
            client_totals, key=client_totals.get, reverse=True)
        top_clients = sorted_clients[:number_of_customers]
        best_customers = []
        for client in top_clients:
            best_customers.append(
                {"client_name": client, "total_spending": client_totals[client]})
        return best_customers
