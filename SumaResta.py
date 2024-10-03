class Add_Sub:
    def add(self, a, b):
        self.r = a+b
    def sub(self, a, b):
        self.r = a-b
    def mullti(self, a, b):
        self.r = a*b
    def divi(self, a, b):
        if b == 0:
            print("no se acepta dividir entre 0")
        else:
            self.r = a/b
    def imprimirResultado(self):
        print("el resultado es", self.r)