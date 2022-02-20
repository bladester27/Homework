"""
Я эту задачи самостоятельно не решил, а скопировал решение.
Пример реализации списка с итератором
"""


class MyList(object):
    """Класс списка"""

    def __init__(self, iterable=None):
        # Длина списка
        self._length = 0
        # Первый элемент списка
        self._head = None
        # Последний элемент списка
        self._tail = None
        # Добавление всех переданных элементов
        if iterable is not None:
            for element in iterable:
                self.append(element)

    def append(self, element):
        """Добавление элемента в конец списка"""

        # Создание элемента списка
        node = MyList._ListNode(element)

        if self._tail is None:
            # Список пока пустой
            self._head = self._tail = node
        else:
            # Добавление элемента
            self._tail.next = node
            node.prev = self._tail
            self._tail = node

        self._length += 1

    def __len__(self):
        return self._length

    def __repr__(self):
        # Метод join класса str принимает последовательность строк
        # и возвращает строку, в которой все элементы этой
        # последовательности соединены изначальной строкой.
        # Функция map применяет заданную функцию ко всем элементам последовательности.
        return 'MyList([{}])'.format(', '.join(map(repr, self)))

    def __getitem__(self, index):
        if not 0 <= index < len(self):
            raise IndexError('list index out of range')

        node = self._head
        for _ in range(index):
            node = node.next

        return node.value

    def __iter__(self):
        return MyList._Iterator(self)

    def clear(self):
        self._head = None

    def add_i(self, element, index):
        """Добавления элемента в произвольное место списка"""
        # Создание элемента списка
        node = MyList._ListNode(element)

        if index == self._length:
            self.append(element)
        elif index == 0:
            self._head.prev = node
            node.next = self._head
            self._head = node
            self._length += 1
        elif 1 <= index < self._length:
            tmp = self._head
            for i in range(index):
                tmp = tmp.next
            tmp_prev = tmp.prev
            tmp_prev.next = node
            node.prev = tmp_prev
            node.next = tmp
            tmp.prev = node
            self._length += 1
        else:
            raise IndexError('list index out of range')

    def del_i(self, index):
        """Удаления элемента из конца и произвольного места списка"""
        if 1 <= index < self._length - 1:
            tmp = self._head
            for _ in range(index):
                tmp = tmp.next
            tmp_prev = tmp.prev
            tmp_next = tmp.next
            tmp_prev.next = tmp_next
            tmp_next.prev = tmp_prev
            tmp.next = None
            tmp.prev = None
        elif index == 0:
            tmp = self._head
            tmp = tmp.next
            self._head.next = None
            tmp.prev = None
            self._head = tmp
        elif index == self._length - 1:
            tmp = self._tail
            tmp = tmp.prev
            self._tail.prev = None
            tmp.next = None
            self._tail = tmp
        else:
            raise IndexError('list index out of range')
        self._length -= 1

    class _ListNode(object):
        """Внутренний класс элемента списка"""

        # По умолчанию атрибуты-данные хранятся в словаре __dict__.
        # Если возможность динамически добавлять новые атрибуты
        # не требуется, можно заранее их описать, что более
        # эффективно с точки зрения памяти и быстродействия, что
        # особенно важно, когда создаётся множество экземляров
        # данного класса.
        __slots__ = ('value', 'prev', 'next')

        def __init__(self, value, prev=None, next=None):
            self.value = value
            self.prev = prev
            self.next = next

        def __repr__(self):
            return 'MyList._ListNode({}, {}, {})'.format(self.value,
                                                         id(self.prev),
                                                         id(self.next))

    class _Iterator(object):
        """Внутренний класс итератора"""

        def __init__(self, list_instance):
            self._list_instance = list_instance
            self._next_node = list_instance._head

        def __iter__(self):
            return self

        def __next__(self):
            if self._next_node is None:
                raise StopIteration

            value = self._next_node.value
            self._next_node = self._next_node.next

            return value


def main():
    my_list1 = MyList([1, 2, 5])
    print(my_list1)
    my_list1.add_i(15, 1)
    print(my_list1)
    my_list1.del_i(0)
    print(my_list1)
    my_list1.del_i(2)
    print(my_list1)


if __name__ == '__main__':
    main()
