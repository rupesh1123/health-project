def get_ai_response(user_message):
    user_message = user_message.lower()

    # Define tag patterns and responses
    tags = {
        "diet": [
            "diet", "food", "eat", "nutrition", "meal"
        ],
        "workout": [
            "workout", "exercise", "gym", "training", "pushup", "fitness"
        ],
        "sleep": [
            "sleep", "rest", "tired", "nap"
        ],
        "hydration": [
            "drink", "water", "hydration", "thirst"
        ],
        "mental": [
            "stress", "mental", "relax", "mind", "focus"
        ],
        "yoga": [
            "yoga","postures","breathing","dance"
        ],
    }

    responses = {
        "diet": "Balanced Diet  Includes all nutrients: carbohydrates, proteins, fats, vitamins, minerals, and water.",
        "workout": "Start with 30 minutes of exercise daily. Consistency is key!",
        "sleep": "You need at least 7-8 hours of sleep for full recovery.",
        "hydration": "Drink at least 2-3 liters of water daily to stay hydrated.",
        "mental": "Try meditation, journaling, or talking to someone you trust.",
        "yoga":"try different yogasanas."
    }

    # Match tags based on keywords
    for tag, keywords in tags.items():
        for keyword in keywords:
            if keyword in user_message:
                return responses[tag]

    return "I'm here to help! Try asking about diet, workout, sleep, hydration, yoga or mental health."
