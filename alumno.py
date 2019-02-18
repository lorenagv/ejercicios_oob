

class Alumno():
    def __init__(self, n_matricula, nombre, nota1,nota2,nota3):
        self.n_matricula = n_matricula
        self.nombre = nombre
        self.nota1 = nota1
        self.nota2 = nota2
        self.nota3 = nota3

    def nota_final(self):
        nota_final = (self.nota1 + self.nota2 + self.nota3) / 3
        if nota_final >= 4.8:
            print("El alumno", self.n_matricula, self.nombre," ha aprobado")
            final = "nota final: "+ str(nota_final)
            return final 

        else:
            print("El alumno", self.n_matricula, self.nombre,"ha suspendido, con nota", nota_final)
            final = "nota final: "+ str(nota_final)
            return final 

a = Alumno(188,"Lorena",9,8,9)
print(a.nota_final())
