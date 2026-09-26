# --- Arithmetic ---

base_fare    = 18.50
passengers   = 43
stops        = 11
capacity     = 60

extra_stops  = stops - 5               # stops beyond the first 5
extra_charge = extra_stops * 2.50      # ₹2.50 per extra stop
total_fare   = base_fare + extra_charge
load_pct     = (passengers / capacity) * 100   # bus load percentage
stop_blocks  = stops // 3              # every 3 stops = 1 pricing block
leftover     = stops % 3               # stops that don't fill a full block

print("=== Arithmetic Results ===")
print(f"Extra stops  : {extra_stops}")
print(f"Extra charge : ₹{extra_charge}")
print(f"Total fare   : ₹{total_fare}")
print(f"Bus load     : {load_pct:.1f}%")
print(f"Pricing blocks: {stop_blocks}, leftover stops: {leftover}")
# --- Comparison ---
is_crowded       = passengers > 40         # True
is_free          = total_fare == 0         # False
needs_extra_bus  = load_pct >= 90          # True/False depending on load

print("\n=== Comparison Results ===")
print(f"Is crowded?       {is_crowded}")
print(f"Is free ride?     {is_free}")
print(f"Needs extra bus?  {needs_extra_bus}")

# --- Logical ---
is_peak          = True
is_student       = False
is_senior        = True

apply_surge      = is_peak and is_crowded          # surge: peak AND crowded
apply_concession = is_student or is_senior         # concession: either
full_fare        = not (is_student or is_senior)   # full fare if neither

print("\n=== Logical Results ===")
print(f"Apply surge?      {apply_surge}")
print(f"Apply concession? {apply_concession}")
print(f"Full fare?        {full_fare}")

# --- Assignment shortcuts ---
daily_revenue = 0
daily_revenue += 795.50    # morning trips
daily_revenue += 1240.00   # afternoon trips
daily_revenue -= 50.00     # refunds
daily_revenue *= 1.05      # apply 5% GST
print(f"\nDaily revenue (incl. GST): ₹{daily_revenue:.2f}")

