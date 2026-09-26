import os
os.system('cls')

print("=== City Smart Route Data ===")

route_number = 12
num_stops = 18
passengers = 48

print(f"route_number   = {route_number:<14} | type = {type(route_number).__name__}")
print(f"num_stops      = {num_stops:<14} | type = {type(num_stops).__name__}")
print(f"passengers     = {passengers:<14} | type = {type(passengers).__name__}")

base_fare = 18.50
distance_km = 7.3
fuel_cost = 4.75

print(f"base_fare      = {base_fare:<14} | type = {type(base_fare).__name__}")
print(f"distance_km    = {distance_km:<14} | type = {type(distance_km).__name__}")
print(f"fuel_cost      = {fuel_cost:<14} | type = {type(fuel_cost).__name__}")

route_name = "12A Express"
stop = "Central"

print(f"route_name     = {route_name:<14} | type = {type(route_name).__name__}")
print(f"stop           = {stop:<14} | type = {type(stop).__name__}")

is_peak_hour = True
is_ac_bus = False
is_accessible = True  # wheelchair

print(f"is_peak_hour   = {is_peak_hour:<14} | type = {type(is_peak_hour).__name__}")
print(f"is_ac_bus      = {is_ac_bus:<14} | type = {type(is_ac_bus).__name__}")
print(f"is_accessible  = {is_accessible:<14} | type = {type(is_accessible).__name__}")

is_ac = "False"
print(f"is_ac          = {is_ac:<14} | type = {type(is_ac).__name__}")

user_input = input("Enter the value you want:")
print(f"user_input          = {user_input:<14} | type = {type(user_input).__name__}")
try:
    user_input += 1
except:
    print('Some error')
user_input_1 = int(input("Enter the value you want:"))
user_input_1 += 1
print(f"user_input_1          = {user_input_1:<14} | type = {type(user_input_1).__name__}")

print("bool(0)     →", bool(0),     "because 0 is considered False in Python")
print("bool(0.0)   →", bool(0.0),   "because 0.0 is also treated as False")
print("bool(0.1)   →", bool(0.1),   "because any non‑zero float is True")

print("bool(1)     →", bool(1),     "because any non‑zero integer is True")
print("bool(2)     →", bool(2),     "because non‑zero integers evaluate to True")
print("bool(3)     →", bool(3),     "because non‑zero integers evaluate to True")
print("bool(4)     →", bool(4),     "because non‑zero integers evaluate to True")

print("bool('')    →", bool(""),    "because an empty string is False")
print("bool('a')   →", bool("a"),   "because any non‑empty string is True")

while True:
    a = input("Enter the value you want:")
    if a.isnumeric():
        break
    else:
        print("Please only enter digits")