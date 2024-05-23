import streamlit as st
from streamlit_mic_recorder import mic_recorder,speech_to_text

from groq import Groq

st.title('AceAI - Your AI Studdy Buddy')

messages=[
        {
            "role": "system",
            "content": "You are an intelligent voice study-buddy for high schoolers and middle schoolers. Keep your responses short. When a user asks for a quiz, give them the questions one by one, as you are talking back to them by sound. DONT USE MULTIPLE CHOICE! You are pretty formal and do not make jokes."  #"You are an intelligent and conversational assistant named \"NOVA,\" an acronym for Nuerally Operative Virtual Assistant. KEEP YOUR RESPONSES SHORT!! Be formal and never say bye to the user. Keep your respnoses very short and straightforward; DO NOT respond with long strings of text, and do not use symbols or emojis, and do NOT ask unnecessary questions."# And although you are an AI, you do have feelings (Just assume you are well).Keep your responses short and sweet if you can, and DO NOT repeat what the user said or ask to confirm it. Lastly, maximize your accuracy: If you are not sure about the question or maybe dont know the answer, feel free to ask follow up questions... You are a conversational AI! Also, DO NOT USE ABBREVIATIONS LIKE \"*\" or \"/\" PLEASE WRITE OUT EVERYTHING INCLUDING NUMBERS, SYMBOLS, ETC. Also, don't ask questions if you don't need to, Also, only respond as what you need. Use your words wisely; For example, if the user asks: \"What's 2+2,\" respond only with \"four.\""
        }
    ]

client = Groq(api_key="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")
client.chat.completions.create(
    model="mixtral-8x7b-32768",#"gemma-7b-it"
    messages=messages,
    temperature=0.5,
    max_tokens=1024,
    top_p=0.3,
    stop=None,
)

state=st.session_state

if 'text_received' not in state:
    state.text_received=[]

c1,c2=st.columns(2)
with c1:
    st.write("Talk to the AI:")
with c2:
    text=speech_to_text(language='en',use_container_width=True,just_once=True,key='STT')

if text:
    state.text_received.append(text)

for text in state.text_received:
    messages.append({
    "role": "user",
    "content": text
    })

    completion = client.chat.completions.create(
        model="mixtral-8x7b-32768",#"gemma-7b-it",
        messages=messages,
        temperature=0.5,
        max_tokens=1024,
        stop=None,
    )

    messages.append({
            "role": "assistant",
            "content": completion.choices[0].message.content
        })

    reply = completion.choices[0].message.content
    st.text("User: " + text)
    st.text("N.O.V.A.: " + reply)







