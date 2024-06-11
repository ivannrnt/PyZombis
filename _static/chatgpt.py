from openai import OpenAI
import os

client = OpenAI(
    api_key=os.environ.get("openai_key")
)

def GetResponse(prompt):
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content" : "You are an assistant for python lerners, you will be provided with a piece of Python code, and your task is to find and fix the error if it has, if not just give a congratulations message"
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_tokens=500,
        top_p=1
    )

    response = completion.choices[0].message.content #save response
    return response


if __name__ == "__main__":
    prompt = "Tengo este codigo pero tendrá un error?, como lo soluciono?"
    prompt += """
    # Haga un programa que en una funcion pida dos números enteros y devuelva la suma de esos dos números.
    def suma(n, m):
        return n m
    """
    response = GetResponse(prompt)
    print (response)