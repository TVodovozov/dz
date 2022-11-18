"""
Задание 2.
Доработайте пример структуры "дерево", рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии
 с требованиями для бинарного дерева). При валидации приветствуется генерация
 собственного исключения
Поработайте с оптимизированной структурой,
протестируйте на реальных данных - на клиентском коде
"""


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def insert_val(self, new_node):
        print(f'вставляем {new_node}')
        root = self.get_root_val()
        if new_node > root:
            self.insert_right(new_node)
        if new_node < root:
            self.insert_left(new_node)

    # добавить левого потомка
    def insert_left(self, new_node):
        if new_node > self.root:
            raise ValueError(f"Значение должно быть меньше {self.root}")
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node < self.root:
            raise ValueError(f"Значение должно быть больше {self.root}")
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


root = BinaryTree(8)
print(root.get_root_val())
print(root.get_left_child())
root.insert_left(7)
print(root.get_left_child())
print(root.get_left_child().get_root_val())
root.insert_right(12)
print(root.get_right_child())
print(root.get_right_child().get_root_val())
root.get_right_child().set_root_val(16)
print(root.get_right_child().get_root_val())
