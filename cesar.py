class Cesar:
    alfabeto = list("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ")

    def __init__(self, clave=0):
        if isinstance(clave, int):
            self.clave = clave
        else:
            raise AttributeError(f"{clave} debe ser un entero")
        

    def encriptar(self, mensaje):
        """
        Para cada caracter del mensaje
           1. Obtener su posicion en alfabeto
           2. Sumar clave a posicion
           3. Obtener caracter en nueva posicion
        Devolver la concatenacion de todos los nuevos caracteres
        """
        mensaje_encriptado = ""
        for caracter in mensaje.upper():
            if caracter not in self.alfabeto:
                new_caracter = caracter
            else:
                pos = self.alfabeto.index(caracter)
                new_pos = pos + self.clave
                if new_pos > len(self.alfabeto)-1:
                    new_pos = new_pos - len(self.alfabeto)

                new_caracter = self.alfabeto[new_pos]
            mensaje_encriptado += new_caracter
        return mensaje_encriptado.upper()
            
    def desencriptar(self, mensaje_encriptado):
        mensaje_desencriptado = ""
        for caracter in mensaje_encriptado.upper():
            if caracter not in self.alfabeto:
                new_caracter = caracter
            else:
                pos = self.alfabeto.index(caracter)
                new_pos = pos - self.clave
                new_caracter = self.alfabeto[new_pos]
            mensaje_desencriptado += new_caracter
        return mensaje_desencriptado
