import math

def validate_height_and_fastpass(rider_spec):
    if not isinstance(rider_spec, str):
        return "Invalid input: expected text like 140:YES"
    parts = rider_spec.strip().split(':')
    if len(parts) != 2:
        return "Invalid input: expected format Height:FastPass"
    height_str, pass_str = parts
    try:
        height = int(height_str.strip())
    except ValueError:
        return "Invalid input: height must be a whole number"
    if height <= 0 or height > 300:
        return "Invalid input: height out of range"
    pass_map = {"YES": True, "NO": False}
    key = pass_str.strip().upper()
    if key not in pass_map:
        return "Invalid input: FastPass must be YES or NO"
    eligible = height >= 120
    status = "FastPass Priority" if pass_map[key] else "Standard Entry"
    return f"Height {height}cm: {'Approved' if eligible else 'Denied'} ({status})"

def compute_dispatch_throughput(ride_metric_str):
    if not isinstance(ride_metric_str, str):
        return None
    parts = ride_metric_str.split('/')
    if len(parts) != 2:
        return None
    try:
        riders = float(parts[0])
        cycle_mins = float(parts[1])
    except ValueError:
        return None
    if not (math.isfinite(riders) and math.isfinite(cycle_mins)):
        return None
    if cycle_mins <= 0 or riders < 0:
        return None
    return round(riders / cycle_mins, 2)

def resolve_safety_restraint_code(zone_code):
    if not isinstance(zone_code, str):
        return "Unknown"
    prefix = zone_code.strip().upper()[:3]
    restraint_types = {
        "CST": "Over-the-Shoulder Harness",
        "WTR": "Lap Bar and Seatbelt",
        "DRP": "Hydraulic Shoulder Vest",
        "WHL": "Manual Safety Bar"
    }
    return restraint_types.get(prefix, "Unknown")


def main():
    print("==== Running validate_height_and_fastpass ====")
    r_input = input("Enter rider spec (Height:FastPass, e.g. 140:YES): ")
    print(validate_height_and_fastpass(r_input))

    print("\n==== Running compute_dispatch_throughput ====")
    t_input = input("Enter riders/mins (e.g. 48/2.5): ")
    print("Throughput (riders/min):", compute_dispatch_throughput(t_input))

    print("\n==== Running resolve_safety_restraint_code ====")
    z_input = input("Enter ride zone code (e.g. CST_01, WTR_A): ")
    print("Restraint:", resolve_safety_restraint_code(z_input))

if __name__ == "__main__":
    main()