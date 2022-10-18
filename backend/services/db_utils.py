def generate_query_columns_value(data_dict):
    return {
        'name': data_dict.__class__.__name__.lower(),
        'columns': ', '.join(dict(data_dict).keys()),
        'values': tuple(dict(data_dict).values())
    }