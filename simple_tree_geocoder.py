from api import API, TreeNode
from geocoders.geocoder import Geocoder

#При инициализации алгоритм получает данные из /areas
#Для каждого id алгоритм осуществляет перебор дерева:
#При нахождении необходимого узла, алгоритм возвращает этот узел "вверх" по дереву
#При движении "вверх" по дереву собирается путь к искомому узлу
#По найденому пути алгоритм формирует полный адрес
# Перебор дерева
class SimpleTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    def _apply_geocoding(self, area_id: str) -> str:

        stack = []

        for node in self.__data:
            stack.append((node, [node]))

        while stack:
            current_node, path = stack.pop()

            if current_node.id == area_id:
                full_adds = " ".join([n.name for n in path])
                return f"{area_id}: {full_adds}"

            for child_node in current_node.areas:
                stack.append((child_node, path + [child_node]))