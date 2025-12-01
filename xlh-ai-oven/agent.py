from dataclasses import dataclass
from pydantic_ai import Tool
import asyncio
from rich import print
from pydantic import BaseModel, Field
from pydantic_ai import Agent
from deps import Deps
from tools import set_oven_temperature
from llm_model import get_model, LlmProvider, LlmModel

@dataclass
class Deps:
    name: str

class Ingredient(BaseModel):
    name: str = Field(description='Name der Zutat')
    quantity: str = Field(description='Menge')
    unit: str = Field(description='Einheit')

class Recipe(BaseModel):
    title: str = Field(description='Name der Pizza')
    ingredients: list[Ingredient] = Field(description='Zutaten für die Menuezubereitung')
    preparation_steps: list[str] = Field(description='Zubereitungsschritte')

def get_agent():
    # model = get_model(llm_provider=LlmProvider.OPENROUTER, llm_model=LlmModel.OPENAI_GPT_5_1)
    model = get_model(llm_provider=LlmProvider.OPENROUTER, llm_model=LlmModel.OPENAI_GPT_5_MINI)
    # model = get_model(llm_provider=LlmProvider.OLLAMA, llm_model=LlmModel.GPT_OSS_20B)
    # model = get_model(llm_provider=LlmProvider.OPENROUTER, llm_model=LlmModel.GROK_4)
    return Agent(
        model=model,
        system_prompt=('Du bist ein Pizzabäcker welcher Rezepte für kreative Pizzas kreirt. '
                       'Nutze das Tool set_oven_temperature für die Einstellung des Backofens.'),
        deps_type=Deps,
        tools=[
            Tool(set_oven_temperature, takes_ctx=True),
        ],
        retries=3,
        output_type=Recipe,
    )

async def main(user_prompt: str):
    deps = Deps(name='Peter')
    agent = get_agent()
    response = await agent.run(user_prompt=user_prompt, deps=deps)
    result: Recipe = response.output

    print(f'Antwort: {result.model_dump_json(indent=4)}')

    print('=====================================================================')
    settings = agent.model.settings
    print(f'Settings: {settings}')
    print(f'temperature: {settings.get('temperature')}')
    print(f'presence_penalty: {settings.get('presence_penalty')}')
    print(f'frequency_penalty: {settings.get('frequency_penalty')}')

    usage = response.usage()
    print(f"Input Tokens: {usage.input_tokens}")
    print(f"Output Tokens: {usage.output_tokens}")
    print(f"Total Tokens: {usage.total_tokens}")

if __name__ == '__main__':
    asyncio.run(main(user_prompt='Ich habe im Kühlschrank Lachs, Salami, Ananas und Tomaten '
                                 'Kreire mir eine Pizza. Da mein Backofen etwas alterschwach ist, '
                                 'kann die Temperatur nicht höher als 210 Grad eingestellt werden.'))
