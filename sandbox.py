FREEZING_POINT_F = 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - FREEZING_POINT_F) * 5/9

def display_temp(city_name, temp_f):
    temp_c = fahrenheit_to_celsius(temp_f)
    # Using :.1f to format to 1 decimal place makes it even cleaner
    print(f"{city_name} is {temp_c:.1f} degrees Celsius")

display_temp("City 1", 32)
display_temp("City 2", 100)
display_temp("City 3", 212)