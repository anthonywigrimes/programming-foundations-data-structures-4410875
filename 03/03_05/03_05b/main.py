user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}

def update_preferences(user_pref):
    new_preferences = {}
    for key, item in user_pref.items():
        if item != None:
            new_preferences[key] = item
    return new_preferences

print(update_preferences(user_preferences))
