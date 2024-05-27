import sqlite3
import pandas as pd
import socket
import time
import threading

def create_connection(db_file):
    conn = None
    conn = sqlite3.connect(db_file)
    return conn

def insertar_datos(database, columna1, columna2):
    
    presion1 = 0
    presion2 = 0
    presion3 = 0
    presion4 = 0
    presion5 = 0

    try:
        presion1, presion2, presion3, presion4, presion5 = columna2.split(',')
        presiones = [presion1, presion2, presion3, presion4, presion5]

        for i in range(5):

            conexion = sqlite3.connect(database)
            cursor = conexion.cursor()
                
            table = 'foot1sensor' + str(i+1)

            consulta = "INSERT INTO graficas_database" + table + " (data_date, data_value) VALUES (?, ?)"

            valores = (columna1, presiones[i])

            try:
                cursor.execute(consulta, valores)
                conexion.commit()

            except sqlite3.Error as e:
                print(f"Error al insertar datos: {e}")

            finally:
                conexion.close()

    except:
        print("error xd")



def receive_data(client_socket, client_address):
    database = r"db.sqlite3"
    conn = create_connection(database)


    while True:
        request = client_socket.recv(1024)

        if len(request) != 0:

            request = request.decode("utf-8") # convert bytes to string
            print(request)
            with conn:
                insertar_datos("db.sqlite3", time.strftime("%H:%M:%S"), request)

                cursor = conn.cursor()
                #print(f"Received: {request}")

                cursor.execute("select * from graficas_databasefoot1sensor1")
                numerofilas = len(cursor.fetchall())

                #print("umero filaaaaa\n\n\n", numerofilas)

                if numerofilas >=2:
                     for i in range(5):
                        cursor.execute("SELECT * FROM graficas_databasefoot1sensor" + str(i+1) + " WHERE id = ?", (numerofilas,))
                        datoultimo = cursor.fetchone()[2]

                        cursor.execute("SELECT * FROM graficas_databasefoot1sensor" + str(i+1) + " WHERE id = ?", (numerofilas-1,))
                        datoanterior = cursor.fetchone()[2]

                        print('sensor: ', i)
                        print('dato ultimo', datoultimo)
                        print('dato anterior', datoanterior)
                        print()

                        if float(datoultimo) - float(datoanterior) > 100:
                            table = str(i+1)
                            consulta = "INSERT INTO graficas_databasefoot1presionsensor"+table+" (data_date, data_value) VALUES (?, ?)"
                            valores = (time.strftime("%H:%M:%S"), datoultimo)
                            cursor.execute(consulta, valores)

           #     print("\nRecibido:", request)
            #    print(" \nPresion sensor: ", presionsensor1)

            #response = "accepted".encode("utf-8") 
            #client_socket.send(response)


def run_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_ip = "0.0.0.0"
    port = 8082

    server.bind((server_ip, port))
    server.listen(3)
    print(f"Pendiente de datos de {server_ip}:{port}")
   
    while True:
        client_socket, client_address = server.accept()
        print(f"A.C. from {client_address[0]}:{client_address[1]}")
        #threading.Thread(target=receive_data, args=(client_socket, client_address)).start()
        receive_data(client_socket,client_address)
    # close connection socket with the client
    # client_socket.close()
    # print("Connection to client closed")
    # close server socket
    # server.close()


run_server()