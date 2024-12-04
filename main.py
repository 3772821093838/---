import random

inventory = []

def show_inventory():
    print("\nВаш инвентарь:")
    if inventory:
        for item in inventory:
            print(f"- {item}")
    else:
        print("Ваш инвентарь пуст.")

def battle(enemy, weapon, enemy_health_start=10, player_health_start=10):
    enemy_health = enemy_health_start
    player_health = player_health_start
    print(f"\nВы столкнулись с {enemy}! Его здоровье: {enemy_health}")
    print(f"Ваше здоровье: {player_health}")
    resurrection_used = False

    while enemy_health > 0 and player_health > 0:
        print("\nВыберите действие:")
        print("1. Атаковать")
        print("2. Защищаться")
        print("3. Использовать предмет")
        print("4. Бежать (только если у вас достаточно выносливости)")

        choice = input("> ").lower()

        if choice == "1":
            damage = random.randint(1, 3)
            if weapon == "меч":
                damage += 2
            elif weapon == "дубинка":
                damage += 1
            elif weapon == "кинжал":
                damage += 2
            enemy_health -= damage
            print(f"Вы нанесли {damage} урона! Осталось здоровья у врага {enemy_health}")
            if enemy_health <= 0:
                print(f"Вы победили {enemy}!")
                break
            enemy_damage = random.randint(1, 1) #Уменьшен урон врага
            player_health -= enemy_damage
            print(f"{enemy} нанес вам {enemy_damage} урона!")

        elif choice == "2":
            print("Вы приготовились к защите!")
            enemy_damage = random.randint(0, 1)
            player_health -= enemy_damage
            print(f"{enemy} нанес вам {enemy_damage} урона!")

        elif choice == "3":
            show_inventory()
            if inventory:
                item_choice = input("Выберите предмет: ").lower()
                if item_choice in inventory:
                    if item_choice == "зелье исцеления":
                        heal_amount = 5
                        player_health = min(player_health + heal_amount, player_health_start)
                        print(f"Вы выпили зелье и восстановили {heal_amount} здоровья!")
                        inventory.remove("зелье исцеления")
                    elif item_choice == "свиток воскрешения" and not resurrection_used:
                        resurrection_used = True
                        player_health = player_health_start
                        print("Вы использовали свиток воскрешения!")
                        inventory.remove("свиток воскрешения")
                    elif item_choice == "дубинка":
                        print("Вы используете дубинка,+1 к атаке.")
                    elif item_choice == "меч":
                        print("Вы используете меч, +2 к атаке.")
                    elif item_choice == "кинжал":
                        print("Вы используете кинжал, +2 к атаке.")
                    else:
                        print("Этот предмет нельзя использовать в бою.")
                else:
                    print("У вас нет такого предмета.")
            else:
                print("Ваш инвентарь пуст.")
            enemy_damage = random.randint(1, 1) #Уменьшен урон врага
            player_health -= enemy_damage
            print(f"{enemy} нанес вам {enemy_damage} урона!")

        elif choice == "4":
            if player_health > 5:
                print("Вы успешно сбежали!")
                break
            else:
                print("У вас недостаточно выносливости для побега!")
                enemy_damage = random.randint(1, 1) #Уменьшен урон врага
                player_health -= enemy_damage
                print(f"{enemy} нанес вам {enemy_damage} урона!")

        else:
            print("Неверный выбор.")

        if player_health <= 0 and not resurrection_used:
            print("Вы проиграли!")
            exit()
        elif player_health <= 0 and resurrection_used:
            print("Вы использовали свиток воскрешения!")
            player_health = player_health_start


def riddle1():
    print("\nЗагадка 1: У меня много глаз, но я не вижу. Что я?")
    answer = input("> ").lower()
    if answer == "картофель":
        print("Правильно! Ты получил ключ.")
        inventory.append("ключ")
        return True
    else:
        print("Неправильно. Попробуй ещё раз!")
        return False

