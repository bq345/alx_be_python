from datetime import datetime, timedelta
def display_current_datetime():
    current_datetime = datetime.now()
    print("Current Date and Time:", current_datetime.strftime("%Y-%m-%d %H:%M:%S"))
def calculate_future_date (days):
    future_date = datetime.now() + timedelta(days=days)
    print("Future Date after", days, "days:", future_date.strftime("%Y-%m-%d")) 
    return future_date.strftime("%Y-%m-%d")
def main():
    display_current_datetime()
    days = int(input("Enter the number of days to add to the current date: "))
    calculate_future_date(days)
if __name__ == "__main__":
    main()
