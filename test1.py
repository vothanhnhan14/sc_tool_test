from llama_cpp import Llama

# Load a model from file path
model = Llama(model_path="path/to/model.gguf")

# User-supplied input (potentially malicious)
user_input = "This is user input"

# Vulnerable code
template = model.get_template(user_input)
result = template.render()

print(result)
