"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
#import warnings
#warnings.filterwarnings("ignore", category=FutureWarning)
import pandas as pd



def clean_data():
    

    df = pd.read_csv("solicitudes_credito.csv", sep=";",index_col=0)


    #borrar todas las filas con espacios vacios
    df.dropna(inplace=True)

    

    #reemplazar
    df=df.apply(lambda x: x.astype(str).str.replace("-"," ").str.replace("_"," ").str.replace("$","").str.replace(",",""))
    #df=df.apply(lambda x: x.astype(str).str.replace("-"," ").str.replace("_"," ").str.replace(",",""))
    #df = df.apply(lambda x: x.astype(str).replace({"_": "-", "-": " ", "$": "", ",": ""}))
    

    #convertir todo a minisculas
    df.loc[:, df.dtypes=='object']=df.loc[:, df.dtypes=='object'].apply(lambda row: row.str.lower())

    #covertir a fecha
    #df.fecha_de_beneficio = pd.to_datetime(df['fecha_de_beneficio'],format="mixed",dayfirst=True)
    df.fecha_de_beneficio = pd.to_datetime(df['fecha_de_beneficio'],format="mixed",dayfirst=True)

    #convertir float, nuevo
    df.monto_del_credito = df.monto_del_credito.astype(float)

    #borrar los duplicados
    df.drop_duplicates(inplace=True)

    return df



