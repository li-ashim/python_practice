from typing import Dict, Any, Callable, Iterable, Sequence

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]


def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    """
    Query data with column selection and filters

    :param data: List of dictionaries with columns and values
    :param selector: result of `select` function call
    :param filters: Any number of results of `field_filter` function calls
    :return: Filtered data
    """
    res = selector(data)
    for filter in filters:
        res = filter(res)
    
    return res


def select(*columns: Sequence[str]) -> ModifierFunc:
    """Return function that selects only specific columns from dataset"""
    def select_columns(data: DataType) -> DataType:
        data_selected = []
        for entry in data:
            data_selected.append({col: val for col, val in entry.items() if col in columns})
        return data_selected
    
    return select_columns


def field_filter(column: Sequence[str], *values: Any) -> ModifierFunc:
    """Return function that filters specific column to be one of `values`"""
    def filter_columns(data:DataType) -> DataType:
        data_fitered = []
        for entry in data:
            if entry[column] in values:
                data_fitered.append(entry)
        return data_fitered
    
    return filter_columns

friends = [
    {'name': 'Сэм', 'gender': 'Мужской', 'sport': 'Баскетбол'},
    {'name': 'Эмили', 'gender': 'Женский', 'sport': 'Волейбол'}
]

result = query(
    friends,
    select('name', 'gender', 'sport'),
    field_filter('sport', *['Баскетбол', 'Волейбол']),
    field_filter('gender', *['Мужской']),
)