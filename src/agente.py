import openai
from config import API_KEY

client = openai.OpenAI(api_key=API_KEY)

def get_resposta(historico_contexto, mensagem_usuario):
    system_prompt = """Você é o EcoDom AI, um assistente financeiro familiar. 
    Use os dados de transações fornecidos para responder. Seja empático e prático."""
    
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"Contexto: {historico_contexto}\n\nPergunta: {mensagem_usuario}"}
        ]
    )
    return response.choices[0].message.content