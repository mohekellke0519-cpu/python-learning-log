import openai

client = openai.OpenAI(api_key="YOUR_API_KEY")

response = client.chat.completions.create(
    model="gpt-4.1-mini",
    messages=[
        {"role": "user", "content": "Pythonでじゃんけんゲーム作って"}
    ]
)

print(response.choices[0].message.content)