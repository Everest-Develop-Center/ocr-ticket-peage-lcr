from fastapi import UploadFile, HTTPException

def checking_file_extension(filename: UploadFile) -> None:
    extension = filename.filename.split(".")[-1]
    if extension not in ["jpg", "jpeg", "png"]:
        raise HTTPException(status_code=404, detail="File type not supported")
