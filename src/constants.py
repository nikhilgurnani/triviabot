"""
constants.py
"""

URL = "https://slack.com/api/views.open"

CATEGORIES = [
    "General Knowledge",
    "Entertainment: Books",
    "Entertainment: Film",
    "Entertainment: Music",
    "Entertainment: Musicals & Theatres",
    "Entertainment: Television",
    "Entertainment: Video Games",
    "Entertainment: Board Games",
    "Science & Nature",
    "Science: Computers",
    "Science: Mathematics",
    "Mythology",
    "Sports",
    "Geography",
    "History",
    "Politics",
    "Art",
    "Celebrities",
    "Animals",
    "Vehicles",
    "Entertainment: Comics",
    "Science: Gadgets",
    "Entertainment: Japanese Anime & Manga",
    "Entertainment: Cartoon & Animations",
]

CATEGORY_OPTIONS = list(
    map(
        lambda option: {
            "text": {"type": "plain_text", "text": option},
            "value": option,
        },
        CATEGORIES,
    )
)

MODAL = {
    "title": {"type": "plain_text", "text": "Super Trivia"},
    "submit": {"type": "plain_text", "text": "Submit"},
    "type": "modal",
    "callback_id": "modal-identifier",
    "close": {"type": "plain_text", "text": "Cancel"},
    "blocks": [
        {
            "type": "section",
            "text": {"type": "mrkdwn", "text": "Choose Categories",},
            "accessory": {
                "type": "multi_static_select",
                "placeholder": {"type": "plain_text", "text": "Select categories"},
                "options": CATEGORY_OPTIONS,
                "action_id": "create_feedback_final_step",
            },
        },
    ],
}
