# %%
#install dependencies
%pip install anthropic python-dotenv

# %%
# Load env variables
from dotenv import load_dotenv
load_dotenv()

# %%
# Create an API Client  
from anthropic import Anthropic
client = Anthropic()
model = "claude-sonnet-4-6"


# %%
message = client.messages.create(
    model=model,
    max_tokens=100,
    messages=[
        {
            "role":"user",
            "content":"what is quantum computing? Answer in one line"
        }
    ]
)
print()

message = client.messages.create(
    model=model,
    max_tokens=100,
    messages=[
        {
            "role":"user",
            "content":"write amother line"
        }
    ]
)
print()

# %%
from dotenv import load_dotenv
import os

load_dotenv()

print(os.getenv("ANTHROPIC_API_KEY"))

# %%
print(message)

# %%
message.content[0].text


