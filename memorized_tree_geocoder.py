from api import TreeNode, API
from geocoders.geocoder import Geocoder

#При инициализации алгоритм получает данные из /areas
#Алгоритм осуществляет перебор дерева регионов
#Для всех узлов дерева собирается полный адрес и записывается в словарь
#Для каждого id алгоритм возвращает данные из созданного словаря адресов
# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data
        self.address_dict = {}

    def _apply_geocoding(self, area_id: str) -> str:
        if not self.address_dict:
            stack = [(node, [node]) for node in self.__data]

            while stack:
                node, path = stack.pop()
                curr_path = "/".join([p.name for p in path])
                self.address_dict[node.id] = curr_path

                for child_node in node.areas:
                    stack.append((child_node, path + [child_node]))

        if area_id in self.address_dict:
            return self.address_dict[area_id]