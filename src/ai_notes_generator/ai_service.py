from mistralai.client import Mistral

from ai_notes_generator.config import MISTRAL_API_KEY


def generate_notes(text: str) -> str:
    if not MISTRAL_API_KEY:
        raise ValueError("MISTRAL_API_KEY is missing in the .env file.")

    if not text or not text.strip():
        raise ValueError("No input text provided for note generation.")

    with Mistral(api_key=MISTRAL_API_KEY) as mistral:
        response = mistral.chat.complete(
            model="mistral-large-latest",
            messages=[
                {
                    "role": "user",
                    "content": (
                        "Create clear, short study notes from the following PDF text. "
                        "Use headings and bullet points where useful.\n\n"
                        f"{text[:3000]}"
                    ),
                }
            ],
            stream=False,
            response_format={"type": "text"},
        )

    return response.choices[0].message.content