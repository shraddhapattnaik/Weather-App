import requests
from tkinter import *



def weather():
	city = city_listbox.get()
	url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid=7c4a63c8a8d53d8c66746dff6a3350f6&units=metric".format(city)
	res = requests.get(url)
	output = res.json()

	weather_status = output['weather'][0]['description']
	temprature = output['main']['temp']
	humidity = output['main']['humidity']
	wind_speed = output['wind']['speed']

	weather_status_label.configure(text = "weather status : "+ weather_status)
	temprature_label.configure(text = "temprature : "+ str(temprature))
	humidity_label.configure(text = "Humidity : "+ str(humidity))
	wind_speed_label.configure(text = "wind speed  : "+ str(wind_speed))
	

window = Tk()
window.geometry("400x350")

city_name_list = ["lucknow", "delhi", "bangalore", "pune", "bhubaneswar", "cuttack", "visakhapatnam", "hyderabad"]

city_listbox = StringVar(window)
city_listbox.set("select the city")
option = OptionMenu(window,city_listbox,*city_name_list)
option.grid(row=2,column=2,padx=150,pady=10)

b1 = Button(window,text="o",width=15,command=weather)
b1.grid(row=5,column=2,padx=150)


weather_status_label = Label(window,font=("times",10,"bold"))
weather_status_label.grid(row=10,column=2)

temprature_label = Label(window,font=("times",10,"bold"))
temprature_label.grid(row=12,column=2)

humidity_label = Label(window,font=("times",10,"bold"))
humidity_label.grid(row=14,column=2)

wind_speed_label = Label(window,font=("times",10,"bold"))
wind_speed_label.grid(row=16,column=2)

window.mainloop()