def riddle2():
    print("\nЗагадка 2: Что имеет шею, но головы нет?")
    answer = input("> ").lower()
    if answer == "бутылка":
        print("Правильно! Ты получил дубинку.")
        inventory.append("дубинка")
        return True
    else:
        print("Неправильно. Попробуй ещё раз!")
        return False

def riddle3():
    print("\nЗагадка 3: Что становится мокрее, когда сохнет?")
    answer = input("> ").lower()
    if answer == "полотенце":
        print("Правильно! Ты получил волшебный меч!")
        inventory.append("меч")
        return True
    else:
        print("Неправильно. Попробуй ещё раз!")
        return False

def riddle1_hint():
    print("\nПодсказка 1: Ты можешь это приготовить.")

def riddle2_hint():
    print("\nПодсказка 2:  Может быть стеклянным или пластиковым, часто содержит жидкость.")

def riddle3_hint():
    print("\nПодсказка 3: Используется после душа.")

def ask_for_hint(riddle_number):
    if riddle_number == 1:
        if "hint1_used" not in inventory:
            riddle1_hint()
            inventory.append("hint1_used")
        else:
            print("Вы уже использовали подсказку к этой загадке.")
    elif riddle_number == 2:
        if "hint2_used" not in inventory:
            riddle2_hint()
            inventory.append("hint2_used")
        else:
            print("Вы уже использовали подсказку к этой загадке.")
    elif riddle_number == 3:
        if "hint3_used" not in inventory:
            riddle3_hint()
            inventory.append("hint3_used")
        else:
            print("Вы уже использовали подсказку к этой загадке.")
    else:
        print("Неверный номер загадки.")


def level1():
    print("\nУровень 1: Древний замок.  Вы видите полуразрушенную башню.")
    print("В темноте вы слышите шорохи.")
    print("Перед вами загадка.")
    while not riddle1():
        ask_hint = input("Хотите подсказку? (да/нет): ").lower()
        if ask_hint == "да":
            ask_for_hint(1)
        elif ask_hint != "нет":
            print("Неверный ввод.")

    print("\nВы открыли дверь в темный коридор.  В конце виднеется свет.")
    battle("призрак", "руки", enemy_health_start=10, player_health_start=14)


def level2():
    print("\nУровень 2: Заброшенная шахта.  Холодный ветер проносится сквозь трещины в стенах.")
    print("Вы видите узкий проход, ведущий вглубь шахты.")
    print("Перед вами загадка.")
    while not riddle2():
        ask_hint = input("Хотите подсказку? (да/нет): ").lower()
        if ask_hint == "да":
            ask_for_hint(2)
        elif ask_hint != "нет":
            print("Неверный ввод.")

    print("\nТы пробил путь дальше.")
    battle("крыса", "дубинка", enemy_health_start=6, player_health_start=12)
    inventory.append("зелье исцеления")
    inventory.append("кинжал")
    print("Вы нашли зелье исцеления и кинжал!")


def level3():
    print("\nУровень 3: Пещера с сокровищами.  Воздух влажный и тяжелый.")
    print("Вы чувствуете запах серы и слышите отдаленное рычание.")
    print("Перед вами загадка.")
    while not riddle3():
        ask_hint = input("Хотите подсказку? (да/нет): ").lower()
        if ask_hint == "да":
            ask_for_hint(3)
        elif ask_hint != "нет":
            print("Неверный ввод.")

    print("\nТы готов к финальной битве!")
    inventory.append("свиток воскрешения")
    print("Вы нашли свиток воскрешения!")
    battle("дракон", "меч", enemy_health_start=22, player_health_start=18)


def play_game():
    current_level = 1
    while current_level <= 3:
        if current_level == 1:
            level1()
        elif current_level == 2:
            level2()
        elif current_level == 3:
            level3()
        current_level += 1

print("Добро пожаловать в текстовую новеллу!")
print("Вы находитесь в темном лесу. Перед вами начинается ваш путь.")

play_game()

print("\nПоздравляем! Вы прошли игру!")