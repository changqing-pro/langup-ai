from typing import Optional

import requests
import json
from langchain.chains import LLMChain
from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain.schema.language_model import BaseLanguageModel


from langup import config, BrainType


def get_chat_chain(
        system,
        openai_api_key=None,
        openai_proxy: str = None,
        openai_api_base: str = None,
        temperature: int = 0.7,
        max_tokens: int = None,
        chat_model_kwargs: Optional[dict] = None,
        llm_chain_kwargs: Optional[dict] = None
) -> BrainType:
    # chat_model = ChatOpenAI(
    #     max_retries=2,
    #     request_timeout=60,
    #     openai_api_key=openai_api_key or config.openai_api_key,
    #     openai_proxy=openai_proxy or config.proxy,
    #     openai_api_base=openai_api_base or config.openai_api_base,
    #     temperature=temperature,
    #     max_tokens=max_tokens,
    #     **chat_model_kwargs or {},
    # )
    # template = system
    # system_message_prompt = SystemMessagePromptTemplate.from_template(template)

    # human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    # chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    # chain = LLMChain(
    #     llm=chat_model,
    #     prompt=chat_prompt,
    #     **llm_chain_kwargs or {}
    # )


    param_map = {}
    bty_url = "https://ai-api.betteryeah.com/v1/public_api/webhook/d1d5a20f4ffa461ba06bf713bc89f2a4/execute_flow?Access-Key={}&Workspace-Id={}"

    param_map["message"] ="{text}"
    response = requests.post(bty_url, json=param_map)
    result = json.loads(response.content)
    print("*******************BTY返回" + result)
    run_result = result["data"]["run_result"]
    return run_result
    return bty_llm(human_template)


def get_llm_chain(system, llm: BaseLanguageModel, llm_chain_kwargs=None):
    template = system
    system_message_prompt = SystemMessagePromptTemplate.from_template(template)
    human_template = "{text}"
    human_message_prompt = HumanMessagePromptTemplate.from_template(human_template)
    chat_prompt = ChatPromptTemplate.from_messages([system_message_prompt, human_message_prompt])
    chain = LLMChain(
        llm=llm,
        prompt=chat_prompt,
        **llm_chain_kwargs or {}
    )
    return chain
