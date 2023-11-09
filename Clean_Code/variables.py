import re
import datetime
import time
from typing import Union, Dict

# 1. Meaningful and pronounceable variable names
# bad
ymdstr = datetime.date.today().strftime("%y-%m-%d")

# good
current_date: str = datetime.date.today().strftime("%y-%m-%d")


# 2. Use the same vocabulary for the same type of variable
# Subject: USER, not client, not customer
# bad
def get_user_basic_info():
    pass


def get_client_official_data():
    pass


def get_customer_medical_record():
    pass


###


# best practice
def get_user_basic_info():
    pass


def get_user_official_data():
    pass


def get_user_medical_record():
    pass


#####


class Record:
    pass


class User:
    info: str

    @property
    def data(self) -> Dict[str, str]:
        return {}

    def get_record(self) -> Union[Record, None]:
        return Record()


# 3. Use searchable names -> ctrl + shift + f
# # bad
# time.sleep(86400)  # what's up with this number? + hardcoded
# # best practice
# SECONDS_IN_A_DAY = 60 * 60 * 24
# time.sleep(SECONDS_IN_A_DAY)

# 4. Use explanatory variable
# regex patterns are tricky to use, so most outcomes may be mistunderstood by other engineers
address = "One Infinite Loop, Cupertino 95014"
city_zip_code_regex = r"^[^,\\]+[,\\\s]+(.+?)\s*(\d{5})?$"

# bad
matches = re.match(city_zip_code_regex, address)
if matches:
    print(
        f"{matches[1]}: {matches[2]}"
    )  # who are matches[1] and matches[2]? what do they represent?

# what I prefer
if matches:
    city, zip_code = matches.groups()
    print(f"{city}: {zip_code}")

# best practice
city_zip_code_regex = r"^[^,\\]+[,\\\s]+(?P<city>.+?)\s*(?P<zip_code>\d{5})?$"
matches = re.match(city_zip_code_regex, address)
if matches:
    print(f"{matches['city']}, {matches['zip_code']}")

# 5. Avoid mental mapping (school system iterations)

# bad
lst = ["Hike at Jepii Mici", "Hike at Cabana Ciucas", "Running in Bucharest"]
for x in lst:
    # do stuff
    # do other stuff
    print(x)

# best practice
list_of_activities = [
    "Hike at Jepii Mici",
    "Hike at Cabana Ciucas",
    "Running in Bucharest",
]
for activity in list_of_activities:
    # do stuff
    # do other stuff
    print(activity)


# 6. Don't add unnecessary context
# bad
class Car:
    car_make: str
    car_model: str
    car_color: str


# best practice
class Car:
    make: str
    model: str
    color: str


# 7. Use default arguments instead of short circuiting or conditionals
# bad
def create_micro_brewery(name):
    name = "DEFAULT Name" if name is None else name
    print(name)


create_micro_brewery(None)


# best practice
def create_micro_brewery(name: str = "Default Name"):
    print(name)


create_micro_brewery()
