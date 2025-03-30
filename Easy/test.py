import ollama

# Define the model and prompt
model_name = "llama3.2:3b-instruct-q4_K_M"
prompt = "when and why to use traceback() function in R?"

# Get the response from the model
response = ollama.chat(model=model_name, messages=[{"role": "user", "content": prompt}])

# Save the output to a file
with open("output.txt", "w", encoding="utf-8") as f: 
    f.write(response["message"]["content"])

print("Response saved to output.txt")
