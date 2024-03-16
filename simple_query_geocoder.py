from geocoders.geocoder import Geocoder
from api import API

#Для каждого id алгоритм делает запрос на /areas/{{area_id}}
#Алгоритм получает лист дерева, получает parent_id и делает запрос на /areas/{{area_id}} с parent_id
#Алгоритм повторяет предыдущий шаг до тех пор, пока не дойдет до корня
#Алгоритм возвращает полный адрес

# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:

        node = API.get_area(area_id)
        full_adds = []
        full_adds.append(node.name)

        if node.parent_id is None:
            return ' '.join(full_adds)

        while node.parent_id:
            node = API.get_area(node.parent_id)
            full_adds.append(node.name)

            return ' '.join(full_adds)















        """
            TODO:
            - Делать запросы к API для каждой area
            - Для каждого ответа формировать полный адрес
        """
        raise NotImplementedError()
