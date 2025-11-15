import pandas
import os
import re

path = "../data/BWA/"
files = [os.path.join(path, f) for f in os.listdir(path) if f.endswith("clean.sort.count.txt")]

dataframe = []

for f in files:
    #extraer el nombre de la condicion por cada nombre de archivo
    filename = os.path.basename(f)
    condition_name = re.split(r"[._]", filename.replace("sample", ""))[0]
    #Leer archivo 
    df = pandas.read_csv(f, sep="\t", header=None)

    #Tomar columna 9 y 10 de cada archivo 
    reads_col_name = condition_name
    df = df[[8, 9]]
    df.columns = ["gene_information", reads_col_name]

    # Dado que solo se solicita ID y Name se deben extraer de gene_information 
    df["gene_id"] = df["gene_information"].str.extract(r'ID=([^;]+)')
    df["gene_name"] = df["gene_information"].str.extract(r'Name=([^;]+)')

    # Se mantendra por cada archivo el id, el nombre y lecturas
    df = df[["gene_id", "gene_name", reads_col_name]]
    
    dataframe.append(df)

# tomamos el primer dataframe como base
table_coverage = dataframe[0]
# Iteramos sobre los demás dataframes y los vamos combinando
for df in dataframe[1:]:
    table_coverage = pandas.merge(table_coverage, df, on=["gene_id", "gene_name"], how="outer")

table_coverage.fillna(0, inplace=True)

table_coverage.to_csv("../results/tabla_cobertura.csv", index=False)

print("Tabla de cobertura generada: tabla_cobertura.csv")

