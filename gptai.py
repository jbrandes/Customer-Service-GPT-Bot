import openai




openai.api_key = "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"

model_engine = "text-davinci-003"
prompt = input("Whatis your troubleshooting question? Please be as specific as possible. ")


completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,

)

response = completion.choices[0].text
print(response) 
