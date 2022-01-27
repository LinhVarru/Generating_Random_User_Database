from calendar import month
from tracemalloc import start
import names
import random
import uuid
import datetime
import pandas as pd
import string

class Generate_User:
    #Constructor
    def __init__(self):
        self.data = {}
        self.used_uid = []
        self.location_list = []
    #creating a new user    
    def create_user(self):
        for i in range(100):
            id = uuid.uuid1() #Generate a random user ID
            if id not in self.used_uid:
                name = names.get_full_name() #Generate a random full name
                dob = self.generate_dob() #Generate a random DOB
                location = self.generate_location() #Generate a random location
                email = self.generate_email()
                password = self.generate_password()
                self.data[id] = {
                    "full_name" : name,
                    "dob" : dob,
                    "age" : self.get_age(dob),
                    "location" : location,
                    "email" : email,
                    "password" : password
                }

    #Generate a random password using all characters
    def generate_password(self):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(12))
        return password

    #Generate a simple email using first and last name
    def generate_email(name,self):
        undone_email = name.split(" ")
        email = ''
        for letter in undone_email:
            email += letter.lower()
        email += "@gmail.com"
        return email

    #Randomly choose a location in the world as the user's location of residence
    def generate_location(self):
        csv_data = pd.read_csv(r'C:\Users\Admin\Documents\Study\Personal\Generating_Random_User_Database\data\worldcities.csv')
        df = pd.DataFrame(csv_data, columns=['city','country'])
        self.location_list = [[row[col] for col in df.columns] for row in df.to_dict('records')]
        location = self.location_list[random.randint(0, len(self.location_list) - 1)]
        return location

    #Randomly choose a date from 1950-1-1 to 2022-1-1 (yyyy-mm-dd)
    def generate_dob(self):
        start_date = datetime.date(1950,1,1)
        end_date = datetime.date(2022,1,1)
        time_between_dates = end_date - start_date
        days_between_dates = time_between_dates.days
        random_number_of_days = random.randrange(days_between_dates)
        random_date = start_date + datetime.timedelta(days = random_number_of_days)
        final_date = random_date.strftime("%Y") + "-" + random_date.strftime("%m") + "-" + random_date.strftime("%d")
        return final_date    

    #Get age
    def get_age(dob,self):
        #Today's date
        ty,tm,td = str(datetime.date.today()).split("-")
        #Split user's DOB
        y,m,d = dob.split("-")
        age = 0
        if m < tm:
            age = ty-y-1
        elif m == tm:
            if d < td:
                age = ty- y - 1
            else:
                age = ty - y 
        else:
            age = ty - y

        return age

def main():
    dataSet = Generate_User()

if __name__ == "__main__":
    main()