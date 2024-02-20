from cesar import Cesar
import pytest

def test_create_cesar():
    cesar = Cesar(3)
    assert cesar.clave == 3

def test_clave_must_be_integer():
    with pytest.raises(AttributeError) as exc:
        Cesar("algo que no es entero")

    assert "debe ser un entero" in str(exc.value)

    try:
        Cesar("algo que no es entero")
        variable_de_comprobacion = 0
    except AttributeError:
        variable_de_comprobacion = 1
    
    assert variable_de_comprobacion == 1 # Se ha lanzado una AttributeError

def test_encriptar():
    cesar = Cesar(3)
    entrada = "HOLA"
    salida = "KRÑD"
    assert cesar.encriptar(entrada) == salida

def test_encriptar_con_espacios():
    cesar = Cesar(3)
    entrada = "HOLA PEPE!"
    salida = "KRÑD SHSH!"
    assert cesar.encriptar(entrada) == salida

def test_encriptar_con_minusculas():
    cesar = Cesar(3)
    entrada = "Hola Pepe!"
    salida = "KRÑD SHSH!"
    assert cesar.encriptar(entrada) == salida

def test_encriptar_en_el_limite():
    cesar = Cesar(3)
    entrada = "XYZ"
    salida = "ABC"
    assert cesar.encriptar(entrada) == salida

def test_desencriptar():
    cesar = Cesar(3)
    entrada = "KRÑD"
    salida = "HOLA"
    assert cesar.desencriptar(entrada) == salida

def test_desencriptar_en_el_limite():
    cesar = Cesar(3)
    entrada = "ABC"
    salida = "XYZ"

    assert cesar.desencriptar(entrada) == salida