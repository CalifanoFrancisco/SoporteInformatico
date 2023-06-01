import pandas as pd
import numpy as np

def fixColumns(valor):
    for i in range(len(valor)):
        valor[i] = valor[i].replace(" ", "");
    return valor;

def resolveSpaces(valor):
    valor = str(valor)
    if valor[0] == ' ':
        valor = valor[1:];
    if valor == '':
        valor = np.nan;
    if valor == 'nan':
        valor = np.nan;
    return valor;

csv         = pd.read_csv("./data/DATOS");
csv.columns = fixColumns(list(csv.columns));
csv.applymap(resolveSpaces);
csv.dropna(inplace=True)

def resolveStr(value):
    value = str(value);
    value = value.lower();
    # codigo de depuracion
    return value;

def pushToCsv(pregunta):
    csv[pregunta] = csv[pregunta].apply(resolveStr)

pushToCsv("¿Qué van a estudiar luego de recibirse del secundario?")
pushToCsv("Licenciatura en ciencias de la computación")
pushToCsv("Ingeniería en sistemas")
pushToCsv("Licenciatura en ciencias de la computación")
pushToCsv("Todavía no lo decidí")
pushToCsv("Todavía no lo decidí")
pushToCsv("Otra carrera")
pushToCsv("Licenciatura en ciencias de la computación")
pushToCsv("Todavía no lo decidí")
pushToCsv("Otra carrera")
pushToCsv("Licenciatura en ciencias de datos")
pushToCsv("Todavía no lo decidí")
pushToCsv("Ingeniería en sistemas")
pushToCsv("Todavía no lo decidí")
pushToCsv("Ingeniería informática")
pushToCsv("Todavía no lo decidí")
pushToCsv("Ingeniería en sistemas")
pushToCsv("Ingeniería informática")
pushToCsv("Ingeniería informática")
pushToCsv("Todavía no lo decidí")
pushToCsv("Ingeniería informática")
pushToCsv("Ingeniería en sistemas")
pushToCsv("Ingeniería en sistemas")
pushToCsv("Ingeniería en sistemas")
pushToCsv("Licenciatura en ciencias de la computación")
pushToCsv("Todavía no lo decidí")
pushToCsv("Licenciatura en ciencias de datos")