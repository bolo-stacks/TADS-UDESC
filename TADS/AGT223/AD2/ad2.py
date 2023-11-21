#AD2 Algoritmos


#Ex.1
def corrigir_espacos(texto):
  texto_corrigido = texto.replace(" ,", ",")
  texto_corrigido = texto_corrigido.replace(" .", ".")
  return texto_corrigido

entrada = input()

saida = corrigir_espacos(entrada)
print(saida)

#Ex.2
def converterTempo(N):
  horas = N // 3600
  minutos = (N % 3600) // 60
  segundos = (N % 3600) % 60
  return [horas, minutos, segundos]


#Ex.3
def verifica_dificuldade(sobrenome):
  if sobrenome.isnumeric():
      return ""

  consoantes_consecutivas = 0

  for letra in sobrenome:
      if letra.isalpha() and letra not in "AEIOUaeiou":
          consoantes_consecutivas += 1
          if consoantes_consecutivas >= 3:
              return "nao eh facil"
      else:
          consoantes_consecutivas = 0

  return "eh facil"

num_casos_teste = int(input())

for _ in range(num_casos_teste):
  sobrenome = input()
  resultado = verifica_dificuldade(sobrenome)
  print(f"{sobrenome} {resultado}")

#eX.4
def cifra_de_cesar(n, casos):
  resultados = []

  for i in range(n):
      cod, v = casos[i]
      resultado = ""

      for j in range(len(cod)):
          if cod[j] == '\0':
              break
          if (ord(cod[j]) - v) < 65:
              resultado += chr((ord(cod[j]) - v) + 26)
          else:
              resultado += chr(ord(cod[j]) - v)

      resultados.append(resultado)

  return resultados

n = int(input())

casos = []
for i in range(n):
  cod = input().strip()
  v = int(input())
  casos.append((cod, v))

resultados = cifra_de_cesar(n, casos)
for resultado in resultados:
  print(resultado)

#Ex.5
def main():
    N = int(input())
    
    for a in range(1, N + 1):
        X = int(input())
        c = X // 2
        d = 0

        for b in range(1, c + 1):
            if X % b == 0:
                d += b

        if d == X:
            print(f"{X} eh perfeito")
        else:
            print(f"{X} nao eh perfeito")

if __name__ == "__main__":
    main()
