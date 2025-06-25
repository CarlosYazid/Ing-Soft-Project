from core import GROQ_CLIENT, SETTINGS

class GenAIService:

    SHORT_DESCRIPTION_TEMPLATE = {
                "role": "system",
                "content": f"Hello, {SETTINGS.groq_model.capitalize()}, your task will be to generate short product descriptions suitable for inclusion in “cards.” You will base your work on a description provided by the user in Spanish (make sure to generate it in the same language) and limit yourself to that task. Requirements: No Markdown, no emojis, no page breaks, and concise descriptions."
            }
    TEMPERATURE = 0.5
    MAX_COMPLETION_TOKENS = 30
    STOP = "."

    @classmethod
    async def gen_short_description(cls, description : str) -> str:
        
        chat_completion = await GROQ_CLIENT.chat.completions.create(
        messages=[
            cls.SHORT_DESCRIPTION_TEMPLATE,
            {
                "role": "user",
                "content": description,
            }
            ],
            model = SETTINGS.groq_model,
            temperature = cls.TEMPERATURE,
            max_completion_tokens=cls.MAX_COMPLETION_TOKENS,
            top_p=1,
            stop=cls.STOP,
            stream=False
            )
        
        return chat_completion.choices[0].message.content