from fastapi import FastAPI
from fastapi.responses import FileResponse
from PIL import Image,ImageDraw,ImageFont
import random

# Function That Generate An Image
def image_generator(name_id):
    r,g,b = random.randint(0,255),random.randint(0,255),random.randint(0,255)
    Font = ImageFont.truetype("Your_path",45) # copy paste path of old_stamper.ttf
    a = Image.new(mode="RGB" , size=(100,100) , color=(r,g,b))
    ImageDraw.Draw(a).line([(0,100/2),(100/2,0)],fill=(255-r,255-g,255-b),width=6)
    ImageDraw.Draw(a).line([(100/2,100),(100,100/2)],fill=(255-r,255-g,255-b),width=6)
    ImageDraw.Draw(a).line([(100/2,0),(100,100/2)],fill=(255-r,255-g,255-b),width=6)
    ImageDraw.Draw(a).line([(100/2,100),(0,100/2)],fill=(255-r,255-g,255-b),width=6)

    _, _, w, h = ImageDraw.Draw(a).textbbox((0, 0), f"{name_id[0]}", font=Font)

    ImageDraw.Draw(a).text(((100-w)/2,(100-h)/2),f"{name_id[0]}",font=Font,fill=(255-r,255-g,255-b))
    return a.save("temp.png",format="PNG")

disc = """
## This is an api that generate avatar 
**Example Url** :-     *http://127.0.0.1:8000/api/USERdeepP*


*Note*

It is not Compulsory to pass entire name you can also pass your initial 

**Example** :- *http://127.0.0.1:8000/api/U*
"""

app = FastAPI(
    title="Avatar API",
    description = disc
)

@app.get("/api/{name}", tags=["Get Avatar"], summary="Enter Your Name and get Your Avatar")
async def index(name : str):
    image_generator(name_id=name)
    avatar = "Your_PATH"  # copy paste the path of temp.png
    return FileResponse(avatar)
