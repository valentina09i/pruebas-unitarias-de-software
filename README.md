# PRUEBAS CON PYTEST PARA PYRHON Python 3.12.3
## Crear entorno virtual

## instalar librerias 
```
pip install pytest
```
| Comandos           | Descripcion                     |
| ------------------ | ------------------------------- |
| pip install pytest | libreria para pruebas unitarias |

## Crear archivo con las dependencias
```
pip freeze > requirement.txt
```
## crear archivos ejemplo.py
```
def suma(a,b)
    return a+b
```
## Crear archivo de prueba test_ejemplo.py
```
def test_suma():
    assert suma(2,3) ==5
    assert suma(-1,1) ==0
    assert suma(0,0) ==0
    assert suma(100,200) ==300
    assert suma (-5,-5) ==-10
```
## Ejecutar las test
```
pytest
```