class Empleado:
    def __init__(self,nombre, horas_trabajadas=0, tarifa_hora=0):
        self.nombre = nombre
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora

    def calcular_salario(self):
        return self.horas_trabajadas * self.tarifa_hora
    
class Empleado_por_Hora(Empleado):
    def calcular_salario(self, horas_extras=0):
        salario_inicial = super().calcular_salario()
        salario_extra = horas_extras * self.tarifa_hora
        return salario_inicial + salario_extra 
    
class EmpleadoAsalariado(Empleado):
    def __init__(self, nombre, salario_mensual):
        super().__init__(nombre)
        self.salario_mensual = salario_mensual
        
    def calcular_salario(self):
        return self.salario_mensual
    

Empleado1 = Empleado_por_Hora("juan",30,30)
print (f"Salario de {Empleado1.nombre} mas las horas extras es: {Empleado1.calcular_salario(15)}")

Empleado2 = EmpleadoAsalariado("Luna", 3000)
print (f"\nSalario de {Empleado2.nombre} la asalariada: {Empleado2.calcular_salario()}")

