def online_count(statues):
    count = 0
    for the_state in statues.values():
        if the_state == "online":
            count += 1
    return count
statues = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
print(online_count(statues))