# Lab 3: "Crear un personaje"
# Nombre : Josue
# Fecha : 27-Febrero-2026


full_dot = '●'
empty_dot = '○'
def create_character(name, strengh, intellingence, carism):
    if not isinstance(name, str):
        return "The character name should be a string"
    if not name.strip():
        return "The character should have a name"
    if len(name) > 10:
        return "The character name is too long"
    if " " in name:
        return "The character name should not contain spaces"
    
    if not (isinstance(strengh, int) and isinstance(intellingence, int) and isinstance(carism, int)):
        return "All stats should be integers"
    if strengh < 1 or intellingence < 1 or carism < 1:
        return "All stats should be no less than 1"
    if strengh > 4 or intellingence > 4 or carism > 4:
        return "All stats should be no more than 4"
    total = strengh + intellingence + carism 
    if total != 7:
        return "The character should start with 7 points"
    
    linea_str = "STR " + (full_dot * strengh) + (empty_dot * (10 - strengh))
    linea_int = "INT " + (full_dot * intellingence) + (empty_dot * (10 - intellingence))
    linea_chat = "CHA " + (full_dot * carism) + (empty_dot * (10 - carism))
    return name + "\n" + linea_str + "\n" + linea_int + "\n" + linea_chat