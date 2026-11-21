import json
import os

FILE_NAME = "subscriptions.json"

def load_subscriptions():
    """قراءة الاشتراكات المحفوظة من الملف"""
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        return []

def save_subscriptions(subscriptions):
    """حفظ قائمة الاشتراكات في الملف"""
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(subscriptions, file, ensure_ascii=False, indent=4)