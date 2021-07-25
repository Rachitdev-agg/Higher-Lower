import random
import art
import game_data
from replit import clear
score = 0
def chose_a():
  a = random.choice(game_data.data)
  return a
def chose_b():
  b = random.choice(game_data.data)
  return b
value_a = chose_a()
value_b = chose_b()
def comparing(a, b):
  clear()
  global score
  print(art.logo)
  if score > 0:
    print(f"You are right! Current score: {score}")

  name = a["name"]
  description = a["description"]
  country = a["country"]
  follower_count_a = a["follower_count"]
  print(f"Compare A: {name}, {description}, from {country}")

  print(art.vs)

  name1 = b["name"]
  description1 = b["description"]
  country1 = b["country"]
  follower_count_b = b["follower_count"]
  print(f"Compare B: {name1}, {description1}, from {country1}")

  guess = (input("Who has more followers? Type A or B: ")).lower()
  if guess == "a":
    if follower_count_a > follower_count_b:
      score += 1
      b = chose_b()
      comparing(a, b)
    else:
      clear()
      print(art.logo)
      print(f"Sorry that's wrong. Final score: {score}")
  if guess == "b":
    if follower_count_b > follower_count_a:
      score += 1
      a = chose_a()
      comparing(a, b)
    else:
      clear()
      print(art.logo)
      print(f"Sorry that's wrong. Final score: {score}")

comparing(value_a, value_b)