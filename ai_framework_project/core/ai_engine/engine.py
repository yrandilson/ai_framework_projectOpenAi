import os
from openai import OpenAI

class AIEngine:
    """
    Motor de IA responsável por interagir com modelos de linguagem (LLMs).
    """

    def __init__(self, api_key=None, model="gpt-4.1-mini"):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        self.model = model
        self.client = OpenAI(api_key=self.api_key)

    def generate_response(self, prompt, system_prompt="Você é um assistente útil."):
        """
        Gera uma resposta para o prompt fornecido.
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Erro ao gerar resposta da IA: {str(e)}"

    def analyze_data(self, data, instruction):
        """
        Analisa dados com base em uma instrução específica.
        """
        prompt = f"Dados para análise: {data}\nInstrução: {instruction}"
        return self.generate_response(prompt, system_prompt="Você é um analista de dados especializado.")

    def make_decision(self, context, options):
        """
        Toma uma decisão com base no contexto e nas opções fornecidas.
        """
        prompt = f"Contexto: {context}\nOpções: {options}\nQual a melhor opção? Responda apenas com o nome da opção."
        return self.generate_response(prompt, system_prompt="Você é um tomador de decisões preciso.")
