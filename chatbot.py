import openai

chave = "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"

openai.api_key = chave

def mensagem(mensagem, lista=[]):
    lista.append([
           {"role": "user", "content": mensagem},
    ])
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo-instruct",
        messages= lista
        
    )
    return response['choices'][0]['message']
    #resposta sera praticamente um dicionario 
lista = []  
while True:
    texto = input("Escreva aqui sua mensagem: ")
    
    if texto == "sair": 
        break
    else:
        response= mensagem(texto, lista)
        lista.append(response)
        print("Chatbot",response["content"])
        
        
# print(mensagem("Write a tagline for an ice cream shop")) -- exemplo teste