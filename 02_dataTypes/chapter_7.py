# Tuples -> immutable 

masala_spices = ("cardamom" ,"cloves" , "cinnamon")

# destructureing a tuple
(spice1, spice2, spice3) = masala_spices

print(f"Spice 1 : {spice1} , Spice 2 : {spice2} , Spice 3 : {spice3}")

ginger_ratio, cardmon_ratio = 2, 3 
print(f"Ratio is G {ginger_ratio} and C : {cardmon_ratio}")

# flipped ratio 

ginger_ratio, cardmon_ratio =  cardmon_ratio, ginger_ratio
print(f"Ratio is G {ginger_ratio} and C : {cardmon_ratio}")


#membership 

print(f"is Ginger in masala spice?  {'ginger' in masala_spices}") #false
print(f"is Cinnamon in masala spice?  {'cinnamon' in masala_spices}") #true but case sensitive
print(f"is Cinnamon in masala spice?  {'cinnamon' not in masala_spices}") #false