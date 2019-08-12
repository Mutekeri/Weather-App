import tkinter as tk
from tkinter import font
import requests

HEIGHT = 500
WIDTH = 500

def format_response(weather):
    try:
        name = weather['name']
        desc = weather['weather'][0]['description']
        temp = weather['main']['temp']

        #final_str =  str(name) + '' + str(desc) + '' + str(temp)
        final_str = 'City: %s \nCondtions: %s \nTemperature (°C): %s' % (name, desc, temp)
    except:
        final_str = 'There was a problem retrieving that information'

    return final_str


def test_function(entry):
    print("This is the entry:", entry)

# 82b986037165568a43807f82b202ee07
# api.openweathermap.org/data/2.5/forecast?q={city name},{country code}

def get_weather(city):
    weather_key = '82b986037165568a43807f82b202ee07'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'Metric'}
    response = requests.get(url=url,params=params)
    weather = response.json()

    label['text'] = format_response(weather)

    #print(weather['name'])
    #print(weather['weather'][0]['description'])
    #print(weather['main']['temp'])

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1,relheight=1)


frame = tk.Frame(root, bg='#80c1ff', bd=5)
# frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)
# frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

# entry = tk.Entry(frame, bg='green')
entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)
# entry.pack(fill='both')
# entry.grid(row=2, column=2)

button = tk.Button(frame, text="Get weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)
# button.pack(side='left', fill='x', expand=True)
# button.grid(row=0, column=0)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

# label = tk.Label(lower_frame, text="Regina Analytics", bg='yellow')
label = tk.Label(lower_frame, font=('Modern', 15))
label.place(relwidth=1, relheight=1)
# label.pack(side='right', fill='both')
# label.grid(row=1, column=1)

#print(tk.font.families())

root.mainloop()