def most_frequent_item_count(collection):
    if not collection:
        return 0
    max_count = 0
    for num in collection:
        current_count = collection.count(num)
        if current_count > max_count:
            max_count = current_count
    return max_count
