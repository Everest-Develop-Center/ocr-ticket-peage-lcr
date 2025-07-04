from fastapi import FastAPI, UploadFile, Depends
import shutil
import time
from lib.ocr_ticket import OcrTicket
from lib.token_security import token_checking
from lib.common import checking_file_extension

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/check-image")
async def check_image(image: UploadFile):
    timestamp = int(time.time())
    file_location = f"storage/input_{timestamp}.png"
    with open(file_location.format(timestamp=timestamp), "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    return {"message": "Image successfully saved"}

@app.post("/retrieve-ticket-number")
async def check_image(image: UploadFile, token: str = Depends(token_checking)):
    # Checking file extension
    checking_file_extension(image)

    # Displays used token
    print("token used : ", token)

    # Save temporary file
    timestamp = int(time.time())
    file_location = f"storage/input_{timestamp}.png"
    with open(file_location.format(timestamp=timestamp), "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # Lecture du numéro de ticket
    ocr = OcrTicket()
    code = ocr.get_ticket_number(file_location)
    return code if code else "Impossible de lire le numéro du ticket"
