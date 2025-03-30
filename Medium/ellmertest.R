library(ellmer)

# Initialize  model
chat <- chat_ollama(model = "llama3.2:3b-instruct-q4_K_M")

#response
response <- chat$chat("When and why to use traceback() function in R?")

#saving in a file
file_path <- "ollama_response.txt"
writeLines(response, file_path)

shell.exec(file_path)

