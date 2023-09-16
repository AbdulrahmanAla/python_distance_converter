###########################################################
#
#    Programming Project #1
#
#     Prompts for input
#
#     Performs arithmetic
#
#     Display the results rounded 3 decimal places for the conversions
#
###########################################################


# Input statement for the given rods by the user and its converstions to different units
rods= float(input("Input rods: \n"))

meters= rods * 5.0292

feet= rods * 16.5

miles= meters /1609.34

Furlongs= rods/40

avg_walking_speed= (miles/3.1)*60


#Print statements for how many rods were given and its converstions rounded to 3 decimeal places
print("You input",rods,"rods.\n")

print("Conversions")
print("Meters:",round(meters,3))
print("Feet:",round(feet,3))
print("Miles:",round(miles,3))
print("Furlongs:",round(Furlongs,3))
print("Minutes to walk",rods,"rods:",round(avg_walking_speed,3))