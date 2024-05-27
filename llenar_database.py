import sqlite3

database = r"db.sqlite3"

for i in range(5):

    conexion = sqlite3.connect(database)
    cursor = conexion.cursor()
        
    table = 'foot1presionsensor' + str(i+1)

    consulta = "INSERT INTO graficas_database" + table + " (data_date, data_value) VALUES (?, ?)"

    valores = (0, 0)

    try:
        cursor.execute(consulta, valores)
        conexion.commit()
        print(f"Insertados", valores)

    except sqlite3.Error as e:
        print(f"Error al insertar datos: {e}")

    finally:
        conexion.close()