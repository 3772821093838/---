import random

# Словарь с описанием персонажей
characters = {
    "рыцарь": "храбрый и сильный воин, вооруженный мечом и щитом",
    "маг": "мощный волшебник, способный управлять магией",
    "воин": "опытный боец, вооруженный топором и щитом",
    "лучник": "ловкий стрелок, метко поражающий врагов издалека"
}

# Список возможных действий
actions = ["атаковать", "защищаться", "использовать магию", "бежать", "использовать стрелы"]

# Кортеж с описанием монстров
monsters = (
    ("Гоблин", 5, 2, "слабый противник"),
    ("Огр", 10, 4, "сильный и грубый"),
    ("Дракон", 20, 8, "мощный и опасный"),
    ("Скелет-воин", 7, 3, "быстрый и живучий"),
    ("Ведьма", 6, 2, "опасна своей магией")
)

# Функция для выбора персонажа
def choose_character():
    print("Выберите своего персонажа:")
    for i, character in enumerate(characters.keys()):
        print(f"{i+1}. {character} ({characters[character]})")
    while True:
        choice = input("Введите номер персонажа: ")
        if choice.isdigit() and 1 <= int(choice) <= len(characters):
            return list(characters.keys())[int(choice)-1]
        else:
            print("Неверный ввод. Пожалуйста, введите номер персонажа.")

# Функция для описания ситуации
def describe_situation(level, monster):
    print(f"\n--- Уровень {level} ---")
    print(f"Вы столкнулись с {monster[0]}!")
    print(f"У него {monster[1]} очков здоровья.")

# Функция для хода игрока
def player_turn(player_hp, monster_hp, monster):
    print("\nВыберите действие:")
    for i, action in enumerate(actions):
        print(f"{i+1}. {action}")
    while True:
        choice = input("Введите номер действия: ")
        if choice.isdigit() and 1 <= int(choice) <= len(actions):
            action = actions[int(choice)-1]
            if action == "атаковать":
                attack_damage = random.randint(1, 5)
                monster_hp -= attack_damage
                print(f"Вы атаковали {monster[0]} и нанесли {attack_damage} урона!")
            elif action == "защищаться":
                print(f"Вы защищаетесь.")
            elif action == "использовать магию":
                if player_hp < 5:
                    print("У вас недостаточно маны!")
                else:
                    magic_damage = random.randint(3, 7)
                    monster_hp -= magic_damage
                    player_hp -= 5
                    print(f"Вы использовали магию и нанесли {magic_damage} урона!")
            elif action == "использовать стрелы":
                if characters == "лучник":
                    arrow_damage = random.randint(2, 6)
                    monster_hp -= arrow_damage
                    print(f"Вы выпустили стрелу и нанесли {arrow_damage} урона!")
                else:
                    print(f"У вас нет стрел!")
            elif action == "бежать":
                print(f"Вы пытаетесь убежать...")
                if random.random() < 0.5:
                    print("Вам удалось убежать!")
                    return False
                else:
                    print(f"Вам не удалось убежать!")
            return player_hp, monster_hp
        else:
            print("Неверный ввод. Пожалуйста, введите номер действия.")

# Функция для хода монстра
def monster_turn(player_hp, monster_hp, monster):
    monster_attack = random.randint(1, monster[2])
    player_hp -= monster_attack
    print(f"{monster[0]} атаковал вас и нанес {monster_attack} урона!")
    return player_hp, monster_hp

# Основная функция игры
def play_game():
    character = choose_character()
    print(f"\nВы выбрали персонажа {character}!")
    player_hp = 10
    level = 1
    while level <= 3:
        monster = monsters[level-1]
        describe_situation(level, monster)
        monster_hp = monster[1]
        while player_hp > 0 and monster_hp > 0:
            player_hp, monster_hp = player_turn(player_hp, monster_hp, monster)
            if monster_hp > 0:
                player_hp, monster_hp = monster_turn(player_hp, monster_hp, monster)
        if player_hp <= 0:
            print(f"\n{monster[0]} победил вас!")
            break
        else:
            print(f"\nВы победили {monster[0]}!")
            level += 1
    if level > 3:
        print("\nПоздравляю, вы прошли все уровни!")
play_game()
