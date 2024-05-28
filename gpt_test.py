from openai import OpenAI;

client = OpenAI()
stream = client.chat.completions.create(
    messages=[
        {"role": "system", "content": "You are an expert in sports."},
        {"role": "user", "content": "Which NBA players have won MVP 4 or more times?"}
    ], stream=True, model="gpt-4-turbo")

for chunk in stream:
    print(chunk.choices[0].delta.content or "", end="")