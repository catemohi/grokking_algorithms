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
