
class Fraccion():
    def __init__(self, numerador, denominador):
        self.numerador = numerador
        self.denominador = denominador

    def suma(self,f2):
        suma_num = self.numerador*f2.denominador + self.denominador*f2.denominador
        suma_den = self.denominador*f2.denominador
        return str(suma_num)+ "/"+str(suma_den)

    def resta(self,f2):
        resta_num = self.numerador*f2.denominador - self.denominador*f2.denominador
        resta_den = self.denominador*f2.denominador
        return str(resta_num)+"/"+ str(resta_den)

    def multiplica(self, f2):
        mult_num = self.numerador*f2.numerador
        mult_den = self.denominador*f2.denominador
        return str(mult_num)+"/"+ str(mult_den)

    def divide(self, f2):
        div_num = self.numerador*f2.denominador
        div_den = self.denominador*f2.numerador
        return str(div_num)+"/"+str(div_den)

f1 = Fraccion(1,3)
f2 = Fraccion(2,6)
sumar = f1.suma(f2)
print(sumar)
