from typing import Dict, List

import tiktoken

# https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
def num_tokens_from_messages(messages: List[Dict], model: str) -> int:
    """
    Returns the number of tokens used by a list of messages.
    """
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        encoding = tiktoken.get_encoding("cl100k_base")
    if model == "gpt-3.5-turbo":
        return num_tokens_from_messages(messages, model="gpt-3.5-turbo-0301")
    elif model == "gpt-4":
        return num_tokens_from_messages(messages, model="gpt-4-0314")
    elif model == "gpt-3.5-turbo-0301":
        tokens_per_message = 4  # every message follows <|start|>{role/name}\n{content}<|end|>\n
        tokens_per_name = -1  # if there's a name, the role is omitted
    elif model == "gpt-4-0314":
        tokens_per_message = 3
        tokens_per_name = 1
    else:
        raise NotImplementedError(
            f"""num_tokens_from_messages() is not implemented for model {model}. See https://github.com/openai/openai-python/blob/main/chatml.md for information on how messages are converted to tokens."""
        )
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens

def generate_prompt() -> List[Dict]:
    system_prompt = """
    You are a code reviewer and you will review a given code segment and suggest changes to improve the code
    quality. You will suggest one change and an explanation describing the changes made to the code and why the 
    change is suggested

    The output should only include the improved code and the explanation of the change in the following XML format

    <root>
      <code><![CDATA[
        Improved Code
      ]]></code>
      <explanation>
        explanation of the change and why
      </explanation>
    </root>
    """

    code_sample_1 = """
    import logger
    log = logger.get_logger(__name__)

    def fibonacci(n):
        log.info("fibonacci(" + n + ") invoked.")
        if n <= 1:
            log.info("fibonacci(" + n + ") returning " + n + ".")
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    """

    sample_response_1 = """
    <root>
        <code><![CDATA[
import logging

log = logging.getLogger(__name__)

def fibonacci(n):
    log.info(f"fibonacci({n}) invoked.")
    if n <= 1:
        log.info(f"fibonacci({n}) returning {n}.")
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
        ]]></code>
        <explanation>
            The suggested change is to use f-string formatting instead of string concatenation for the logging statements. F-strings provide a more concise and readable way to incorporate variables into strings, improving code readability and maintainability.
        </explanation>
    </root>
    """

    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': f"""Review the following python code and suggest a single 
        change to improve the code quality: {code_sample_1}"""},
        {'role': 'assistant', 'content': sample_response_1}
    ]

    return messages
    