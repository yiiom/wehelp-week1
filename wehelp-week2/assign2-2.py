services = [
    {"name":"S1", "r":4.5, "c":1000},
    {"name":"S2", "r":3, "c":1200},
    {"name":"S3", "r":3.8, "c":800}
]

bookings = {
    "S1": [],
    "S2": [],
    "S3": []
}

def func2(ss, start, end, criteria):

    if ">=" in criteria:
        field, value = criteria.split(">=")
        operator = ">="
    elif "<=" in criteria:
        field, value = criteria.split("<=")
        operator = "<="
    else:
        field, value = criteria.split("=")
        operator = "="

    if field != "name":
        value = float(value)

    candidates = []

    for service in ss:

        if operator == "=":
            match = service[field] == value

        elif operator == ">=":
            match = service[field] >= value

        else:
            match = service[field] <= value

        if not match:
            continue

        conflict = False

        for s, e in bookings[service["name"]]:
            if start < e and end > s:
                conflict = True
                break

        if not conflict:
            candidates.append(service)

    if len(candidates) == 0:
        print("Sorry")
        return

    if operator == ">=":
        chosen = min(candidates, key=lambda x: x[field])
    elif operator == "<=":
        chosen = max(candidates, key=lambda x: x[field])
    else:
        chosen = candidates[0]

    print(chosen["name"])

    bookings[chosen["name"]].append((start, end))


func2(services, 15, 17, "c>=800")
func2(services, 11, 13, "r<=4")
func2(services, 10, 12, "name=S3")
func2(services, 15, 18, "r>=4.5")
func2(services, 16, 18, "r>=4")
func2(services, 13, 17, "name=S1")
func2(services, 8, 9, "c<=1500")