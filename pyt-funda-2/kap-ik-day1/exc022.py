# Given trip details:
route_id        = 5
passengers      = 67
stops_travelled = 14
bus_capacity    = 80
base_fare       = 20.00
is_ac           = True
is_peak         = True
student_count   = 12    # of the 67 passengers, 12 are students
senior_count    = 8     # 8 are senior citizens

# --- TASK 1: Basic fare components ---
# Extra stops cost ₹3 each (beyond the first 5 stops)
extra_stops     = stops_travelled - 5
extra_fare      = extra_stops * 3
full_adult_fare = base_fare + extra_fare   # base_fare + extra_fare

# --- TASK 2: Surcharges ---
# AC surcharge: ₹8 flat (only if AC bus)
# Peak surcharge: 15% on the full_adult_fare (only if peak hour)
ac_surcharge    = 8 * is_ac   # use a logical expression — no if/else yet!
                        # Hint: True * 8 == 8, False * 8 == 0
peak_surcharge  = 0.15 * (full_adult_fare * is_peak)   # 15% of full_adult_fare, only if peak
total_adult_fare = full_adult_fare + ac_surcharge + peak_surcharge  # full_adult_fare + ac_surcharge + peak_surcharge

#---TASK 3: Concession fares ---

# Students pay 50% of total_adult_fare
# Seniors pay 40% of total_adult_fare
regular_passengers = passengers - student_count - senior_count
student_fare    = total_adult_fare * 0.5   # 50% of total_adult_fare
senior_fare     = total_adult_fare * 0.4   # 40% of total_adult_fare

#--- TASK 4: Total trip revenue ---
revenue_regular  = regular_passengers * total_adult_fare  # regular_passengers × total_adult_fare
revenue_students = student_count * student_fare  # student_count × student_fare
revenue_seniors  = senior_count * senior_fare  # senior_count × senior_fare
total_revenue    = revenue_regular + revenue_students + revenue_seniors  # sum of all three

#--- TASK 5: Load analysis ---
load_percentage = passengers / bus_capacity * 100   # passengers as % of capacity
is_overcrowded  = load_percentage > 100   # True if load_percentage > 100
is_surge_zone   = is_peak and load_percentage > 80   # True if is_peak AND load_percentage > 80
# Print your results:
print(f"Route {route_id} | {passengers} passengers | {stops_travelled} stops")
print(f"Adult fare : ₹{total_adult_fare:.2f}")
print(f"Student fare: ₹{student_fare:.2f}")
print(f"Senior fare : ₹{senior_fare:.2f}")
print(f"Total revenue: ₹{total_revenue:.2f}")
print(f"Load: {load_percentage:.1f}% | Overcrowded: {is_overcrowded} | Surge zone: {is_surge_zone}")