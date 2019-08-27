#This program is to test if a person is eligible for presidency in the U.S
#The person must be at least 35 years old, must be a U.S citizen, and must stay in the U.S for at least 14 years to be eligible for U.S presidency 

age = input ("How old are you?")
citizen = input ("Born in the U.S?")
years_of_residency = input ("How long have you been a resident in the U.S?")

if age >= "35" and citizen == "yes" and years_of_residency >= "14 years":
    print ("You are eligible to run for president!")
else:
    print ("You are not eligible to run for president.")
