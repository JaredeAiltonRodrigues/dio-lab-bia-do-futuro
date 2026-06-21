# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |
| `perfil_investidor.json` | JSON | Personalizar recomendações |
| `produtos_financeiros.json` | JSON | Sugerir produtos adequados ao perfil |
| `transacoes.csv` | CSV | Analisar padrão de gastos do cliente |

> [!TIP]
> **Quer um dataset mais robusto?** Você pode utilizar datasets públicos do [Hugging Face](https://huggingface.co/datasets) relacionados a finanças, desde que sejam adequados ao contexto do desafio.

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.


Para tornar o agente mais realista, os dados foram expandidos da seguinte forma:

 -  Categorização Hierárquica: O historico_gastos.csv foi expandido com subcategorias (ex: "Alimentação" -> "Supermercado", "Restaurantes", "Delivery") para permitir análises mais detalhadas.

- Campos de "Feedback": Adicionei uma coluna de sentimento/prioridade nas metas de curto prazo para que o agente saiba quais gastos podem ser cortados primeiro em caso de aperto financeiro.
---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

Os arquivos são lidos através de um script de carregamento (Python/Pandas) no momento em que o usuário inicia a sessão. Os dados são convertidos em strings formatadas que representam o estado atual da conta e as metas da família, garantindo que o agente tenha uma visão "snapshot" do momento.

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

Os dados são injetados dinamicamente no Contexto do System Prompt (técnica de RAG simplificada). Sempre que o usuário faz uma pergunta, o sistema recupera apenas as transações dos últimos 30 dias e as metas ativas, garantindo que o prompt não ultrapasse o limite de tokens e mantenha o foco no que é relevante hoje

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
--- INÍCIO DO CONTEXTO DE DADOS ---
Perfil Familiar: Família Silva
Meta Mensal de Gastos: R$ 4.500,00
Gasto Acumulado no Mês: R$ 3.850,00

Metas de Economia:
- Reserva de Emergência: R$ 1.200/R$ 5.000
- Fundo de Viagem: R$ 800/R$ 3.000

Últimas transações registradas:
- 15/06: Supermercado - R$ 620,00
- 16/06: Assinatura App - R$ 35,00
- 18/06: Farmácia - R$ 120,00

Dica do momento: "Cuidado com a categoria 'Delivery', você já atingiu 90% do limite mensal planejado."
--- FIM DO CONTEXTO DE DADOS ---
...
```
