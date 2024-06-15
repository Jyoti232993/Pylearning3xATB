# Multiple Conditions
# Switch in JAVA - I
# Match Case in Python

browser = input("Enter the browser name: ")
browser = browser.lower()

match browser:
    case "chrome":
        print("Chrome code is executed.")
    case "firefox":
        print("Firefox code is executed.")
    case _:
        print("No browser Found!")
