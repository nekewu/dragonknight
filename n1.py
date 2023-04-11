class Hero():
    def __init__ (self, name, health, armor, power, weapon):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.weapon = weapon
    def print_info(self):
        print('Уровень здоровья:', self.health)
        print('Класс брони:', self.armor)
        print('Сила оружия:', self.power)
        print('Оружие:', self.weapon)
    def alive(self):
        if self.health > 0:
            return True
        else:
            return False
    def strike(self, enemy):
        enemy.armor -= self.power
        if enemy.armor < 0:
            enemy.health -= self.power
            enemy.armor = 0
class Warrior(Hero):
    def hello(self):
        print('Из леса медленно выходит воин, пафосно взмахивая мечом')
    def attack(self, enemy):
        print(self.name, 'наносит рубящий удар мечом в сторону', enemy.name)
        print('Результат схватки для', self.name)
        self.print_info()
        print('Результат схватки для', enemy.name)
        enemy.print_info()
class Mag(Hero):
    def hello(self):
        print('На поляне появляется маг, выходя из круга телепортации')
    def attack(self, enemy):
        print(self.name, 'взмахивает посохом в сторону', enemy.name)
        print('Результат схватки для', self.name)
        self.print_info()
        print('Результат схватки для', enemy.name)
        enemy.print_info()
class Bard(Hero):
    def hello(self):
        print('Из таверны, пьяно пошатываясь, выползает бард')
    def attack(self, enemy):
        print(self.name, 'выхватывает лютню и начинает играть, завораживая', enemy.name)
        print('Результат схватки для', self.name)
        self.print_info()
        print('Результат схватки для', enemy.name)
        enemy.print_info()
class Rogue_ar(Hero):
    def hello(self):
        print('Мимо героя пролетает стрела, оповещая о притаившемся разбойнике')
        print('Знакомьтесь,', self.name)
    def attack(self, enemy):
        print(self.name, 'выхватывает арбалет и стреляет в', enemy.name)
        print('Результат схватки для', self.name)
        self.print_info()
        print('Результат схватки для', enemy.name)
        enemy.print_info()
class Rogue_mch(Hero):
    def hello(self):
        print('Дорогу перегораживает разбойник, гнусно ухмыляясь')
        print('Знакомьтесь,', self.name)
    def attack(self, enemy):
        print(self.name, 'с силой ударяет мечом', enemy.name)
        print('Результат схватки для', self.name)
        self.print_info()
        print('Результат схватки для', enemy.name)
        enemy.print_info()
class Dragon(Hero):
    def hello(self):
        print('Из пещеры доносятся маленькие струйки огня, и перед героем предстаёт ДРАКОН')
    def attack_fire(self, enemy):
        print(self.name, 'пышет огнём на', enemy.name)
        print('Результат схватки для', self.name)
        self.print_info()
        print('Результат схватки для', enemy.name)
        enemy.print_info()
    def attack_kgt(self, enemy):
        print(self.name, 'замахивается огромной лапой с остро поблескивающими когтями на', enemy.name)
        print('Результат схватки для', self.name)
        self.print_info()
        print('Результат схватки для', enemy.name)
        enemy.print_info()

from random import randint

print('Добрый день, путник')
print('Сегодня ты отправишься в увлекательное путешествие')
name = input('Как твоё имя? ')
print('А теперь выбери свой класс')
class_choise = input('Воин, бард или маг? ').lower()
print('')
if class_choise == 'воин':
    knight = Warrior(name, 150, 50, 20, 'меч')
elif class_choise == 'бард':
    knight = Bard(name, 30, 10, 100, 'лютня')
elif class_choise == 'маг':
    knight = Mag(name, 50, 20, 80, 'посох')

knight.hello()
knight.print_info()

print('Здравствуй,', knight.name)
answer = input('Ты готов к приключению?(да/нет) ').lower()
if answer == 'да':
    play = True
else:
    play = False

print('Вы решаете отправиться за сокровищами!')
print('Дурость избранности ударила вам в голову!')
print('Вы взмахиваете оружием и идёте в дорогу.')
print('')
print('На дороге вы встречаете разбойника.')


