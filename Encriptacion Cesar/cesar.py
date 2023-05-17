abecedario = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encriptar_cesar(texto, shift):
    rta = ""
    for letra in texto:
        letra = letra.lower()
        if letra in abecedario:
            i = abecedario.index(letra)
            i += shift

            if i >= len(abecedario):
                i = i - len(abecedario)
            
            rta = rta + abecedario[i]
        else:
            rta = rta + letra

    return rta

def desencriptar_cesar(texto, shift):
    rta = ""
    for letra in texto:
        letra = letra.lower()
        if letra in abecedario:
            i = abecedario.index(letra)
            i -= shift

            if i < 0:
                i = i + len(abecedario)
            
            rta = rta + abecedario[i]
        else:
            rta = rta + letra

    return rta

if __name__ == "__main__":
    text = encriptar_cesar("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG", 23)
    print(text)
    print(desencriptar_cesar(text, 23))