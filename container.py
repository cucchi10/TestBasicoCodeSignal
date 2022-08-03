import math
from typing_extensions import runtime
class Container:
    """
    A container of integers that should support
    addition, removal, and search for the median integer
    """
    def __init__(self):
        container = []
        self.container = container

    def add(self, value: int) -> None:
        """
        Adds the specified value to the container

        :param value: int
        """
        # TODO: implement this method
        container = self.container
        try:
            if isinstance(value, int):
                container.append(value)
            return container
        except Exception:
            raise Exception

    def delete(self, value: int) -> bool:
        """
        Attempts to delete one item of the specified value from the container

        :param value: int
        :return: True, if the value has been deleted, or
                 False, otherwise.
        """
        # TODO: implement this method
        
        container = self.container
        if container != [] and isinstance(value, int):
            for indx, valor in enumerate(container):
                if valor == value:
                    container.pop(indx)
                    return True
        return False

    def get_median(self) -> int:
        """
        Finds the container's median integer value, which is
        the middle integer when the all integers are sorted in order.
        If the sorted array has an even length,
        the leftmost integer between the two middle 
        integers should be considered as the median.

        :return: The median if the array is not empty, or
        :raise:  a runtime exception, otherwise.
        """
        # TODO: implement this method
        try:
            container = self.container
            if not container:
                raise Exception
            if container == []:
                raise Exception
            if len(container) == 1:
                return container[0]
            container = sorted(container)
            if len(container)%2 == 0:
                #container = sorted(container)
                media = (len(container)//2)-1
                #media = math.floor(media)
                return container[media]
            media = (len(container)//2)
            media=math.ceil(media)
            return container[media]
        except Exception:
            raise Exception