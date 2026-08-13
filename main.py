from pyscript import display, document 

name = 'Chester'
age = '14'
height167 = '182.4'
targeted_countries = [ "Switzerland", "Japan", "USA"]
student_type = False 
student_dict = {'color': 'blue', 'car_brand': 'Tesla','shoe_size': '11','best_friend': 'William',}
fruit_favorite = {"Watermelon", "Mango", "Papayas", "Strawberry", "Grape"}
days_of_the_week = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday",)

document.getElementById('result').innerHTML = f'Hello My name is <i>{name}</i>, I am {age} years old, My height is {height167}cm, the countries I plan on vissiting in the future are {targeted_countries},my student past is {student_type}, and my student dictionary is {student_dict}.,My favorite fruits are {fruit_favorite}, and here are the seven days of the week {days_of_the_week}' 
