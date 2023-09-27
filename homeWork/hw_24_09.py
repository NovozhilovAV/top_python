# Модуль 10. ООП.
# Часть 6. Множественное наследование. Полиморфизм.
# Реализация магических методов.

# Задание 1
# Создать базовый класс Фигура с методом для подсчета площади.
# Создать производные классы: прямоугольник, круг, прямоугольный треугольник,
# трапеция со своими методами для подсчета площади.

# Задание 2
# Для классов из задания 1 нужно переопределить магические методы int(возвращает площадь) и str(возвращает
# информацию о фигуре).

# Задание 3
# Создайте базовый класс Shape для рисования плоских фигур.
# Определите методы:
# ■ Show() — вывод на экран информации о фигуре;
# ■ Save() — сохранение фигуры в файл;
# ■ Load() — считывание фигуры из файла.
# Определите производные классы:
# ■ Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
# ■ Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
# ■ Circle — окружность с заданными координатами центра и радиусом;
# ■ Ellipse — эллипс с заданными координатами верхнего угла описанного вокруг него прямоугольника
# со сторонами, параллельными осям координат, и размерами этого прямоугольника.
# Создайте список фигур, сохраните фигуры в файл, загрузите в другой список и отобразите информацию о
# каждой из фигур.