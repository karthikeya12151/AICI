def flatten_dict(nested_dict, parent_key='', sep='.'):
    items = []
    for key, value in nested_dict.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict): items.extend(flatten_dict(value, new_key, sep).items())
        elif isinstance(value, list):
            for i, item in enumerate(value):
                if isinstance(item, dict): items.extend(flatten_dict(item, f"{new_key}[{i}]", sep).items())
                else: items.append((f"{new_key}[{i}]", item))
        else: items.append((new_key, value))
    return dict(items)

if __name__ == "__main__":
    sample = {'user': {'id': 1, 'name': 'Ana'}, 'meta': {'lang': 'en'}}
    result = flatten_dict(sample)
    print(f"Input: {sample}")
    print(f"Output: {result}")
