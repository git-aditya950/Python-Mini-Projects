from plyer import notification
import random

quotes = [
    "Push yourself, because no one else is going to do it for you.",
    "Success doesn’t just find you. You have to go out and get it.",
    "Great things never come from comfort zones.",
    "Dream it. Wish it. Do it.",
    "Do something today that your future self will thank you for.",
    "Little things make big days.",
    "Don’t stop when you’re tired. Stop when you’re done.",
    "The harder you work for something, the greater you’ll feel when you achieve it."
]

selected_quote = random.choice(quotes)

notification.notify(
    title="💡 Daily Motivation",
    message=selected_quote,
    timeout=8
)
