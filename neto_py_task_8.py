"""Описание классов Домашние животные и примеры работы с ними."""


class Livestock:
    """Класс Домашние животные."""

    name = None
    price = None
    breed = None
    weight = None
    status = 'ON BASE'

    def __init__(self, name, price, breed, weight):
        """Инициализация объекта класса - имя, стоимость, порода, вес."""
        self.name = name
        self.price = price
        self.breed = breed
        self.weight = weight

    def print_status(self):
        """Сообщение о текущем статусе животного."""
        print('{}: {}'.format(self.name, self.status))

    def run(self):
        """Смена статуса животного на БЕЖАТЬ."""
        self.status = 'RUN'

    def eat(self):
        """Смена статуса животного на ЕСТЬ."""
        self.status = 'EAT'

    def sleep(self):
        """Смена статуса животного на СПАТЬ."""
        self.status = 'SLEEP'

    def wakeup(self):
        """Смена статуса животного на ВЕРНУТЬСЯ НА СКОТНЫЙ ДВОР."""
        self.status = 'ON BASE'


class Birds(Livestock):
    """Класс Птицы, подчиненный Домашние живтотные."""

    def fly(self):
        """Смена статуса птицы на ЛЕТЕТЬ."""
        self.status = 'FLY'
        super().print_status()


class Animals(Livestock):
    """Класс Животины, подченный классу Домашние животные."""

    # показатель выдачи навоза Животиной
    shit = 0

    def give_shit(self):
        """Команда - ДАТЬ НАВОЗА."""
        self.shit += 1
        print('Животное {} дало навозу уже {} кг'.format(self.name, self.shit))


class Cattle(Animals):
    """Класс Скотина, подченный классу Животины."""

    # показатель выдачи молока Скотиной
    milk = 0

    def give_milk(self):
        """Команда - ДАТЬ МОЛОКА."""
        self.milk += 1
        print('Животное {} дало молока уже {} литров'.
              format(self.name, self.shit))


class Boar(Animals):
    """Класс Свины, подченный классу Скотина."""

    # показатель увеличения жира у Свины
    fat = 0

    def increasefat(self):
        """Команда - НАРОСТИТЬ ЖИР."""
        self.fat += 1
        print('Животное {} дало сальца уже {} кг'.format(self.name, self.fat))


class Waterfowl(Birds):
    """Класс Водоплавающие, подченный классу Птицы."""

    def voice(self):
        """Команда - ГОЛОС."""
        print('ГА-ГА')


class Nonwaterfowl(Birds):
    """Класс Неводоплавающие, подченный классу Птицы."""

    # показатель выдачи яиц у Неводоплавающие
    egg = 0

    def give_egg(self):
        """Команда - ДАТЬ ЯИЦО."""
        self.egg += 1
        print('Животное {} дало яиц уже {} шт'.format(self.name, self.egg))


class Cow(Cattle):
    """Класс Коровы, подченный классу Скотина."""

    def voice(self):
        """Команда - ГОЛОС."""
        print('МУ')


class Goat(Cattle):
    """Класс Козы, подченный классу Скотина."""

    def voice(self):
        """Команда - ГОЛОС."""
        print('БЕ')


class Sheep(Cattle):
    """Класс Овцы, подченный классу Скотина."""

    def voice(self):
        """Команда - ГОЛОС."""
        print('МЕ')


class Pig(Boar):
    """Класс Свиньи, подченный классу Свины."""

    def voice(self):
        """Команда - ГОЛОС."""
        print('ХРЮ')


class Duck(Waterfowl):
    """Класс Утки, подченный классу Водоплавающие."""

    def voice(self):
        """Команда - ГОЛОС."""
        super().voice()


class Goose(Waterfowl):
    """Класс Гуси, подченный классу Водоплавающие."""

    def voice(self):
        """Команда - ГОЛОС."""
        super().voice()


class Chicken(Nonwaterfowl):
    """Класс Курицы, подченный классу Неводоплавающие."""

    def voice(self):
        """Команда - ГОЛОС."""
        print('КО-КО-КО')

    def fly(self):
        """Команда - ЛЕТАТЬ."""
        self.status = 'I CANT FLY'
        super().print_status()


def print_dict(our_object):
    """Дать информацию об объекте класса."""
    print(our_object.__dict__)


def main():
    """Приемеры использования классов."""
    our_cow = Cow('Корова Мурка', 1000, 'безпородная', 500)
    our_duck_1 = Duck('Дональд', 50, 'которая в цене', 5)
    our_duck_2 = Duck('Скрудж', 150, 'которая в цене', 15)
    our_goose = Goose('Гусь Жирняк', 250, 'которая в цене', 25)
    our_chicken = Chicken('Ряба', 150, 'которая в цене', 20)

    print_dict(our_cow)
    print_dict(our_duck_1)
    print_dict(our_duck_2)
    print_dict(our_chicken)

    our_cow.voice()
    our_duck_1.voice()
    our_duck_2.voice()
    our_goose.voice()
    our_chicken.voice()

    our_cow.give_shit()
    our_cow.give_shit()

    our_goose.fly()
    our_chicken.fly()

    our_duck_1.run()
    our_duck_1.print_status()
    our_duck_1.sleep()
    our_duck_1.print_status()
    our_duck_1.wakeup()
    our_duck_1.print_status()


main()
