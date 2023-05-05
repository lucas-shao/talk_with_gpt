from langchain import PromptTemplate
from pai.common.chains.pai_chain import PaiChain
from pai.enum.model_type_enum import ModelType

template = "以下问题请用中文回答我 : {question}"


def chat_with_gpt(question):
    pai_chain = PaiChain()
    out = pai_chain.llm_run(
        PromptTemplate(
            template=template,
            input_variables=["question"],
        ),
        # docs=docs,
        model_type=ModelType.CHAT_OPENAI.value,
        model_name='gpt-3.5-turbo',
        format_prompt_value={
            'question': question,
        },
    )
    return out


if __name__ == "__main__":
    chat_with_gpt("What is your name?")
