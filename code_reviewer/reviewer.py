import logging
import os
import openai
import xml.etree.ElementTree as ET
from dotenv import load_dotenv
from util import generate_prompt

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

load_dotenv(dotenv_path="../.env")
openai.api_key = os.getenv("API_KEY")

def parse_xml(xml_string):
    root = ET.fromstring(xml_string)
    code = root.find('code').text.strip()
    explanation = root.find('explanation').text.strip()
    return code, explanation

def review_code(file_path: str, model: str) -> None:
    #todo: read from file

    messages = generate_prompt()

    code = """
    import logging

    log = logging.getLogger(__name__)

    def fibonacci(n):
        log.info(f"fibonacci({n}) invoked.")
        if n <= 1:
            log.info(f"fibonacci({n}) returning {n}.")
            return n
        return fibonacci(n - 1) + fibonacci(n - 2)
    """

    messages.append({'role': 'user', 'content': f'Suggest another change for the code: {code}'})

    result = openai.ChatCompletion.create(
        model=model,
        messages=messages
    )

    print(result.choices[0].message.content)

    parsed_code, parsed_explanation = parse_xml(result.choices[0].message.content)

    print(parsed_code)

    print(parsed_explanation)

def main():
    review_code("", "gpt-3.5-turbo")

if __name__ == "__main__":
    main()
