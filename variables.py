#Playing with variables.

cars = 100
space_in_Car = 5
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_Car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "available"
print "There are only", drivers, "drivers available"
print "There will therefore be", cars_not_driven, "empty cars today"
