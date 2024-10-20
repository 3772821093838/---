import time
import random

def print_with_pause(text, pause_time=1):
  """Печатает текст с паузой между словами."""
  for word in text.split():
    print(word, end=" ", flush=True)
    time.sleep(pause_time)
  print()

def start_game():
  """Начало игры."""
  print_with_pause("Ты, студент, заходишь в уютное кафе, чтобы выпить чашечку любимого кофе.")
  print_with_pause("На диване уютно разлегся милый кот.")
  print_with_pause("Ты решаешь познакомиться с ним.")
  play_with_cat()

def play_with_cat():
  """Функция для взаимодействия с котом."""

  actions = [
    "Погладить кота за ушком.",
    "Предложить коту кофе.",
    "Сделать селфи с котом.",
  ]

  while actions:
    print_with_pause("Что ты хочешь сделать с котиком?")
    for i, action in enumerate(actions):
      print(f"{i+1}. {action}")

    choice = input("Введи номер действия: ")

    try:
      choice_index = int(choice) - 1
      if 0 <= choice_index < len(actions):
        action = actions.pop(choice_index)
        print_with_pause(f"Ты {action}")
        print()
        if action == "Погладить кота за ушком.":
          pet_cat()
        elif action == "Предложить коту кофе.":
          offer_coffee()
        elif action == "Сделать селфи с котом.":
          take_selfie()
      else:
        print_with_pause("Неверный выбор. Попробуй еще раз.")
    except ValueError:
      print_with_pause("Неверный ввод. Попробуй ввести число.")

  print_with_pause("Ты хотел еще побыть с котиком, но у тебя почти не осталось времени и тебе уже пора уезжать по делам.")

def pet_cat():
  """Погладить кота."""
  print_with_pause("Ты нежно гладишь кота по голове. Он мурлычет от удовольствия и трется о твою руку.")

def offer_coffee():
  """Предложить коту кофе."""
  print_with_pause("Ты поднимаешь чашку с кофе и предлагаешь ее коту.")
  print_with_pause("Кот смотрит на тебя с интересом, но, конечно, отказывается. Он просто трется о твою ногу.")

def take_selfie():
  """Сделать селфи с котом."""
  print_with_pause("Ты делаешь селфи с котом. Получается милая фотография.")
  print_with_pause("Кот смотрит на тебя с интересом.")

if __name__ == "__main__":
  start_game()

