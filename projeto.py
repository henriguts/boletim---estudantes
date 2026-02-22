notas = []

portugues = float(input("Escreva sua nota de Português: "))
notas.append(portugues)
matematica = float(input("Escreva sua nota de Matemática: "))
notas.append(matematica)
fisica = float(input("Escreva sua nota de Física: "))
notas.append(fisica)
biologia = float(input("Escreva sua nota de Biologia: "))
notas.append(biologia)
quimica = float(input("Escreva sua nota de Química: "))
notas.append(quimica)
historia = float(input("Escreva sua nota de História: "))
notas.append(historia)
geografia = float(input("Escreva sua nota de Geografia: "))
notas.append(geografia)
sociologia = float(input("Escreva sua nota de Sociologia: "))
notas.append(sociologia)
ingles = float(input("Escreva sua nota de Inglês: "))
notas.append(ingles)
arte = float(input("Escreva sua nota de Arte: "))
notas.append(arte)
edfisica = float(input("Escreva sua nota de Ed. Física: "))
notas.append(edfisica)
filosofia = float(input("Escreva sua nota de Filosofia: "))
notas.append(filosofia)


if portugues >= 6:
    status_portugues = "APROVADO"
else:
    status_portugues = "REPROVADO"

if matematica >= 6:
    status_matematica = "APROVADO"
else:
    status_matematica = "REPROVADO"

if fisica >= 6:
    status_fisica = "APROVADO"
else:
    status_fisica = "REPROVADO"

if biologia >= 6:
    status_biologia = "APROVADO"
else:
    status_biologia = "REPROVADO"

if quimica >= 6:
    status_quimica = "APROVADO"
else:
    status_quimica = "REPROVADO"

if historia >= 6:
    status_historia = "APROVADO"
else:
    status_historia = "REPROVADO"

if geografia >= 6:
    status_geografia = "APROVADO"
else:
    status_geografia = "REPROVADO"

if sociologia >= 6:
    status_sociologia = "APROVADO"
else:
    status_sociologia = "REPROVADO"

if ingles >= 6:
    status_ingles = "APROVADO"
else:
    status_ingles = "REPROVADO"

if arte >= 6:
    status_arte = "APROVADO"
else:
    status_arte = "REPROVADO"

if edfisica >= 6:
    status_edfisica = "APROVADO"
else:
    status_edfisica = "REPROVADO"

if filosofia >= 6:
    status_filosofia = "APROVADO"
else:
    status_filosofia = "REPROVADO"

print("---------------------------------------")

print(f"Português -- {portugues} {status_portugues}")
print(f"Matemática -- {matematica} {status_matematica}")
print(f"fisica -- {fisica} {status_fisica}")
print(f"biologia -- {biologia} {status_biologia}")
print(f"quimica -- {quimica} {status_quimica}")
print(f"historia -- {historia} {status_historia}")
print(f"geografia -- {geografia} {status_geografia}")
print(f"sociologia -- {sociologia} {status_sociologia}")
print(f"ingles -- {ingles} {status_ingles}")
print(f"arte -- {arte} {status_arte}")
print(f"edfisica -- {edfisica} {status_edfisica}")
print(f"filosofia -- {filosofia} {status_filosofia9}")
