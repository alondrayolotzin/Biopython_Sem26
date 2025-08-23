### Ejercicio 3 y 4:
"""
Ejercicio 3: Usando el concepto de Herencia, realicen una subclase de la clase gen, llamada tRNA, y otra clase llamada RNA no codificante.  Luego deriva de tRNA otra subclase llamada proteina.
Ejercicio 4: Genera una función longitud para la clase tRNA y una función longitud para la clase proteína.  La primera regresa el numero de nucleótidos, la segunda, el número de nucleótidos y de aminoácidos.
"""

import MarquezMendoza_AlondraYolotzin_Ejercicio2 as Gen 
    
class tRNA(Gen.Gen):

    def funcion(self):
        return "Transporta aminoacidos al ribosoma durante la traducción."
    
    def longitud(self):
        return self.longitud_sec() 
    
    def imprimir(self):
        return (f"tRNA: {self.nombre}, Función: {self.funcion()}, "
                f"Longitud: {self.longitud_sec()} nucleótidos")

class RNA_no_codificante(Gen.Gen):
   #miRNA, siRNA, lncRNA
    
    def __init__(self, nombre, secuencia, cromosoma, organismo, tipo):
        Gen.Gen.__init__(self,nombre, secuencia, cromosoma, organismo, cadena_codificante=False)
        self.tipo = tipo  

    def funcion(self):
        return f"Regula la expresion genica como {self.tipo}."
    
    def longitud(self):
        return self.longitud_sec()   # reutiliza el método del padre
    
    def imprimir(self):
        return (f"ncRNA: {self.nombre}, Tipo: {self.tipo}, Función: {self.funcion()}, "
                f"Longitud: {self.longitud_sec()} nucleotidos")

class Proteina(tRNA):
    
    def __init__(self, nombre, secuencia, cromosoma, organismo):
        Gen.Gen.__init__(self, nombre, secuencia, cromosoma, organismo, cadena_codificante=True)
    
    def longitud(self):

        nucleotidos = self.longitud_sec()
        aminoacidos = nucleotidos // 3
        return {"nucleotidos": nucleotidos, "aminoacidos": aminoacidos}
    
    def imprimir(self):
        long = self.longitud()
        return (f"Proteína derivada de {self.nombre}, "
                f"Nucleotidos: {'nucleotidos'}, "
                f"Aminoácidos: {'aminoacidos'}")

# Instancia de tRNA
trna2 = tRNA("tRNA-Met", "ATGCGTACGTTAG", "Cromosoma 3", "Mus musculus")
# Instancia de RNA no codificante
rna2 = RNA_no_codificante("siRNA-101", "GGAUCCAGUAGC", "Cromosoma 2", "Drosophila melanogaster", tipo="siRNA")
# Instancia de Proteina
proteina2 = Proteina("Actina", "ATGGCCTGACGATGCGTGGGCTCTAGACGCTGAGGAC", "Cromosoma 12", "Homo sapiens")
print(trna2.imprimir())
print(rna2.imprimir())
print(proteina2.imprimir())
