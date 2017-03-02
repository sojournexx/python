#Andrew Tan, 1/31, Section 010, Math Expressions

#Storing calculated values to variables
conv = 0.621
lightspeed = 299792.458
miles_lightspeed = lightspeed * conv
half_miles_lightspeed = miles_lightspeed * 0.5
quarter_miles_lightspeed = miles_lightspeed * 0.25
revolution = 66600
km_revolution = revolution / conv / 60 / 60
revolution_pct = format(km_revolution / lightspeed, ".15e")

#formatting 38s strings
L1 = format("Speed of light (Kilometers / sec):", "<38s")
L2 = format("Speed of light (Miles / sec):", "<38s")
L3 = format("Half speed of light (Miles / sec):", "<38s")
L4 = format("Quarter speed of light (Miles / sec):", "<38s")
L5 = format("66,000 miles per hour is equal to:", "<38s")
L6 = L5

#printing output
print(L1, lightspeed, "kps")
print(L2, miles_lightspeed, "mps")
print(L3, half_miles_lightspeed, "mps")
print(L4, quarter_miles_lightspeed, "mps")
print()
print("The earth moves 66,000 miles / hour around the sun")
print(L5, km_revolution, "kps")
print(L6, revolution_pct, "% of the speed of light")
