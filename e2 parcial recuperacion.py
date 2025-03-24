class cliente:
    def __init__(self,cedula,edad,sexo,referido,tipo_vehiculo,numero_horas)
        self.cedula = cedula
        self.edad = edad
        self.sexo = sexo
        self.referido = referido
        self.tipo_vehiculo = tipo_vehiculo
        self.numero_horas = numero_horas
        self.descuentos = 0
        self.monto_total = 0


    def calcular_descuento(self):
     tarifa_por_hora = 25 if self.tipo_vehiculo == "Automático" else 35

     monto_total_sin_descuento = tarifa_por_hora * self.horas

     if self.referido:
            self.descuento += 0.25 * monto_total_sin_descuento
     if self.edad < 18:
            self.descuento += 0.20 * monto_total_sin_descuento
     if self.horas > 3:
            self.descuento += 0.15 * monto_total_sin_descuento

     self.monto_total = monto_total_sin_descuento - self.descuento
     

    def generar_recibo(self):
        recibo = f"""
        Recibo de la Autoescuela 'La Rápida'
        -----------------------------------
        Cédula de Identidad: {self.cedula}
        Tipo de Vehículo: {self.tipo_vehiculo}
        Descuentos Aplicados: {self.descuento:.2f} USD
        Monto Total a Facturar: {self.monto_total:.2f} USD
        """
        return recibo
    








