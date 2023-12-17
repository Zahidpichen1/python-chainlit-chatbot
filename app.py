import chainlit as cl
import openai

openai.api_key = "YOUR-API-KEY"


@cl.on_message
async def main(message: cl.Message):
    # Get user input
    user_input = message.content

    # Check if user wants to quit
    if user_input.lower() in ["quit", "exit", "bye"]:
        # End the conversation
        await cl.stop()

    # Call the GPT function
    response = chat_with_gpt(user_input)

    # Print the live chat text generation
    print(f"AI: {response}")

    # Send the GPT response back to the user
    await cl.Message(content=response).send()


def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    # Start the conversation loop
    cl.run()
