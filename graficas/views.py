from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
import matplotlib.pyplot as plt
import io
import urllib, base64
import numpy as np
import django
from django.http.response import JsonResponse
from .models import  DataBaseFoot1PresionSensor1, DataBaseFoot1PresionSensor2, DataBaseFoot1PresionSensor3, DataBaseFoot1PresionSensor4,DataBaseFoot1PresionSensor5
 
def graficas(request):
    return render(request, 'index.html')

def read_data_base_foot1():
    datos = DataBaseFoot1PresionSensor1.objects.all()
    data_value = []
    data_date = []

    for dato in datos:
      data_value.append(dato.data_value)
      data_date.append(dato.data_date)

    return data_date, data_value

def read_data_base_foot2():
    datos = DataBaseFoot1PresionSensor2.objects.all()
    data_value = []
    data_date = []

    for dato in datos:
      data_value.append(dato.data_value)
      data_date.append(dato.data_date)

    return data_date, data_value

def read_data_base_foot3():
    datos = DataBaseFoot1PresionSensor3.objects.all()
    data_value = []
    data_date = []

    for dato in datos:
      data_value.append(dato.data_value)
      data_date.append(dato.data_date)

    return data_date, data_value

def read_data_base_foot4():
    datos = DataBaseFoot1PresionSensor4.objects.all()
    data_value = []
    data_date = []

    for dato in datos:
      data_value.append(dato.data_value)
      data_date.append(dato.data_date)

    return data_date, data_value

def read_data_base_foot5():
    datos = DataBaseFoot1PresionSensor5.objects.all()
    data_value = []
    data_date = []

    for dato in datos:
      data_value.append(dato.data_value)
      data_date.append(dato.data_date)

    return data_date, data_value


