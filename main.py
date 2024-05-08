from llama_index.core.llms import ChatMessage
from llama_index.llms.litellm import LiteLLM
from config import settings


# Define a chat message
message = ChatMessage(role="user", content="Hey! how's it going?")

# Initialize LiteLLM with the desired model
llm = LiteLLM(
    model=settings.chat_completion_kwargs.model, 
    api_key=settings.chat_completion_kwargs.api_key, 
    api_base=settings.chat_completion_kwargs.api_base
    )

# Call the chat method with the message
chat_response = llm.chat([message])

# Print the response
print(chat_response)