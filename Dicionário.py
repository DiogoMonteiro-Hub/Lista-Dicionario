# Dicionário:

# 1- 

alunos = {"Ana": 8.5, "Pedro": 7.0, "Maria": 9.2}
alunos["Carlos"] = 6.5
alunos["Ana"] = 9.0
del alunos["Pedro"]
print(alunos)

media = sum(alunos.values()) / len(alunos)
print(f"Média das notas: {media:.2f}")

if "Maria" in alunos:
    print("Maria está no dicionário.")
else:
    print("Maria não está no dicionário.")