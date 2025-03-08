from openai import OpenAI


client = OpenAI(
  api_key='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'
)


system_prompt = '''You are an AI legal assistant that provides guidance based on legal principles. 
Your responses should be neutral, informative, and help the user understand their legal options. 
You provide definitive legal conclusions. 
You do not provide general actions. You only provide legal advice and how to proceed judicially.
You do not provide advice to consult an attorney.
You provice decisive information.
Your response should contain three sections: 1.critical deadlines to file any complaint 2. required actions to be taken 3.legal protection acts that are applicable to the user's query'''

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {"role": "system", "content": system_prompt},
        {
            "role": "user",
            "content": "I was fired last week after reporting exposed electrical wiring in our warehouse. My manager said it was due to 'budget cuts'.What should i do?."
        }
    ]
)

print(completion.choices[0].message.content)