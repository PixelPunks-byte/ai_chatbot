from nlp_processing import process_message
from image_classification import classify_image

def integrate(image, message):

    objects = classify_image(image)
    
    response = process_message(message, objects)
    
    return response, objects
