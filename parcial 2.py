class clinica_estudios:
    def __init__(Ultrasonido,Tomografia,Resonancia):
        self.Ultrasonido = Ultrasonido
        self.Tomografia = Tomografia
        self.Resonancia = Resonancia


class cliente:
    def __init__(edad,Numero_cedula,sexo,Tipo_de_estudio,seguro):
        self.edad = edad
        self.Numero_cedula = Numero_cedula
        self.sexo = sexo
        self.Tipo_de_estudio = Tipo_de_estudio
        self.seguro = seguro

     


     def calcular_monto_neto(cedula, edad, sexo, seguro, tipo_estudio):
    
        precios_base = {
        'Ultrasonido': 8.90,
        'Tomografía': 12.64,
        'Resonancia': 15.60
    }
    

    precio_inicial = precios_base[tipo_estudio] + (edad * 10)
    
  
    if seguro:
        precio_inicial *= 0.20 
    
  
    if sexo == 'F' and edad > 70:
        precio_inicial *= 0.80  
    elif sexo == 'M' and edad > 80:
        precio_inicial *= 0.85 

     {
        'Cédula de Identidad': cedula,
        'Edad': edad,
        'Sexo': sexo,
        'Tipo de Estudio': tipo_estudio,
        'Pertenece a Seguro': 'Sí' if seguro else 'No',
        'Monto Neto a Pagar': round(precio_inicial, 2)
    }
    
    return recibo


  
