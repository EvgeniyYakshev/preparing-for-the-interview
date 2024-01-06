BAL_DICT = {
    '(': ')',
    '[': ']',
    '{': '}'
}

BALLANCED_LIST = [
    '(((([{}]))))',
    '[([])((([[[]]])))]{()}',
    '{{[()]}}'
]
UNBALLANCED_LIST = [
    '}{}',
    '{{[(])]}}',
    '[[{())}]'
]


class Stack(list):
    def __init__(self):               #Инициализировать новый пустой стек.
        self.items = []
    
    def is_empty(self):               #is_empty — проверка стека на пустоту. Метод возвращает True или False;
        return len(self) == 0

    def push(self, _item):            #push — добавляет новый элемент на вершину стека. Метод ничего не возвращает;
        self.append(_item)

    def pop(self):                    #pop — удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека;
        if not self.is_empty():
            _item = self[-1]
            self.__delitem__(-1)
        return _item

    def peek(self):                   #peek — возвращает верхний элемент стека, но не удаляет его. Стек не меняется;  
        if not self.is_empty():
            return self[-1]

    def size(self):                   #size — возвращает количество элементов в стеке. 
        return len(self)


def check_ballance(seq_):
    stack = Stack()
    for item_ in seq_:
        if item_ in BAL_DICT:
            stack.push(item_)
        elif item_ == BAL_DICT.get(stack.peek()):
            stack.pop()
        else:
            return False
    return stack.is_empty()


if __name__ == '__main__':
    for seq in BALLANCED_LIST + UNBALLANCED_LIST:
        print(f'{seq:<30}{check_ballance(seq)}')
