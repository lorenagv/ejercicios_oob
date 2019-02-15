

class NIF():
    def __init__(self, numerodni):
        self.numerodni = numerodni

    def calcula_letra(self):
        suma = 0
        dict1 = {0:"T",1:"R",2:"W",3:"A",4:"G",5:"M",6:"Y",7:"F",8:"P",9:"D",10:"X",11:"B",12:"N",13:"J",14:"Z",15:"S",16:"Q",17:"V",18:"H",19:"L",20:"C",21:"K",22:"E"}

        resto = self.numerodni % 23
        return dict1[resto]

a = NIF(72903161)
print("Su letra de DNI es la",a.calcula_letra())
