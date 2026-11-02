# simple reflex agent for a vacuum cleaner environment

def vacuum_agent(location, status):
    if status == "dirty":
        return 'suck'
    elif location == "A":
        return 'right'
    else:
        return 'left'

# environment
rooms= {"A":"dirty", "B":"dirty"}
location="A"

print("initial environment:", rooms)

for i in range(2):
    status=rooms[location]
    action=vacuum_agent(location, status)

    print("location:",location, "status:", status, "action:",action)

    if action == 'suck':
        rooms[location]='clean'
    elif action == 'right':
        location='B'
    else:
        location='A'

        if all(status=='clean' for status in rooms.values()):
            print("all rooms cleaned")
            break

print("final environment:",rooms)

print("end")