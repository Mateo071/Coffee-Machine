import data

is_on = True

def make_drink(ingredients, user_input):
  print(f"making {user_input}...")
  resources = data.RESOURCES

  if "milk" not in ingredients:
    ingredients["milk"] = 0

  resources["milk"] -= ingredients["milk"]
  resources["water"] -= ingredients["water"]
  resources["coffee"] -= ingredients["coffee"]

  print(f"Here is your {user_input}. Enjoy! 😁")

def print_report():
  print("printing report...")
  resources = data.RESOURCES
  water_level = resources["water"]
  milk_level = resources["milk"]
  coffee_level = resources["coffee"]
  money_collected = resources["capital"]

  print(f"Water: {water_level}ml.\nMilk: {milk_level}ml.\nCoffee: {coffee_level}g.\nMoney: ${format(money_collected, '.2f')}.")

def check_funds(price, quarters, dimes, nickels, cents):
  print("calculating amount paid...")
  amount_in_quarters = 0.25 * float(quarters)
  amount_in_dimes = 0.1 * float(dimes)
  amount_in_nickels = 0.05 * float(nickels)
  amount_in_cents = 0.01 * float(cents)
  amount_paid = amount_in_quarters + amount_in_dimes + amount_in_nickels + amount_in_cents
  print(f"Amount paid: ${format(amount_paid, '.2f')}")

  if amount_paid >= price:
    process_coins(price)
    give_change(amount_paid, price)
    return True
  else:
    print("Not enough funds. Your coins have been refunded. Please try again.")
    return False
  
def process_coins(amount_added):
  print("adding to money pool...")
  data.RESOURCES["capital"] += amount_added

def give_change(paid, price):
  print("calculating change...")
  change = round(paid - price, 2)
  total_change = change

  change_in_quarters = 0
  change_in_dimes = 0
  change_in_nickels = 0
  change_in_cents = 0

  while change >= 0.25:
    change -= 0.25
    change_in_quarters += 1

  while change >= 0.10:
    change -= 0.10
    change_in_dimes += 1

  while change >= 0.05:
    change -= 0.05
    change_in_nickels += 1

  while change > 0.00:
    change -= 0.01
    change_in_cents += 1

  print(f"Your change is {format(total_change, '.2f')}.\nQuarters: {change_in_quarters}\nDimes: {change_in_dimes}\nNickels: {change_in_nickels}\nPennies: {change_in_cents}")

def check_resources(ingredients):
  print("checking levels...")

  coffee_levels = data.RESOURCES["coffee"]
  milk_levels = data.RESOURCES["milk"]
  water_levels = data.RESOURCES["water"]

  coffee_required = ingredients["coffee"]
  water_required = ingredients["water"]
  if 'milk' in ingredients:
    milk_required = ingredients["milk"]
  else:
    milk_required = 0

  if coffee_levels >= coffee_required and water_levels >= water_required and milk_levels >= milk_required:
    return True
  else:
    if coffee_required > coffee_levels:
      print("Coffee levels too low. Please add more.")
    if water_required > water_levels:
      print("Water levels too low. Please add more.")
    if milk_required > milk_levels:
      print("Milk levels too low. Please add more.")
    return False

def turn_off():
  global is_on
  print("Turning off... Goodbye. 😴")
  is_on = False

def prompt():
  user_input = input("What would you like? (espresso/latte/cappuccino) ☕: ")
  if user_input == "latte" or user_input == "espresso" or user_input == "cappuccino":
    price = data.MENU[user_input]["cost"]
    ingredients = data.MENU[user_input]["ingredients"]



    have_ingredients = check_resources(ingredients)
    if have_ingredients:
      print(f"Your {user_input} will be ${format(price, '.2f')}")
      print("Please insert your coins.")
      quarters = input("How many quarters?: ")
      dimes = input("How many dimes?: ")
      nickels = input("How many nickels?: ")
      cents = input("How many cents?: ")
      can_afford = check_funds(price, quarters, dimes, nickels, cents)

    if can_afford and have_ingredients:
      if user_input == "latte" or user_input == "cappuccino" or user_input == "espresso":
        make_drink(ingredients, user_input)
  elif user_input == "report":
    print_report()
  elif user_input == "off":
    turn_off()
  else:
    print("Please enter a valid command.")

while is_on == True:
  prompt()


# TODO: 1. Print report of all coffee machine resources.
# TODO: 2.Check resources sufficient to make drink order.