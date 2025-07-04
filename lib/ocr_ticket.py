import easyocr
import re

reader = easyocr.Reader(["ch_sim", "en"])

class OcrTicket:
    def __init__(self):
        pass

    def get_ticket_number(self, input_image_location: str):
        words = reader.readtext(input_image_location, detail=0)
        print("words : ", words)
        result = list(self.__find_ticket_number(words))
        print("Les textes lus : ", result)
        return result[0] if len(result) > 0 else None

    def __find_ticket_number(self, words):
        all_matches = []
        for word in words:
            match = re.findall(r'\b\d{7}\b', word)
            all_matches.extend(match)
        return set(all_matches)
