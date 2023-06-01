import pandas as pd
import numpy as np

# Series_reference,     DCQ.SF1AA2CAB
# Period,               2016.06
# Data_value,           1116.386
# Suppressed,
# STATUS,               F
# UNITS,                Dollars
# Magnitude,            6
# Subject,              Business Data Collection - BDC
# Group,                Industry by financial variable (NZSIOC Level 2)
# Series_title_1,       Sales (operating income)
# Series_title_2,       Forestry and Logging
# Series_title_3,       Current prices
# Series_title_4,       Unadjusted
# Series_title_5

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

csv = pd.read_csv("./datos/DATA.csv");
csv.columns = fixColumns(list(csv.columns));
csv.applymap(resolveSpaces);
csv.dropna(inplace=True)

# resolve numerics
def resolvePeriod(value):
    value = int(value);
    for character in valor:
        if not character.isnumeric() and character != ".":
            valor = valor.replace(character,'');
    return valor;

def resolveDataValue(value):
    value = int(value);
    for character in valor:
        if not character.isnumeric() and character != ".":
            valor = valor.replace(character,'')
    return valor

def resolveMagnitude(value):
    value = int(value);
    for character in valor:
        if not character.isnumeric() and character != ".":
            valor = valor.replace(character,'')
    return valor

# resolve strings

def resolveSeriesReference(value):
    value = str(value);
    value = value.lower();
    # codigo de depuracion
    return value;

def resolveSupressed(value):
    value = str(value);
    value = value.lower();
    # codigo de depuracion
    return value;

def resolveStatus(value):
    value = str(value);
    value = value.lower();
    # codigo de depuracion
    return value;

def resolveUnits(value):
    value = str(value);
    value = value.lower();
    # codigo de depuracion
    return value;

def resolveSubject(value):
    value = str(value);
    value = value.lower();
    # codigo de depuracion
    return value;

def resolveGroup(value):
    value = str(value);
    value = value.lower();
    # codigo de depuracion
    return value;

def resolveSeriesTitle1(value):
    value = str(value);
    value = value.lower();
    # codigo de depuracion
    return value;

def resolveSeriesTitle2(value):
    value = str(value);
    value = value.lower();
    # codigo de depuracion
    return value;

def resolveSeriesTitle3(value):
    value = str(value);
    value = value.lower();
    # codigo de depuracion
    return value;

def resolveSeriesTitle4(value):
    value = str(value);
    value = value.lower();
    # codigo de depuracion
    return value;

def resolveSeriesTitle5(value):
    value = str(value);
    value = value.lower();
    # codigo de depuracion
    return value;

csv["Series_reference"] = csv["Series_reference"].apply(resolveSeriesReference);
csv["Period"]           = csv["Period"]          .apply(resolvePeriod         );
csv["Data_value"]       = csv["Data_value"]      .apply(resolveDataValue      );
csv["Suppressed"]       = csv["Suppressed"]      .apply(resolveSupressed      );
csv["STATUS"]           = csv["STATUS"]          .apply(resolveStatus         );
csv["UNITS"]            = csv["UNITS"]           .apply(resolveUnits          );
csv["Magnitude"]        = csv["Magnitude"]       .apply(resolveMagnitude      );
csv["Subject"]          = csv["Subject"]         .apply(resolveSubject        );
csv["Group"]            = csv["Group"]           .apply(resolveGroup          );
csv["Series_title_1"]   = csv["Series_title_1"]  .apply(resolveSeriesTitle1   );
csv["Series_title_2"]   = csv["Series_title_2"]  .apply(resolveSeriesTitle2   );
csv["Series_title_3"]   = csv["Series_title_3"]  .apply(resolveSeriesTitle3   );
csv["Series_title_4"]   = csv["Series_title_4"]  .apply(resolveSeriesTitle4   );
csv["Series_title_5"]   = csv["Series_title_5"]  .apply(resolveSeriesTitle5   );

csv.dropna(inplace=True)
print(csv)