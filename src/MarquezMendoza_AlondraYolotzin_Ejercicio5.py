'''
Alondra Marquez 
BioPython (2026-1)
8/12/2025
Descripcion: Script para buscar ORFs reales en una secuencia de DNA o RNA.
Uso:
    python MarquezMendoza_AlondraYolotzin_Ejercicio5.py AGCCATGTAGCTAACTCAGGTTACATGGGGATGACCCCGCGACT
'''    

from Bio.Seq import Seq
import argparse

'''
Verifica si la secuencia es RNA.
Devuelve True si es RNA (sin T), False si es DNA.
'''
def verificar_rna(secuencia):
    secuencia = secuencia.upper()
    if "T" in secuencia:
        return False
'''
Convierte RNA a DNA si es necesario y limpia la secuencia, devuelve la secuencia 
'''
def preparar_secuencia(secuencia):
   
    secuencia = secuencia.strip().upper()
    try:
        if verificar_rna(secuencia):
            return str(Seq(secuencia).back_transcribe())
        else:
            return secuencia
    except ValueError as e:
        raise ValueError(f"Error en la secuencia: {e}")

'''
Busca ORFs en los 6 marcos de lectura.
Devuelve un diccionario con el marco y lista de proteínas traducidas de cada ORF
'''
def buscar_orfs(secuencia):
    secuencia_dna = Seq(secuencia)
    secuencia_rev = secuencia_dna.reverse_complement()
    orfs_por_marco = {}

    # Definir los 6 marcos
    marcos = [
        ("F1", secuencia_dna[0:]),
        ("F2", secuencia_dna[1:]),
        ("F3", secuencia_dna[2:]),
        ("R1", secuencia_rev[0:]),
        ("R2", secuencia_rev[1:]),
        ("R3", secuencia_rev[2:])
    ]

    for nombre_marco, secuencia_marco in marcos:
        proteinas = []
        secuencia_aminoacidos = secuencia_marco.translate(to_stop=False) # to_stop=False indica que no se detenga en los codones stop, sino que los traduzca como * 
        proteina_temp = ""
        orf = False

        for aminoacido in secuencia_aminoacidos:
            if aminoacido == "M":         # Inicio de ORF
                proteina_temp = "M"
                orf = True
            elif aminoacido == "*" and orf:  # se usa * porque porque en Biopython, cuando traduces una secuencia de nucleótidos a aminoácidos con .translate(to_stop=False), todos los codones stop (TAA, TAG, TGA) se traducen automáticamente como * 
                proteina_temp += "*"
                proteinas.append(proteina_temp)
                proteina_temp = ""
                orf = False
            elif orf:
                proteina_temp += aminoacido

        # ORF que llega al final sin stop
        if orf and proteina_temp:
            proteinas.append(proteina_temp)

        orfs_por_marco[nombre_marco] = proteinas

    return orfs_por_marco

def main():
    parser = argparse.ArgumentParser(description= "Busca ORFs en una secuencia de DNA o RNA." )
    parser.add_argument("secuencia")
    args = parser.parse_args()

    try:
        secuencia_dna = preparar_secuencia(args.secuencia)
    except ValueError as e:
        print(e)
        return

    orfs = buscar_orfs(secuencia_dna)

    print("\nSecuencia (DNA):")
    print(secuencia_dna)

    print("\nProteinas traducidas de los ORFs por marco:")
    for marco, proteinas in orfs.items():
        print(f"{marco} ({len(proteinas)} ORFs):")
        for p in proteinas:
            print(f"  {p}")

if __name__ == "__main__":
    main()
