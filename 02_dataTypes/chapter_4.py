#boolean

#0 means false and 1 means true

is_boiling = True
stri_count = 5

total_actions = is_boiling + stri_count #upcasting
print(f"total actions is {total_actions}")

milk_present = 0 # "0" no milk i.e false  "1" milk i.e true
print(f"milk present is {bool(milk_present)}")


# And , Or , Not

# tea and cookies , means need both to be true
# tea or cookies , means either of them can be true
# not tea , means tea is false



water_hot = True 
tea_added = False 

can_server = water_hot and tea_added
print(f"can server is {can_server}")

can_server = water_hot or tea_added
print(f"can server is {can_server}")

can_server = not water_hot
print(f"can server is {can_server}")


#outputs

# total actions is 6
# milk present is False
# can server is False
# can server is True
# can server is False