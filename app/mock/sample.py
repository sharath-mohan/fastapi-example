def create_items():
    items = []
    for i in range(1, 101):
        items.append({"item_id": i, "name": f"Item {i}"})
    return items