import openai as op
import gradio as gr

## Need to create your own api key
op.api_key = "api_key"

List = [{"role": "system", "content": "You are ChatGPT Clone Bot"}]

## ChatGPT Clone Bot Function 
def ChatGptClone(Prompt):
    List.append({"role": "user", "content": Prompt})
    response = op.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = List
    )
    reply = response["choices"][0]["message"]["content"]
    List.append({"role": "assistant", "content": reply})
    return reply

## ChatGPT Clone Bot Application
def app():
  app = gr.Interface(fn=ChatGptClone, inputs = "text", outputs = "text", title = "ChatGPT Clone")
  return app.launch(share=True)

app()


