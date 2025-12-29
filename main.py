from lab_python_oop.rectangle import Rectangle
from lab_python_oop.circle import Circle
from lab_python_oop.square import Square

import cowsay

def main():
    rectangle = Rectangle(22, 22, "Синий")
    circle = Circle(22, "Зеленый")
    square = Square(22, "Красный")

    print(rectangle)
    print(circle)
    print(square)

    message = """
    Урра! Отлично сработано, ребятки. Давайте завтра не придем?
    Возьмем отгул на денек?
    Вы пробовали шаурму?
    В двух кварталах отсюда делают какую-то шаурму.
    Не знаю, что это, но мне хочется.

    -- Тони Старк
    """.strip()

    # Используем функцию cow из модуля cowsay
    print(cowsay.cow(message))

if __name__ == "__main__":
    main()
