# In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY),
# otherwise known as middle-endian order, which is arguably bad design.
# Dates in that format can’t be easily sorted because the date’s year comes last instead of first.
# Try sorting, for instance, 2/2/1800, 3/3/1900, and 1/1/2000 chronologically in any program (e.g., a spreadsheet).
# Dates in that format are also ambiguous. Harvard was founded on September 8, 1636,
# but 9/8/1636 could also be interpreted as August 9, 1636!

# Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted
# in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits,
# months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

# In a file called outdated.py, implement a program that prompts the user for a date, anno Domini,
# in month-day-year order, formatted like 9/8/1636 or September 8, 1636,
# wherein the month in the latter might be any of the values in the list below:

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# Then output that same date in YYYY-MM-DD format.
# If the user’s input is not a valid date in either format, prompt the user again.
# Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.


# while True:
#     date_input = input("Insert date in (MM/DD/YYYY) or (Month, Day Year): ")

#     # check if date is in the format "month day, year"
#     if "," in date_input:
#         try:
#             month, day, year = date_input.split()
#             day = day.strip(",")
#             month_index = months.index(month) + 1 # because month index start from 1 - (January)
#             formatted_date = f"{year}-{month_index:02d}-{int(day):02d}"
#             print(formatted_date)
#             break
#         except ValueError:
#             print("Invalid date format. Please try again.")
#         # Check if the date is in the format "month/day/year"
#     elif "/" in date_input:
#         try:
#             month, day, year = date_input.split("/")
#             month_index = int(month)
#             formatted_date = f"{year}-{month_index:02d}-{int(day):02d}"
#             print(formatted_date)
#             break
#         except ValueError:
#             print("Invalid date format. Please try again.")
#     else:
#         print("Invalid date format. Try again please!")


while True:
    date_input = input("Enter date in (MM/DD/YYYY) or (Month, Day Year): ")

    # Check if the date is in the format "month/day/year"
    if "/" in date_input:
        try:
            month, day, year = date_input.split("/")
            month_index = int(month)
            day = int(day)
            year = int(year)

            # Validate the date components
            if month_index < 1 or month_index > 12 or day < 1 or day > 31:
                raise ValueError()

            formatted_date = f"{year:04d}-{month_index:02d}-{day:02d}"
            print(formatted_date)
            break  # Exit the loop if the date is valid
        except ValueError:
            print("Invalid date format. Please try again.")
    # Check if the date is in the format "month day, year"
    elif "," in date_input:
        try:
            month, day, year = date_input.split()
            day = day.rstrip(",")
            month_index = months.index(month) + 1  # Month index starts from 1
            year = int(year)

            # Validate the date components
            if month_index < 1 or month_index > 12 or int(day) < 1 or int(day) > 31:
                raise ValueError()

            formatted_date = f"{year:04d}-{month_index:02d}-{int(day):02d}"
            print(formatted_date)
            break  # Exit the loop if the date is valid
        except (ValueError, IndexError):
            print("Invalid date format. Please try again.")
    # Reprompt if the format is not valid:
    else:
        print("Invalid date format. Try again please!")
