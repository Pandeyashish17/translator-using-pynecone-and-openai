import openai
import pynecone as pc

openai.api_key = "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"


class State(pc.State):
    """The app state."""
    
    text = ""
    language = ""
    translation = ""

    def translate(self):
       """Translate the text to the given language."""

       if not self.text:
            return pc.window_alert("Please enter some text.")
       if not self.language:
            return pc.window_alert("Please select a language.")
        
        
       prompt = f"translate '{self.text}' to {self.language}"
       
       
       try:
            response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=0.5,
                max_tokens=1000,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                stop=None,
            )
            self.translation = response.choices[0].text.strip()
       except:
            return pc.window_alert("Error with OpenAI API.")
        
        
def index():
    return pc.center(
        pc.vstack(
           pc.heading("Language Translator", font_size="1.5em"),  
           pc.input(placeholder="Enter text to translate", on_blur=State.set_text,variant="outlined"),
           pc.select(
                ["", "German", "French", "Spanish", "Italian","Hindi","Chinese","nepali",""],
                on_change=State.set_language,
                options_config={"style": "height: 3em; font-size: 1em;"}, 
                variant="outlined"
            ),
           pc.button(
                "Translate",
                on_click=[State.translate],
                width="20%",
                color_scheme="#F0A04B",
                variant="outline",
                border_radius="1em",
                ),
            pc.divider(),
            pc.cond(
                 State.translation,
                 pc.text(State.translation, font_size="1.25em"),
                ),

            bg="#E1EEDD",
            width="50vw",
            padding="2em",
            shadow="lg",
            border_radius="lg",
        ),
        width="100%",
        height="100vh",
        background="#FEFBE9",
    )
    
    
    # Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, title="Pynecone: Language Translator")
app.compile()
        
        
        
        
       
       
       
       
      
    


