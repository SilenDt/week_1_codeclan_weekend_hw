# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    return pet_shop["name"] 

def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]

def add_or_remove_cash(pet_shop,num):
    pet_shop["admin"]["total_cash"] += num
    
def add_or_remove_cash(pet_shop,num):
    pet_shop["admin"]["total_cash"] += num

def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]

def increase_pets_sold(pet_shop,num):
    pet_shop["admin"]["pets_sold"] += num

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop,breed):
    given_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            given_breed.append(pet)
    return given_breed

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]

def remove_customer_cash(given_customer, num):
    given_customer["cash"] -= num

def get_customer_pet_count(given_customer):
    pet_count = len(given_customer["pets"])
    return pet_count

def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


#Optional:
def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        can_buy_pet = True
    return can_buy_pet

def customer_cant_afford_pet(customer, new_pet):
    if customer["cash"] < new_pet["price"]:
        can_buy_pet = False
    return can_buy_pet












