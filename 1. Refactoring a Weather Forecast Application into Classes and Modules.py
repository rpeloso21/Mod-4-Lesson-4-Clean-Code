class CityWeatherReport:
    def __init__(self, city_name, temperature, condition, humidity):
        self.city_name = city_name
        self.temperature = temperature
        self.condition = condition
        self.humidity = humidity

    def get_name(self):
        return self.city_name

    def get_report(self):
        return (f"\nCity: {self.city_name} \nTemperature: {self.temperature} \nCondition: {self.condition} \nHumidity: {self.humidity}\n")
    
    def get_temp(self):
        return (f"\nCity: {self.city_name} \nTemperature: {self.temperature}.\n")
    
    def get_condition(self):
        return (f"\nCity: {self.city_name} \nCondition: {self.condition}.\n")
                 
    

new_york = CityWeatherReport("New York", 70, "Sunny", 50)
london = CityWeatherReport("London", 60, "Cloudy", 65)
tokyo = CityWeatherReport("Tokyo", 75, "Rainy", 70)

cities = [new_york, london, tokyo]


def main():
    while True:
        try:
            continue_input = input("Would you like to view a weather report (yes/no): ").lower()
            if continue_input != "yes":
                break

            city_input = input("Please select a city (New York, London, or Tokyo): ").lower()
            if city_input not in (city.get_name().lower() for city in cities):
                print("We do not have a report on that city yet.  Please select from the list.")
                continue

            report_input = input("What report would you like to view? (Full, Condition Only, Temperature Only):  ").lower()
            for city in cities:
                if city_input == city.get_name().lower():
                    if report_input == "full":
                        print(city.get_report())
                        break
                    elif report_input == "condition only":
                        print(city.get_condition())
                        break
                    elif report_input == "temperature only":
                        print(city.get_temp())
                        break
                    else:
                        print('That is not a valid report name.  Please try again.')
                        break

        except ValueError:
            print("Unexpexted Error.  Please try again.")

    print("Thank you for using the City Weather Report App.")



if __name__ == "__main__":
    main()
