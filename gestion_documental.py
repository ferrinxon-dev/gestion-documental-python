import json
import os

ARCHIVO = "documentos.json"


# Cargar documentos desde archivo
def cargar_documentos():
    if os.path.exists(ARCHIVO):
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    return []


# Guardar documentos en archivo
def guardar_documentos(documentos):
    with open(ARCHIVO, "w") as f:
        json.dump(documentos, f, indent=4)


documentos = cargar_documentos()


def agregar_documento():
    nombre = input("Nombre del documento: ")
    tipo = input("Tipo (PDF, Word, etc): ")

    doc = {
        "id": len(documentos) + 1,
        "nombre": nombre,
        "tipo": tipo
    }

    documentos.append(doc)
    guardar_documentos(documentos)
    print("✅ Documento agregado y guardado")


def listar_documentos():
    if not documentos:
        print("No hay documentos")
    else:
        for doc in documentos:
            print(doc)


def buscar_documento():
    nombre = input("Buscar por nombre: ")
    encontrados = [d for d in documentos if nombre.lower() in d["nombre"].lower()]

    if encontrados:
        for doc in encontrados:
            print(doc)
    else:
        print("No se encontró el documento")


def menu():
    while True:
        print("\n--- GESTIÓN DOCUMENTAL ---")
        print("1. Agregar documento")
        print("2. Listar documentos")
        print("3. Buscar documento")
        print("4. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_documento()
        elif opcion == "2":
            listar_documentos()
        elif opcion == "3":
            buscar_documento()
        elif opcion == "4":
            break
        else:
            print("Opción inválida")


menu()
