"""
#Variables(string)
#Printea el primer caracter de la string
z = "Que tengas una buena semana"[0]
print(z)
#Mezcla de minusculas y mayusculas
x = "vOLVer a vir"
print(x.lower())
#Largo de la variable
print(len(x))
#Usar + en el print
primer_nombre = "David"
print("Mi nombre es: " + primer_nombre)
#Reemplazar parte del string
numero_serial = "ABC123"
print(numero_serial.replace("123","456"))
"""
windows_serial_number = "abc-def-ghi-jkl"
new_partial_variable_a = windows_serial_number[0:3]
new_partial_variable_b = windows_serial_number[4:7]
new_partial_variable_c = windows_serial_number[8:11]
new_partial_variable_d = windows_serial_number[12:15]
print(new_partial_variable_a)
print(new_partial_variable_b)
print(new_partial_variable_c)
print(new_partial_variable_d)
new_partial_variable_a = new_partial_variable_a.replace('abc' , 'aaa')
new_partial_variable_b = new_partial_variable_b.replace('def', 'bbb')
new_partial_variable_c = new_partial_variable_c.replace('ghi' , 'ccc')
new_partial_variable_d = new_partial_variable_d.replace('jkl' , 'ddd')
print(new_partial_variable_a)
print(new_partial_variable_b)
print(new_partial_variable_c)
print(new_partial_variable_d)
encoded_windows_serial_number = new_partial_variable_a+"-"+new_partial_variable_b+"-"+new_partial_variable_c+"-"+ new_partial_variable_d
print(encoded_windows_serial_number)
