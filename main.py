# Importa o módulo random para gerar números aleatórios
import random  

# Gera um número aleatório entre 1 e 100 e o armazena em numero_secreto
numero_secreto = random.randint(1, 100)  
# Inicializa o contador de tentativas
tentativas = 0  

# Imprime as instruções para o usuário
print("Adivinhe o número secreto entre 1 e 100.")  

# Inicia um loop infinito que continuará até que o número correto seja adivinhado
while True:  
    
    # Pede ao usuário para inserir um palpite e converte para inteiro
    palpite = int(input("Digite o seu palpite: "))  
    # Incrementa o contador de tentativas
    tentativas += 1  

    # Verifica se o palpite é menor que o número secreto
    if palpite < numero_secreto:  
        
        # Informa ao usuário que o número secreto é maior
        print("O número secreto é maior. Tente novamente!")  
        
    # Verifica se o palpite é maior que o número secreto
    elif palpite > numero_secreto:  
        
        # Informa ao usuário que o número secreto é menor
        print("O número secreto é menor. Tente novamente!")  
        
    # Se o palpite não for nem maior nem menor, ele deve ser igual
    else:  
        
        # Imprime uma mensagem de sucesso
        print(f"Parabéns! Você acertou o número secreto {numero_secreto} em {tentativas} tentativas.")  
        
        # Sai do loop, já que o número correto foi adivinhado
        break  
