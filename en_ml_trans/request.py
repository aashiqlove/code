import tritonclient.http as triton_http
import numpy as np
import sys

# Initialize Triton HTTP client
triton_client = triton_http.InferenceServerClient(url="192.168.1.43:8000", verbose=False)

# Prepare input data (replace with your actual data)
# input_text = sys.argv[1]  # Get the first argument passed to the script
# input_text = "ഹലോ ലോകം, ഞാൻ രാമനും ഞാനും അയോധ്യയിൽ നിന്നുള്ളവനാണ്."
input_text = "hi how are you"
# Prepare inputs
inputs = []
inputs.append(triton_http.InferInput("INPUT_TEXT", [1], "BYTES"))
inputs.append(triton_http.InferInput("INPUT_LANGUAGE_ID", [1], "BYTES"))
inputs.append(triton_http.InferInput("OUTPUT_LANGUAGE_ID", [1], "BYTES"))

inputs[0].set_data_from_numpy(np.array([input_text.encode('utf-8')], dtype=object))
inputs[1].set_data_from_numpy(np.array(["en"], dtype=object))  # Assuming 'en' is the language ID
inputs[2].set_data_from_numpy(np.array(["ml"], dtype=object))  # Assuming 'ml' is the language ID

# Fetch output
outputs = []
outputs.append(triton_http.InferRequestedOutput("OUTPUT_TEXT"))

# Perform inference
response = triton_client.infer("trans_model", inputs, request_id="<id_unknown>", outputs=outputs)

# Process output
output_data = response.as_numpy("OUTPUT_TEXT")[0]
translated_output = output_data.decode('utf-8').strip()

print("Translated Output:", translated_output)
