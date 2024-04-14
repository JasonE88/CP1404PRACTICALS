COLOR_CODES = {
    "ALICEBLUE": "#F0F8FF",
    "ANTIQUEWHITE": "#FAEBD7",
    "AQUA": "#00FFFF",
    "AQUAMARINE": "#7FFFD4",
    "AZURE": "#F0FFFF",
    "BEIGE": "#F5F5DC",
    "BISQUE": "#FFE4C4",
    "BLACK": "#000000",
    "BLANCHEDALMOND": "#FFEBCD",
    "BLUE": "#0000FF"
}

print("Enter a color name to get its hexadecimal color code.")
print("Enter a blank line to stop the program.")

while True:
    color_name = input("Enter a color name: ").upper()
    if not color_name:
        break
    try:
        color_code = COLOR_CODES[color_name]
        print(f"The hexadecimal color code for {color_name} is {color_code}")
    except KeyError:
        print("Invalid color name. Please try again.")