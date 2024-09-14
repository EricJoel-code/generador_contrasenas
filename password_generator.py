import string
import secrets

def transformar_texto_a_contraseña(texto):
    reemplazos = {
        'a': '@', 'A': '4',
        'e': '3', 'E': '3',
        'i': '1', 'I': '1',
        'o': '0', 'O': '0',
        's': '$', 'S': '$'
    }

    contraseña = []
    for char in texto:
        if char in reemplazos:
            contraseña.append(reemplazos[char])
        else:
            if char.isalpha():
                if secrets.choice([True, False]):
                    contraseña.append(char.upper())
                else:
                    contraseña.append(char.lower())
            else:
                contraseña.append(char)
    
    especiales = string.punctuation
    for _ in range(3):
        contraseña.insert(secrets.randbelow(len(contraseña)), secrets.choice(especiales))
    
    return ''.join(contraseña)

def generar_contraseña(longitud, tipo, referencia="", include_symbols=False, include_digits=False):
    if tipo == 1:
        caracteres = string.ascii_lowercase
    elif tipo == 2:
        caracteres = string.ascii_uppercase
    elif tipo == 3:
        caracteres = string.digits
    elif tipo == 4:
        caracteres = referencia
    elif tipo == 5:
        caracteres = string.ascii_letters + referencia
    elif tipo == 6:
        caracteres = string.ascii_letters
        if include_symbols:
            caracteres += string.punctuation
        if include_digits:
            caracteres += string.digits
    else:
        caracteres = string.ascii_letters + string.punctuation
    
    contraseña = "".join(secrets.choice(caracteres) for _ in range(longitud))
    return contraseña

def guardar_contraseña(contraseña):
    with open("contraseñas.txt", "a") as file:
        file.write(contraseña + "\n")
