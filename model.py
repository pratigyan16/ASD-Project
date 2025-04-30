
def predict_naive_bayes(input_data):
    qchat_score = input_data['feature1']
    age_months = input_data['feature2']

    if qchat_score >= 6 and age_months >= 18:
        return "Positive (Likely ASD)"
    else:
        return "Negative (Unlikely ASD)"

def get_bot_response(user_input):
    user_input = user_input.lower()
    if "autism" in user_input:
        return "Autism is a neurodevelopmental condition that affects communication and behavior."
    elif "therapy" in user_input:
        return "We offer ABA, Speech, and Occupational therapies for toddlers."
    elif "diagnosis" in user_input:
        return "You can use our Diagnosis page to check symptoms."
    else:
        return "Sorry, I didn't understand that. Please ask something related to autism, diagnosis, or therapy."
