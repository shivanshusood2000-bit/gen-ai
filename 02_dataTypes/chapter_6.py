#strings are immutable 


chai_type = "Ginger chai"
customer_name = "priya"

print(f"Order for {customer_name} : {chai_type} please !")


chai_description = "Aromatic and Bold"

print(f"Word :  {chai_description[::4]}")

# [Start : End : Step] 
# {chai_description[0:8:]} => "Aromatic"
# {chai_description[0:8:2]} => "Aoai"
# {chai_description[0:8:3]} => "Ami"
# {chai_description[::4]} => "Ar"