from fastapi import FastAPI, UploadFile, Depends
import shutil
import time
from lib.ocr_ticket import OcrTicket
from lib.token_security import token_checking
from lib.common import checking_file_extension
import os

app = FastAPI()
current_folder = os.getcwd()

@app.get("/")
async def root():
    return {"message": "Your app is running..."}


@app.post("/retrieve-ticket-number")
async def check_image(image: UploadFile, token: str = Depends(token_checking)):
    # Checking file extension
    file_extension = checking_file_extension(image)

    # Displays used token
    print("token used : ", token)

    # Save temporary file
    timestamp = int(time.time())
    file_location = f"{current_folder}/storage/input_{timestamp}.{file_extension}"
    with open(file_location.format(timestamp=timestamp), "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)

    # Lecture du numéro de ticket
    ocr = OcrTicket()
    code = ocr.get_ticket_number(file_location)
    return code if code else "Impossible de lire le numéro du ticket"