def get_foot(request):
    data = []
    presion1 = []
    presion2 = []
    presion3 = []
    presion4 = []
    presion5 = []
    date1, value1 = read_data_base_foot1()
    date2, value2 = read_data_base_foot2()
    date3, value3 = read_data_base_foot3()
    date4, value4 = read_data_base_foot4()
    date5, value5 = read_data_base_foot5()

    presion1.append(value1[-1])
    presion2.append(value2[-1])
    presion3.append(value3[-1])
    presion4.append(value4[-1])
    presion5.append(value5[-1])

    
    days = [i for i in range (54)]
    for i in range(0,54):
        for j in range(0,54):
            data.append([i,j,100])
    
    #for entry in data:
     #   if entry[0] == 20 and entry[1] == 41:
      #      entry[2] = presion[-1]
       #     break

    #for entry in data:
     #   if 19 <= entry[0] <= 21 and 40 <= entry[1] <= 42 and not (entry[0] == 20 and entry[1] == 41):
      #      entry[2] = presion[-1]-10 
  
    for entry in data:

        ##Quinto sensor
        if entry[0] == 22 and entry[1] == 16:
            entry[2] = presion5[-1]
  
        elif entry[0] == 22 and entry[1] == 17:
            entry[2] = presion5[-1]
  
        elif entry[0] == 23 and entry[1] == 16:
            entry[2] = presion5[-1]
 
        elif entry[0] == 23 and entry[1] == 17:
            entry[2] = presion5[-1]

        elif 21 <= entry[0] <= 24 and 15 <= entry[1] <= 18 and not (entry[0] == 22 and entry[1] == 16) and not (entry[0] == 22 and entry[1] == 17) and not (entry[0] == 23 and entry[1] == 16) and not (entry[0] == 23 and entry[1] == 17):
            entry[2] = presion5[-1] - 80
        
        ##Cuarto sensor
        elif entry[0] == 17 and entry[1] == 22:
            entry[2] = presion4[-1]
  
        elif entry[0] == 17 and entry[1] == 23:
            entry[2] = presion4[-1]
  
        elif entry[0] == 18 and entry[1] == 22:
            entry[2] = presion4[-1]
 
        elif entry[0] == 18 and entry[1] == 23:
            entry[2] = presion4[-1]
        
        elif 16 <= entry[0] <= 19 and 21 <= entry[1] <= 24 and not (entry[0] == 17 and entry[1] == 22) and not (entry[0] == 17 and entry[1] == 23) and not (entry[0] == 18 and entry[1] == 22) and not (entry[0] == 18 and entry[1] == 23):
            entry[2] = presion4[-1] - 80

        ##Tercer sensor
        elif entry[0] == 18 and entry[1] == 29:
            entry[2] = presion3[-1]
  
        elif entry[0] == 18 and entry[1] == 30:
            entry[2] = presion3[-1]
  
        elif entry[0] == 19 and entry[1] == 29:
            entry[2] = presion3[-1]
 
        elif entry[0] == 19 and entry[1] == 30:
            entry[2] = presion3[-1]
        
        elif 17 <= entry[0] <= 20 and 28 <= entry[1] <= 31 and not (entry[0] == 18 and entry[1] == 29) and not (entry[0] == 18 and entry[1] == 30) and not (entry[0] == 19 and entry[1] == 29) and not (entry[0] == 19 and entry[1] == 30):
            entry[2] = presion3[-1] - 100

        ##Segundo sensor
        elif entry[0] == 22 and entry[1] == 35:
            entry[2] = presion2[-1]
  
        elif entry[0] == 22 and entry[1] == 36:
            entry[2] = presion2[-1]
  
        elif entry[0] == 23 and entry[1] == 35:
            entry[2] = presion2[-1]

        elif entry[0] == 23 and entry[1] == 36:
            entry[2] = presion2[-1]
        
        elif 21 <= entry[0] <= 24 and 34 <= entry[1] <= 37 and not (entry[0] == 22 and entry[1] == 35) and not (entry[0] == 22 and entry[1] == 36) and not (entry[0] == 23 and entry[1] == 35) and not (entry[0] == 23 and entry[1] == 36):
            entry[2] = presion2[-1] - 80

        ##Primer sensor
        elif entry[0] == 21 and entry[1] == 43:
            entry[2] = presion1[-1]
  
        elif entry[0] == 21 and entry[1] == 44:
            entry[2] = presion1[-1]
  
        elif entry[0] == 22 and entry[1] == 43:
            entry[2] = presion1[-1]
 
        elif entry[0] == 22 and entry[1] == 44:
            entry[2] = presion1[-1]

        elif 20 <= entry[0] <= 23 and 42 <= entry[1] <= 45 and not (entry[0] == 21 and entry[1] == 43) and not (entry[0] == 21 and entry[1] == 44) and not (entry[0] == 22 and entry[1] == 43) and not (entry[0] == 22 and entry[1] == 44):
            entry[2] = presion1[-1] - 80



    
    chart = {
        'title': {
            'text': "Gráfica de presiones aplicadas en la plantilla",
            'left': "center"
        },
        'tooltip': {
            'position': "top"
        },
        'grid': {
            'height': "80%",
            'top': "10%"
        },
        'xAxis': {
            'position': "top",
            'type': "category",
            'data': days,
            
            'splitArea': {
            'show': True
            }
        },
        'yAxis': {
            'inverse': True,
            'type': "category",
            'data': days,
            'splitArea': {
            'show': True
            }
        },
        
        'visualMap': {
            'min': 0,
            'max': 1000,
            'calculable': True,
            'realtime': False,
            'orient': "horizontal",
            'left': "center",
            'bottom': "0%",
            'inRange': {
            'color': [
                "rgba(0, 0, 255, 0)",      
                "rgba(0, 128, 0, 0.5)",     
                "rgba(255, 165, 0, 0.5)",   
                "rgba(255, 0, 0, 1)",   
                ],
        'symbolSize': [100, 100]
            }
            
        
            
        },
        
        'backgroundColor': {
            'image': 'http://localhost:8080/pie2.png',
        },

        
        'series': [
            {
            'name': "Presión",
            'type': "heatmap",
            'data': data,
            'label': {
                'show': False
            },
            'emphasis': {
                'itemStyle': {
                'shadowBlur': 10,
                'shadowColor': "rgba(0, 0, 0, 0.5)"
                }
            }
            }
        ]

    } 
    return JsonResponse(chart)
    