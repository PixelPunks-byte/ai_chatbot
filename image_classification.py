import tensorflow as tf
from tensorflow.keras.applications import ResNet50
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image as keras_image

# Load the pre-trained ResNet50 model
model = ResNet50(weights='imagenet')

def classify_image(image):
    img = keras_image.load_img(image, target_size=(224, 224))
    img_array = keras_image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)  # Create a batch axis

    img_array = preprocess_input(img_array)
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=5)[0]

    objects = [label for _, label, _ in decoded_predictions]
    return objects
