import os
import shutil

# Ruta base donde se reconfigurarán las carpetas
base_path = r"C:\Users\marco\Documentos\docencia\radicacion_vectorial_numerico\6_numerico\3_integracion"

# Estructura deseada con mapeo de carpetas existentes
new_structure = {
    "1_Diagnostico": {
        "subcarpetas": ["1_propu_investigativa", "2_programa_curso", "3_formatos_generales_clase"],
        "nuevas": ["entrevistas_iniciales", "pruebas_diagnosticas"]
    },
    "2_Planificacion": {
        "subcarpetas": ["11_recursos_enseñanza_aprendizaje"],
        "nuevas": ["diseño_intervencion", "calendario_actividades"]
    },
    "3_Implementacion": {
        "Ciclo1_Metodos_Basicos": ["4_suma_left_riemann", "5_suma_right_riemann", 
                                  "6_suma_punto_medio", "7_suma_trapecios"],
        "Ciclo2_Aplicaciones_Avanzadas": ["8_suma_simpson", "9_proyecto_prob_lluvia", 
                                        "10_proyecto_prob_temperature"],
        "nuevas": ["sesiones_practicas", "registros_clase"]
    },
    "4_Observacion": {
        "subcarpetas": ["12_tareas", "13_proyectos"],
        "nuevas": ["bitacoras_estudiantes", "registros_video"]
    },
    "5_Reflexion": {
        "nuevas": ["analisis_intermedio", "ajustes_metodologicos", 
                  "informes_parciales"]
    },
    "6_Evaluacion": {
        "subcarpetas": ["14_parcial"],
        "nuevas": ["portafolios_finales", "evaluacion_competencias"]
    }
}

def reorganizar_carpetas():
    # Crear estructura principal
    for fase in new_structure:
        fase_path = os.path.join(base_path, fase)
        os.makedirs(fase_path, exist_ok=True)
        
        # Mover carpetas existentes
        if "subcarpetas" in new_structure[fase]:
            for carpeta in new_structure[fase]["subcarpetas"]:
                orig = os.path.join(base_path, carpeta)
                dest = os.path.join(fase_path, carpeta)
                if os.path.exists(orig):
                    shutil.move(orig, dest)
        
        # Crear nuevas subcarpetas
        if "nuevas" in new_structure[fase]:
            for nueva in new_structure[fase]["nuevas"]:
                os.makedirs(os.path.join(fase_path, nueva), exist_ok=True)
        
        # Manejar subfases en Implementación
        if fase == "3_Implementacion":
            for subfase in ["Ciclo1_Metodos_Basicos", "Ciclo2_Aplicaciones_Avanzadas"]:
                subfase_path = os.path.join(fase_path, subfase)
                os.makedirs(subfase_path, exist_ok=True)
                for carpeta in new_structure[fase][subfase]:
                    orig = os.path.join(base_path, carpeta)
                    dest = os.path.join(subfase_path, carpeta)
                    if os.path.exists(orig):
                        shutil.move(orig, dest)

    print("Reorganización completada. Nueva estructura:")
    for root, dirs, files in os.walk(base_path):
        level = root.replace(base_path, '').count(os.sep)
        indent = ' ' * 4 * level
        print(f'{indent}{os.path.basename(root)}/')

if __name__ == "__main__":
    reorganizar_carpetas()