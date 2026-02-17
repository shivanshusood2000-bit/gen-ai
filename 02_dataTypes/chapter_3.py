# => Intergers , => Boolean , => Real , => Floating -> decimal , =>Complex Number 


# Intergers

black_tea_grams = 14
ginger_grams = 12

# addition
total  = black_tea_grams + ginger_grams
print(f"total grams of base tea is {total}")

# subtraction
remaining_tea = black_tea_grams - ginger_grams
print(f"remaining grams of base tea is {remaining_tea}")

# division
milk_litres = 7
servings = 4

milk_litres_per_serving = milk_litres / servings
print(f"litres of milk per serving is {milk_litres_per_serving}")

# division using two // will give us the quotient without the decimal part
total_tea_bas = 7
pots = 4

bags_per_pot = total_tea_bas // pots
print(f"bags per pot is {bags_per_pot}")  

# modulus using % will give us the remainder after division
total_cadamon_pods = 10
pods_per_cup = 3 

leftover_pods = total_cadamon_pods % pods_per_cup
print(f"leftover pods is {leftover_pods}")


# power using ** 
base_flavor_strength = 2
scale_factor = 3 

powerful_flavour = base_flavor_strength ** scale_factor
print(f"scale flavour strengeth is {powerful_flavour}")


# underscores in numbers 
total_tea_leaves_harvested = 1_000_000_000
print(f"total tea leaves harvested is {total_tea_leaves_harvested}")


#outputs

# total grams of base tea is 26
# remaining grams of base tea is 2
# litres of milk per serving is 1.75
# bags per pot is 1
# leftover pods is 1
# scale flavour strengeth is 8
# total tea leaves harvested is 1000000000