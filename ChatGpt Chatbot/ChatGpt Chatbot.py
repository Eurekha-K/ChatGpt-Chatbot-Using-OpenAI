import openai
import gradio
messages=[{'role':'user','content':'Explain about Chandrayan-3'}]
openai.api_key="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"
def CustomChatGpt(user_input):
    messages.append({'role':'user','content':user_input})
    response=openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=messages
)
    ChatGpt_response=response['choices'][0]['message']['content']
    messages.append({'role':'user','content':ChatGpt_response})
    return ChatGpt_response
demo=gradio.Interface(fn=CustomChatGpt,inputs='text',outputs='text',title="ChatGpt Bot")
demo.launch(share=True)
    