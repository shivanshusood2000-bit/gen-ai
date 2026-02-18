# Lists are mutable with methods like append, remove, extend, insert, pop etc.


ingredients = ["water", "milk", "black tea"]
ingredients.append("sugar")

print(ingredients)
ingredients.remove("water")
print(ingredients)


spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water","milk"]

chai_ingredients.extend(spice_options)
print(chai_ingredients)

new_ingredients = ["water", "milk", "black tea"]
new_ingredients.insert(2,"tea")
print(new_ingredients)



print(new_ingredients.pop())


#sort reverse sort
new_ingredients.sort()
print(new_ingredients)
new_ingredients.reverse()
print(new_ingredients)



sugar_levels = [1,2,3,4,5,6,-1,-3]

print (f"Maximun suagr level : {max(sugar_levels)}")
print (f"Minimun suagr level : {min(sugar_levels)}")



#operator overloading 


base_liquid = ["water","milk"]
extras = ["sugar"]

full_mix = base_liquid + extras
print(full_mix)


strong = base_liquid * 3
print(strong)



# "CINNAMON" TO LIST


raw_spice_data = bytearray(b"CINNAMON")
print(raw_spice_data)

