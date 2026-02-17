spice_mix = set()

print(f"Inital spice mix id: {id(spice_mix)}")

spice_mix.add("Ginger")
spice_mix.add("cardmom")

print(f"After spice mix id: {id(spice_mix)}")

print(f"Inital spice mix id: {(spice_mix)}")


# numbers are immutable , only reference can be changed but not the value itself
# sets are mutable, we can change the value but the reference will remain same