enemy1 = Rogue_mch('Вилли', 5, 10, 10, 'меч')
enemy1.hello()
answ = input('Вы готовы размять свои кости и оружие? да/нет ').lower()
if answ == 'да':
    while enemy1.health > 0 and knight.health > 0:
        if randint(0,1) == 1:
            fighters = [knight, enemy1]
        else:
            fighters = [enemy1, knight]
        fighters[0].strike(fighters[1])
        fighters[0].attack(fighters[1])
    if enemy1.alive() == False:
        print(enemy1.name, 'умер от руки', knight.name)
        print('Какой вопиющий пример жестокости')
    elif knight.alive() == False:
        print('Вы бесславно погибаете, не успев достичь ничего стоящего')
        print('Какая жалкая жизнь')
elif answ == 'нет':
    print('Вы переглядываетесь с разбойником и убегаете от греха подальше')
    print('"Мальчик, что ты забыл в этом лесу?" - кричит вам вслед разбойник')
    print('Какой позор!')
else:
    print('Вы невнятно пробормотали что-то')
    print('Разбойник странно посмотрел на вас и поспешил удалиться')
    print('Упс')

print('------------')
print('************')

print('На дороге вам снова встречается разбойник')
enemy2 = Rogue_ar('Питер', 15, 15, 15, 'арбалет')
enemy2.hello()
answ = input('Вы готовы размять свои кости и оружие? да/нет ').lower()
if answ == 'да':
    while enemy2.health > 0 and knight.health > 0:
        if randint(0,1) == 1:
            fighters = [knight, enemy2]
        else:
            fighters = [enemy2, knight]
        fighters[0].strike(fighters[1])
        fighters[0].attack(fighters[1])
    if enemy2.alive() == False:
        print(enemy2.name, 'умер от руки', knight.name)
        print('Какой вопиющий пример жестокости')
    elif knight.alive() == False:
        print('Вы бесславно погибаете, не успев достичь ничего стоящего')
        print('Какая жалкая жизнь.')
elif answ == 'нет':
    print('Вы переглядываетесь с разбойником и убегаете от греха подальше')
    print('"Мальчик, что ты забыл в этом лесу?" - кричит вам вслед разбойник')
    print('Какой позор!')
else:
    print('Вы невнятно пробормотали что-то')
    print('Разбойник странно посмотрел на вас и поспешил удалиться')
    print('Упс')

print('------------')
print('************')

print('На дороге вам снова встречается разбойник')
enemy4 = Rogue_mch('Нита', 20, 15, 10, 'меч')
enemy4.hello()
answ = input('Вы готовы размять свои кости и оружие? да/нет ').lower()
if answ == 'да':
    while enemy4.health > 0 and knight.health > 0:
        if randint(0, 1) == 1:
            fighters = [knight, enemy4]
        else:
            fighters = [enemy4, knight]
        fighters[0].strike(fighters[1])
        fighters[0].attack(fighters[1])
    if enemy3.alive() == False:
        print(enemy3.name, 'умер от руки', knight.name)
        print('Какой вопиющий пример жестокости')
    elif knight.alive() == False:
        print('Вы бесславно погибаете, не успев достичь ничего стоящего')
        print('Какая жалкая жизнь.')
elif answ == 'нет':
    print('Вы переглядываетесь с разбойником и убегаете от греха подальше')
    print('"Мальчик, что ты забыл в этом лесу?" - кричит вам вслед разбойник')
    print('Какой позор!')
else:
    print('Вы невнятно пробормотали что-то')
    print('Разбойник странно посмотрел на вас и поспешил удалиться')
    print('Упс')

print('Вы оглядываетесь и не видите никого живого в округе')
print('Похоже, что вы убили всех врагов поблизости')
print('О боже, вы слышите каие-то звуки из пещеры, похоже, что вы разбудили дракона')
print('Хотите ли вы сразиться с драконом.да/нет')
    if answ == 'lf'


