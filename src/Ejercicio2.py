
class gen():
    #atributos de la clase 
    nombre=""
    secuencia=""
    funcion=""
    
    def __init__(self, nombre, funcion, secuencia):

        # Atributos de instancia
        self.nombre = nombre  
        self.secuencia = secuencia 
        self.funcion= funcion

    def numero_nucleotidos_total(self):
        return len(self.secuencia)
        
    def calculo_GC(self): #porcentaje
        return (self.secuencia.count('G') + self.secuencia.count('C')) / len(self.secuencia) * 100
    
    def calculo_AT(self):
        return (self.secuencia.count('A') + self.secuencia.count('T')) /len(self.secuencia)* 100
    
    #funcion para transcribor secuencia de RNA: para cada nucleotido tengo que poder modificarlo a su contrario, la funcion necesita recorrer secuencia 
    def transcribir_rna (self.secuencia ):
        #for que recorra la secuencia, por cada nucleotido lo modifique,
        return 
    
gen1=gen('RAP2.12','','' )
print("Gen 1: " gen1.nombre, "longitud del gen: "gen1.longitud," secuencia: ", gen1.secuencia, "contenido GC", gen1.contenidoGC)

#terminar para poder heredar clase 