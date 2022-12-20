from collections import deque

"""
===============================================================================
Задача 1
Из книги Грокаем Алгоритмы задача 6.1
Найти кратчайший путь от S до F
===============================================================================
Задача 2
Из книги Грокаем Алгоритмы задача 6.2
Найти кратчайший путь от CAB до BAT
===============================================================================
Задача 3
Из книги Грокаем Алгоритмы задача 6.3
Проверить списки действий по графу
===============================================================================
"""


def bfs_solution(graph: dict, root_item: str, search_item: str) -> int:
    """Задача найти кратчайший путь от root, до search
    Args:
        graph (dict): задача в виде графа
        root_item (str): элемент начала поиска
        search_item (str): элемент, который необзходимо найти
    Returns:
        int: кратчайший путь до элемента
    """
    visited, queue = set(), deque([{"vertex": root_item, "weight": 0}])
    visited.add(root_item)
    while queue:
        item = queue.popleft()
        vertex, weight = item["vertex"], item["weight"]
        if vertex == search_item:
            return weight
        for neighbour in graph[vertex]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append({"vertex": neighbour, "weight": weight + 1})
    return None


# Нам надо проверить 3 последовательности действий, на действительность.
# По факту задача сводится к вроверке сосдей в графе


def check_actions(graph: dict, actions: list) -> bool:
    """Проверка можно ли исполнить действия в перечисленном порядке.
    Args:
        graph (dict): граф зависимости действий
        action (list): список действий на проверку
    Returns:
        bool: возможена ли такая последовательность
    """
    root = actions[0]
    visited, queue = set(), deque([root])
    visited.add(root)

    while queue:
        vertex = queue.popleft()
        for neighbour in graph[vertex]:

            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)

        actions.remove(vertex)

        if actions and actions[0] not in queue:
            return False

    return True


if __name__ == "__main__":
    # Задача 1
    # Представим задачу в виде графа
    graph = {'s': ['q', 'w'],
             'q': ['e', 'f'],
             'w': ['e', 'r'],
             'e': [],
             'r': ['f']}
    assert bfs_solution(graph, 's', 'f') == 2, (
        "Задача выполнена не верно! Ваш ответ: "
        f"{bfs_solution(graph, 's', 'f')}")

    # Задача 2
    # Представим задачу в виде графа
    graph = {'CAB': ['CAT', 'CAR'],
             'CAR': ['BAR', 'CAT'],
             'CAT': ['MAT', 'BAT'],
             'MAT': ['BAT'],
             'BAR': ['BAT'],
             }
    # Воспользуемся готовым кодом из первой задачи
    assert bfs_solution(graph, 'CAB', 'BAT') == 2, (
        "Задача выполнена не верно! Ваш ответ: "
        f"{bfs_solution(graph, 'CAB', 'BAT')}")

    # Задача 3
    # Представим граф в виде ассоциативного массива списков
    graph = {'Проснуться': ['Принять душ', 'Почистить зубы'],
             'Принять душ': [],
             'Почистить зубы': ['Позавтракать'],
             'Позавтракать': [],
             }
    actions = ['Проснуться', 'Принять душ', 'Позавтракать', 'Почистить зубы']
    assert check_actions(graph, actions) is False, (
        "Задача выполнена не верно! Ваш ответ: "
        f"{check_actions(graph, actions)}")
    actions = ['Проснуться', 'Почистить зубы', 'Позавтракать', 'Принять душ']
    assert check_actions(graph, actions) is True, (
        "Задача выполнена не верно! Ваш ответ: "
        f"{check_actions(graph, actions)}")
    actions = ['Принять душ', 'Проснуться', 'Почистить зубы', 'Позавтракать']
    assert check_actions(graph, actions) is False, (
        "Задача выполнена не верно! Ваш ответ: "
        f"{check_actions(graph, actions)}")
