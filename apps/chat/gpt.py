import openai
from decouple import config as env_config


def gpt3_generate(prompt):
    openai.api_key = env_config('OPENAI_API_KEY')

    response = openai.Completion.create(
        engine="davinci",
        model="gpt-3.5-turbo",
        prompt=prompt,
        max_tokens=4096,
        temperature=0.7,
        n=1,
        stop=None,
    )

    return response.choices[0].text.strip()
