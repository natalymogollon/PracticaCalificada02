# Matriz ejemplo
N = [[1,2,0],[3,1,4],[3,0,1]]
A = []

for i in range(len(N)):
    A.append(N[i][i])
    print(A)

for i in range(1,len(A)+1):
    suma = 0
    suma = suma + i

if suma%2==0:
    print(suma,"es un número par")
else:
    print(suma,"es un número impar")

print("---------------------------------------")

# Primera matriz

B = [[1,2,3,4],[8,7,6,5],[9,8,7,2],[6,8,2,3]]
C = []

for i in range(len(B)):
    C.append(B[i][i])
    for j in C:    
        suma1 = 0
        suma1 = suma1 + j
print(suma1)

if suma%2==0:
    print(suma,"es un número par")
else:
    print(suma,"es un número impar")

# Segunda Matriz

# Tercera Matriz

