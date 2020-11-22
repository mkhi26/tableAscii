from tableAscii import TableAscii
table = TableAscii(6)
table.addHeader("Título de la tabla")
for i in range(20):
    col = []
    for j in range(6):
        col.append("Elemento %s"%i)
    table.addRow(col)

elemento = ["Nombre extremadamente grande", "Nombre pequeño", "0", "Elemento X", "Gatos", "Elemento muy grande"]

table.addRow(elemento)
print(table.getTable())
