
#Atributos de la clase
class Gen:
    nucleotidos = ["A", "T", "C", "G"]
    
    #Atributos de la instancia 
    def __init__(self, nombre, secuencia, cromosoma,organismo, cadena_codificante=True):
        
        self.nombre = nombre
        self.secuencia = secuencia.upper()
        self.cromosoma = cromosoma
        self.organismo = organismo
        self.cadena_codificante = cadena_codificante # True si la secuencia es la cadena codificante, False si no lo es 

   #Metodos

   #Fucion para calcular la longitud de la secuencia
    def longitud_sec(self):
        return len(self.secuencia)
    
    #Funcion para calcular el contenido de GC
    def contenido_gc(self):
        cont_cg = 0
        for char in self.secuencia:
            if char in "CG":
                cont_cg += 1
        porcentaje = cont_cg / len(self.secuencia) * 100
        return porcentaje
    
    #Funcion para obtener la secuencia complementaria reversa
    def reversa_complementaria(self):
        complemento = {"A": "T", "T": "A", "C": "G", "G": "C"}
        #reversed() regresa un iterador que recorre la cadena desde atras
        #por cada base se busca su complementaria en el diccionario, join() une las bases para que queden continuas    
        return "".join(complemento[base] for base in reversed(self.secuencia)) 
    
    #Funcion para transcribir ADN a ARN
    def transcripcion(self):
        rna = "" 
        secuencia_transcribir = self.secuencia
        if not self.cadena_codificante:
            secuencia_transcribir = self.reversa_complementaria()
        
        for nucleotido in secuencia_transcribir:
            if nucleotido == "T":
                rna += "U"
            else:
                rna += nucleotido
        return rna

#Ejemplo para probar los metodos 
gen = Gen("Gen1", "ATGC", "Cromosoma 1", "Homo sapiens", cadena_codificante=True)

print(f"Gen: {gen.nombre}, Secuencia: {gen.secuencia}, Cromosoma: {gen.cromosoma}, Organismo: {gen.organismo}")
print("Longitud de la secuencia:", gen.longitud_sec())
print(f"Contenido de GC:{gen.contenido_gc()}%")
print("RNA:", gen.transcripcion())
