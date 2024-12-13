from arcadepy import Arcade

print("--- BEFORE INSTANTIATE --")

client = Arcade(base_url="http://localhost:9099")

print("--- BEFORE CLIENT COMPLETION ---")
# Use the tools in a chat completion
response = client.chat.completions.create(
    messages=[{"role": "user", "content": "What is 6 times 7?"}],
    model="gpt-3.5",
    tool_choice="generate",
)

print("--- BEFORE RESPONSE RETURN ---")
print(response.choices[0].message.content)
