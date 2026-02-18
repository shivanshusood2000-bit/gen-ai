#sets are mutable 

essential_spices = {"cardamom","ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

#union
all_spices = essential_spices.union(optional_spices)
all_spices = essential_spices | optional_spices
print(all_spices)

#intersection
common_spices = essential_spices & optional_spices
print('intersection' , common_spices)


#only in essential

only_in_essential = essential_spices - optional_spices
print('only in essential' , only_in_essential)


#membership test
print(f"is 'cloves' in essential spices ? {'cloves' in optional_spices}")


