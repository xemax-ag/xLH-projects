from enum import StrEnum
from pydantic import Field, BaseModel
from pydantic_ai.models.openai import OpenAIChatModel, OpenAIResponsesModel
from pydantic_ai.providers.ollama import OllamaProvider
from pydantic_ai.providers.openrouter import OpenRouterProvider
from pydantic_ai.settings import ModelSettings
from config import config

class LlmModel(StrEnum):
    # OpenAI
    GPT_5_PRO = 'gpt-5-pro'
    GPT_5 = 'gpt-5'
    GPT_5_MINI = 'gpt-5-mini'
    GPT_5_NANO = 'gpt-5-nano'
    GPT_5_1 = 'gpt-5.1'  # https://platform.openai.com/docs/guides/latest-model
    # OpenRouter
    GEMINI_2_5_FLASH = 'google/gemini-2.5-flash'
    OPENAI_GPT_5_1 = 'openai/gpt-5.1'
    OPENAI_GPT_5_MINI = 'openai/gpt-5-mini'
    GROK_4 = 'x-ai/grok-4'
    # Ollama
    GPT_OSS_20B = 'gpt-oss:20b'

class LlmProvider(StrEnum):
    OPENAI = 'OpenAI'
    OPENROUTER = 'OpenRouter'
    OLLAMA = 'Ollama'

def get_model(llm_provider: LlmProvider, llm_model:LlmModel, settings: ModelSettings | None = None) \
        -> OpenAIResponsesModel:

    if settings is None:
        # temperature       # https://platform.openai.com/docs/api-reference/audio/createTranslation#audio_createtranslation-temperature
        # presence_penalty  # https://platform.openai.com/docs/api-reference/completions/create#completions_create-presence_penalty
        # frequency_penalty # https://platform.openai.com/docs/api-reference/chat/create#chat_create-frequency_penalty
        settings = ModelSettings(
            temperature=0.0,
            presence_penalty=0.0,
            frequency_penalty=0.0,
            parallel_tool_calls=True,)

    match llm_provider:
        case LlmProvider.OPENAI:
            """
            https://platform.openai.com/docs/models
            https://platform.openai.com/docs/models/compare
            https://platform.openai.com/settings/organization/limits
            https://platform.openai.com/settings/organization/billing/overview
            https://platform.openai.com/settings/organization/usage
            Model	    Input	Cached input	Output
            gpt-5.1	    $1.25	$0.125	        $10.00
            gpt-5-pro   $15.00	$-	            $120.00
            gpt-5	    $1.25	$0.125	        $10.00
            gpt-5-mini	$0.25	$0.025	        $2.00
            gpt-5-nano	$0.05	$0.005	        $0.40
            """
            model = OpenAIResponsesModel(model_name=llm_model, settings=settings)
            return model

        case LlmProvider.OPENROUTER:
            """
            https://openrouter.ai/models?fmt=cards&supported_parameters=tools
            https://openrouter.ai/settings/credits

            openai/gpt-5-mini $0.25/M input $2.00/M output
            mistralai/voxtral-small-24b-2507 $0.10/M input $0.30/M output
            x-ai/grok-code-fast-1 $0.20 input $1.50 output
            google/gemini-2.5-flash $0.30 input $2.50 output
            """

            model = OpenAIResponsesModel(model_name=llm_model,
                                         provider=OpenRouterProvider(),
                                         settings=settings)
            return model

        case LlmProvider.OLLAMA:
            # gpt-oss:20b

            model = OpenAIChatModel(model_name=llm_model,
                                    provider=OllamaProvider(base_url=f'http://localhost:11434/v1',
                                                            api_key='ollama'),
                                    settings=settings)
            return model

        case _:
            raise ValueError(f"Unsupported LLM provider: {llm_provider}")
