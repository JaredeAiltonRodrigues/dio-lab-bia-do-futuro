from ollama import chat

def get_resposta(contexto, pergunta_do_usuario):
    try:
        mensagem_formatada = f"Aqui estão os dados da família:\n{contexto}\n\nPergunta: {pergunta_do_usuario}"

        response = chat(
            model='llama3',
            messages=[
                {
                    "role": "system", 
                    "content": "Você é o EcoDom AI, um assistente financeiro familiar. Seja empático, prático e use os dados fornecidos para dar conselhos exatos."
                },
                {
                    "role": "user", 
                    "content": mensagem_formatada
                }
            ],
        )
        return response.message.content
        
    except Exception as e:
        return f"Erro ao processar sua requisição no DeepSeek: {str(e)}"