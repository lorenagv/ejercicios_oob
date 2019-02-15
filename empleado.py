
class Empleado():
    def __init__(self,nombre,edad,salario):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario

    def get_nombre(self):
        return self.nombre

    def get_edad(self):
        return self.edad

    def get_salario(self):
        if self.edad >= 50:
            impuesto = 0.1
            impuesto_total = self.salario*impuesto
            return impuesto_total
        else:
            impuesto = 0.2
            impuesto_total = self.salario*impuesto
            return impuesto_total

p = Empleado("Juan", 23, 2000)
print(p.get_salario())
