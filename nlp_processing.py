from transformers import pipeline

# Load a pre-trained text-generation model (e.g., GPT-2)
nlp = pipeline('text-generation', model='gpt2')

def process_message(message, objects):

    if not objects:
        prompt = f"User's message: {message}. The image contains no recognizable objects. Can you describe what you see?"
    elif len(objects) == 1:
        prompt = f"User's message: {message}. The image contains a {objects[0]}. What would you like to know about it?"
    else:
        objects_list = ', '.join(objects[:-1]) + ", and " + objects[-1]
        prompt = f"User's message: {message}. The image contains {objects_list}. What would you like to know about them?"

    # Generate a response using the NLP model
    response = nlp(prompt, max_length=50, num_return_sequences=1)[0]['generated_text']
    
    return response
