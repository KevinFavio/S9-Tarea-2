class Persona():

    apellidos=" "
    nombre=" "
    edad=0
    despierta=False

    def despertar(selfs):

        selfs.despierta=True
        print("bunes dias ")

persona1=Persona()
persona1.apellidos="martinez brito"
print(persona1.apellidos)
persona1.despertar()
print(persona1.despierta)

persona2=Persona()
persona2.apellidos="pastos lopez"
print(persona2.apellidos)

print(persona2.despierta)