

#HW4 Question-1  
import openai
import json
import time

# Set your OpenAI API key
api_key = "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"
openai.api_key = api_key

# Function to turn on the microwave with a delay
def turnOnMicrowave(delay):
    signal = {
        "action": "turn_on the microwave ",
        "delay": delay,
      
    }
    print(f"Signal sent: {json.dumps(signal)}")
    time.sleep(delay)
    return "Microwave turned on after delay."

prompt = "Hi, please turn on the microwave after a delay of 10 seconds"
messages = [{"role": "user", "content": prompt}]

functions = [
    {
        "name": "turnOnMicrowave",
        "description": "Turn on microwave after a specified delay (10 or 20 seconds)",
        "parameters": {
            "type": "object",
            "properties": {
                "delay": {
                    "type": "integer",
                    "description": "Delay time in seconds for turning on the microwave (10 or 20)",
                    "enum": [10, 20]
                },
            },
            "required": ["delay"],
        },
    }
]

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=messages,
    functions=functions,
    function_call="auto"
)

# take delay from the prompt and then compare it with the delay to know if it is within the range of delay or not
delay = None
choices = response['choices']
for choice in choices:
    if 'function_call' in choice['message']:
        delay_json = choice['message']['function_call']['arguments']
        extracted_delay = json.loads(delay_json).get("delay")
        if extracted_delay and int(extracted_delay) in [10, 20]:
            delay = int(extracted_delay)
            break


if delay:
    response_result = turnOnMicrowave(delay)
    print(response_result) 
else:
    print("Delay not specified within the expected range.")


