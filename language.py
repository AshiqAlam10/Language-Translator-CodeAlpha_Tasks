import gradio as gr
from googletrans import Translator

def translate_text(text, dest_lang):
    translator = Translator()
    translation = translator.translate(text, dest=dest_lang)
    return translation.text

interface = gr.Interface(
    fn=translate_text,
    inputs=[
        gr.Textbox(label="Enter text to translate"),
        gr.Dropdown(label="Select language", choices=["Spanish", "French", "German", "Chinese (Simplified)", "Arabic", "Hindi", "English","Italian","Punjabi","Urdu"]),
    ],
    outputs=gr.Textbox(label="Translated text"),
    title="Language Translator",
    description="Translate text from one language to another",
)
interface.launch( inbrowser=True)