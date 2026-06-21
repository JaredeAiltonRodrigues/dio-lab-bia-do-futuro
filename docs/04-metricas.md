# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** [ x] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resultado:** [x ] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [x ] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto XYZ?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [x ] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- Diagnóstico de Ambiente Virtual: Conseguimos identificar rapidamente o bloqueio de segurança do Linux (PEP 668) e criar o ambiente isolado para o pip e o Streamlit funcionarem corretamente.

Identificação de Conflitos de Código: Encontramos e resolvemos o problema da função duplicada (get_resposta) que estava misturando configurações da OpenAI com o Ollama.

Sincronização de Arquivos: Corrigimos com sucesso o erro de argumentos (TypeError), fazendo com que o app.py entregasse o histórico financeiro e a pergunta corretamente para o agente.py.

Rápida Adaptação: Quando esbarramos na barreira de pagamento (Erro 403) do modelo de nuvem do DeepSeek, fomos ágeis em pivotar a estratégia para rodar um modelo robusto e 100% gratuito localmente (llama3).

**O que pode melhorar:**
- Separação de Ambientes (Terminal vs. Código): Ter mais atenção para não colar blocos de código Python diretamente no terminal do Linux (Bash), garantindo que os scripts sempre sejam salvos nos arquivos .py.

Limpeza de Arquivos: Ao atualizar o código, certificar-se de apagar as versões anteriores das funções ou importações que não são mais usadas (como o load_dotenv e chamadas da OpenAI) para evitar que o Python se confunda ou que o aplicativo quebre.

Atenção aos Caminhos do Terminal: Observar com cuidado em qual pasta e em qual ambiente virtual estamos trabalhando (ex: .venv com ponto vs. venv sem ponto), para garantir que as bibliotecas (pip install) não sejam instaladas no lugar errado.

Validação de Modelos: Antes de integrar um modelo específico no código (como o deepseek-v4-flash:cloud), verificar na documentação se ele é um modelo de código aberto para uso local ou se exige uma chave de API/assinatura paga.

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

Consumo e Custos: Como você está baixando o Llama 3 para rodar via Ollama na sua própria máquina, o seu custo por tokens será literalmente zero! Você tem uso ilimitado sem precisar de cartão de crédito.

Latência (Tempo de Resposta): Essa será a sua métrica técnica mais importante agora. Como modelos locais exigem bastante processamento do computador, medir quantos segundos ele leva para gerar a resposta ajudará a saber se a sua máquina está dando conta do recado.

Logs e Erros: Nós já começamos a fazer o básico disso no seu agente.py! Aquele bloco try... except Exception as e que configuramos serve exatamente para capturar falhas (como o erro 403 que você tomou antes) e não deixar o aplicativo simplesmente "quebrar" sem te avisar.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!
