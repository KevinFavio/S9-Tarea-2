numero=20
numero1: int=2

try :
    resultado=numero/numero1
except ZeroDivisionError:
      print("no se puede dividir entre si")
finally:
    print("yo siempre aparesco")

print("aqui termina esto")

