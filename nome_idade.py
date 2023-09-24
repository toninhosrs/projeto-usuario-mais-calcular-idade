import datetime

def obter_ano_nascimento():
    while True:
        try:
            ano = int(input("Digite o ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano <= 2021:
                return ano
            else:
                print("Ano inválido. Tente novamente.")
        except ValueError:
            print("Valor inválido. Tente novamente.")

def main():
    nome = input("Digite seu nome completo: ")
    ano_nascimento = obter_ano_nascimento()
    idade = datetime.datetime.now().year - ano_nascimento
    print(f"Olá, {nome}! Você completou, ou completará, {idade} anos no ano atual (2022).")

if __name__ == "__main__":
    main()