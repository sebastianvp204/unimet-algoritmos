from gestores.gestor_estadisticas import GestorEstadisticas
from gestores.gestor_experimetos import GestorExperimentos
from gestores.gestor_reactivos import GestorReactivos
from gestores.gestor_recetas import GestorRecetas
from utils.consola import limpiar_consola
from gestores.gestor_data import gestor_data

class InterfazConsola:
    def __init__(self):
        self.gestor_reactivos = GestorReactivos()
        self.gestor_recetas = GestorRecetas()
        self.gestor_experimentos = GestorExperimentos()
        self.gestor_estadisticas = GestorEstadisticas()
        self.gestor_data = gestor_data()
    
    def menu_gestion_reactivos(self):
        print("\n--- Gestión de Reactivos ---")
        print("1. Listar reactivos")
        print("2. Agregar reactivo")
        print("3. Editar reactivo")
        print("4. Eliminar reactivo")
        print("5. Volver al menú principal")
        
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            self.gestor_reactivos.mostrar_reactivos()
        elif opcion == "2":
            self.gestor_reactivos.crear_reactivo()
        elif opcion == "3":
            self.gestor_reactivos.mostrar_reactivos()
            id_reactivo = int(input("Ingrese el ID del reactivo a editar: "))
            self.gestor_reactivos.editar_reactivo(id_reactivo)
        elif opcion == "4":
            self.gestor_reactivos.mostrar_reactivos()
            id_reactivo = int(input("Ingrese el ID del reactivo a eliminar: "))
            self.gestor_reactivos.eliminar_reactivo(id_reactivo)
        elif opcion == "5":
            return
        
    def menu_gestion_experimentos(self):
        limpiar_consola()
        print("\n--- Gestión de Experimentos ---")
        print("1. Listar experimentos")
        print("2. Crear experimento")
        print("3. Ejecutar experimento")
        print("4. Volver al menú principal")
        
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            self.gestor_experimentos.mostrar_experimentos()
        elif opcion == "2":
            self.gestor_experimentos.crear_experimento()
        elif opcion == "3":
            self.gestor_experimentos.ejecutar_experimento()
        elif opcion == "4":
            return
        
    def menu_gestion_resultados(self):
        limpiar_consola()
        print("\n--- Gestión de Resultados ---")
        print("1. Evaluar resultados de experimento")
        print("2. Volver al menú principal")
        
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            self.gestor_experimentos.evaluar_resultados()
        elif opcion == "2":
            return
        
    def menu_indicadores_gestion(self):
        limpiar_consola()
        print("\n--- Indicadores de Gestión ---")
        print("1. Mostrar estadísticas del laboratorio")
        print("2. Volver al menú principal")
        
        opcion = input("Seleccione una opcion: ")
        if opcion == "1":
            reporte = self.gestor_estadisticas.generar_reporte(self.gestor_experimentos.experimentos)
            grafica = input("Deseas ver la grafica? (S/N): ")
            if grafica.lower() == "s":
                self.gestor_estadisticas.graficar_estadisticas(reporte, self.gestor_reactivos.reactivos)
            else:
                return
        elif opcion == "2":
            return
    
    def mostrar_menu(self):
        limpiar_consola()
        while True:
            print("\n--- Sistema de Laboratorio ---")
            print("1. Gestión de Reactivos")
            print("2. Gestión de Experimentos")
            print("3. Gestión de Estadísticas")
            print("4. Cargar datos API")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
                self.menu_gestion_reactivos()
            elif opcion == "2":
                self.menu_gestion_experimentos()
            elif opcion == "3":
                self.menu_indicadores_gestion()
            elif opcion == "4":
                self.gestor_data.guardar_data_api_recetas()
                self.gestor_data.guardar_data_api_experimentos()
                self.gestor_data.guardar_data_api_reactivos()
                print("Datos cargados desde la API.")
                
            elif opcion == "5":
                break
            else:
                print("Opción no válida.")


