
class ReportController():
    def __init__(self, orders:list):
        self.orders = orders

    def get_most_requested_items(self, search_for:str) -> list:
        counts = {}
        for order in self.orders:
            for item in order[search_for]:
                item_id = item[0]
                if item_id not in counts:
                    counts[item_id] = 0
                counts[item_id] += 1
        max_count = max(counts.values())
        most_requested_items = [item_id for item_id, count in counts.items() if count == max_count]
        
        return most_requested_items