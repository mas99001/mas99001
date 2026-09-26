raw_route_id      = "7"          # should become: int
raw_route_name    = "Harbour Express"  # should become: str
raw_passengers    = "52"         # should become: int
raw_base_fare     = "22.50"      # should become: float
raw_stops_taken   = "9"          # how many stops the passenger travelled - int
raw_is_student    = "1"          # 1 = student, 0 = regular passenger - bool
raw_is_ac         = "0"          # 1 = AC bus, 0 = non-AC
#--- TASK 1: Cast each variable to the correct type ---
route_id     = int(raw_route_id)     # whole number
route_name   = raw_route_name        # already a string, no cast needed
passengers   = int(raw_passengers)   # whole number
base_fare    = float(raw_base_fare)     # decimal number
stops_taken  = int(raw_stops_taken)  # whole number
is_student   = bool(int(raw_is_student))  # True/False (hint: two-step cast)
is_ac        = bool(int(raw_is_ac))        # True/False
#--- TASK 2: Calculate the total fare ---
#Rules:
#- Base fare applies for the first 5 stops
#- Each additional stop costs ₹2.50 extra
#- Students get a 50% discount on the total
#bold text - AC buses add ₹5 flat surcharge (applied AFTER student discount)
extra_stops  = max(stops_taken-5,0)                   # stops beyond the first 5 (min 0)
extra_cost   = extra_stops*2.5                   # extra_stops × 2.50
total_before_discount = base_fare + extra_cost          # base_fare + extra_cost
discount = total_before_discount * 0.5 if is_student else 0 # 50% if student else 0
fare_after_discount = total_before_discount - discount            # total_before_discount - discount
ac_surcharge = 5 if is_ac else 0                   # 5 if AC bus else 0
final_fare   = fare_after_discount + ac_surcharge                  # fare_after_discount + ac_surcharge

#print(f'Final fare is : {final_fare} for the route {raw_route_name}')
#--- TASK 3: Print a receipt ---
print(f'   ###   ============================')
print(f'   ##    CITYSMART TRIP RECEIPT')
print(f'   ###   ============================')
print(f'   ###   Route     : {route_id} - {route_name}')
print(f'   ###   Passengers: {passengers}')
print(f'   ###   Stops     : {stops_taken}')
'''
print(f'   ###   Student?  : {"Yes" if is_student else "No"}')
print(f'   ###   AC Bus?   : {"Yes" if is_ac else "No"}')
'''
print(f'   ###   Student?  : {"Yes" * is_student + "No" * (1 - is_student)}')
print(f'   ###   AC Bus?   : {"Yes" * is_ac + "No" * (1 - is_ac)}')
print('   ###   '+"-"*28)
print(f'   ###   Base fare : ₹{base_fare:.2f}')
print(f'   ###   Extra     : ₹{extra_cost:.2f}')
print(f'   ###   Discount  : -₹{discount:.2f}')
print(f'   ###   AC charge : ₹{ac_surcharge:.2f}')
print(f'   ###   TOTAL     : ₹{final_fare:.2f}')
print(f'   ###   ============================')
