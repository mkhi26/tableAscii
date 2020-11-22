from tableAscii import TableAscii
"""
A continuación se hace una demmostración de como se crea la tabla.
"""


table = TableAscii(6) # creamos una instancia de la tabla, pasamos como parametro el numero de columnas que tendra.
table.addHeader("Listado de empleados para el año 2020") # Agregamos un título a la tabla.

columna1 = ["Primer Nombre", "Segundo Nombre", "Primer Apellido", "Segundo apellido", "fecha de nacimiento", "Genero"]
columna2 = ["Pedro", "Jose", "Calix", "Cruz", "24/12/1995", "Masculino"]
columna3 = ["Daniela", "Sofia", "Perdomo", "Castro", "21/10/1994", "Femenino"]
columna4 = ["Roberto", "Rolando", "Sifuentes", "Meza", "5/01/1999", "Masculino"]
columna5 = ["Antonio", "Amilcar", "Velasquez", "Rodriguez", "26/12/1998", "Masculino"]

table.addRow(columna1)
table.addRow(columna2)
table.addRow(columna3)
table.addRow(columna4)
table.addRow(columna5)


print(table.getTable())
