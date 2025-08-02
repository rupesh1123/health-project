def generate_response(user_input):
    user_input = user_input.lower()

    if "diet" in user_input:
        return "A healthy diet includes vegetables, fruits, lean proteins, and whole grains."
    elif "exercise" in user_input:
        return "Start with daily walking or beginner bodyweight exercises."
    elif "bmi" in user_input:
        return "BMI = weight(kg) / height²(m²). Ideal range is 18.5–24.9."
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! I'm your fitness assistant. Ask me about diet, exercise, or goals."
    else:
        return "Try asking about diet, exercise, or how to set goals!"
