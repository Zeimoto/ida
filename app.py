import requests
import gradio as gr
import json
from PIL import Image
from io import BytesIO
from resources import HF_ACCESS_TOKEN

def fetch_image(url):
    try:
        response = requests.get(url)
        image = Image.open(BytesIO(response.content))
        return image, response
    except Exception as e:
        return None

def url_to_image(url):
    image, message = fetch_image(url)
    if image:
        return image, message
    else:
        return "Invalid URL or Unable to Fetch Image"
    
def caption (url):
    
    image, desc = url_to_image(url)
    
    API_URL = "https://api-inference.huggingface.co/models/Salesforce/blip-image-captioning-large"
    headers = {"Authorization": "Bearer "+HF_ACCESS_TOKEN}
    print("Status code:",desc.status_code)
    
    if desc.status_code == 200:
        
        print("Image downloaded successfully")
        response = requests.post(API_URL, headers=headers, data=desc)
    else:
        print("Failed to download image")

    return image,json.loads(response.text)[0]["generated_text"]

text_input = gr.Textbox(
            label="URL",
            info="Image's URL",
            lines=5,
            value="https://1779092274.rsc.cdn77.org/temp/1714987285_ab89b05ca8071c563d50c6d85a7fdcbd.jpg"
        )
text_output = gr.Textbox(
            label="Description",
            info="Image's Description",
            lines=5,
            value=""
        )
image_output = gr.Image(label="Output Image")

demo = gr.Interface(
    fn=caption,
    description= "Get the description for this image",
    inputs=[text_input], 
    outputs=[image_output, text_output],
    title="Image Description Assistante",
    #capture_session=True
)

if __name__ == "__main__":
    demo.launch(share=True)