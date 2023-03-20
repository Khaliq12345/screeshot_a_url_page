from fastapi import FastAPI
from fastapi.responses import FileResponse
from html2image import Html2Image
hti = Html2Image()

app = FastAPI()

@app.get("/{full_path:path}")
def pred_image(full_path: str):
    hti.screenshot(url=full_path, save_as='image.jpg') # Capture the screenshot and save it as a file
    return FileResponse("image.jpg")
    



