test_settings = {
    "theme": "dark",
    "notifications": "enabled"
    }

def add_setting(settings_dictionary, tupla_key_value):
    key, value = tupla_key_value
    key = key.lower()
    value = value.lower()
    if key in settings_dictionary:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."
    else:
        settings_dictionary[key] = value
        return f"Setting '{key}' added with value '{value}' successfully!"

def update_setting(settings_dictionary, tupla_key_value):
    key, key_value = tupla_key_value
    key = key.lower()
    key_value = key_value.lower()
    if key in settings_dictionary:
        settings_dictionary[key] = key_value
        return f"Setting '{key}' updated to '{key_value}' successfully!"
    else:
        return f"Setting '{key}' does not exist! Cannot update a non-existing setting."

def delete_setting(settings_dictionary, key):
    key = key.lower()
    if key in settings_dictionary:
        del settings_dictionary[key]
        return f"Setting '{key}' deleted successfully!"
    else:
        return "Setting not found!"
    
def view_settings(settings_dictionary):
    if not settings_dictionary:
       return 'No settings available.'
    resultado = 'Current User Settings:'
    for key, value in settings_dictionary.items():
        resultado = resultado + "\n" + key.capitalize() + ": " + str(value)
    return resultado + "\n"