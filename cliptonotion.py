import re
import os
import pyperclip
import keyboard
from notion_client import Client
from dotenv import load_dotenv

# Load secrets from .env
load_dotenv()

NOTION_TOKEN = os.getenv("NOTION_TOKEN")
DATABASE_ID = os.getenv("DATABASE_ID")
HOTKEY = os.getenv("HOTKEY", "ctrl+alt+n")
DEFAULT_STATUS = os.getenv("DEFAULT_STATUS", "Applied")

# Initialise Notion client
notion = Client(auth=NOTION_TOKEN)

def extract_company_and_description(text):
    # Try to extract company name from the first line if it looks like a name
    lines = text.strip().split("\n")

    first_line = lines[0].strip()
    if 2 <= len(first_line.split()) <= 8:
        company = first_line
        description = "\n".join(lines[1:]).strip()
        return company, description

    match = re.search(r"([A-Z][a-zA-Z&\s,.]{2,40})", text)
    if match:
        company = match.group(1).strip()
        description = text.replace(company, "").strip()
        return company, description

    return text.strip(), ""

def send_to_notion(text):
    company, description = extract_company_and_description(text)

    # Split description into chunks of ≤ 2000 chars as Notion does not allow long blocks
    MAX_LEN = 2000
    chunks = [description[i:i+MAX_LEN] for i in range(0, len(description), MAX_LEN)]

    children = []
    for chunk in chunks:
        children.append({
            "object": "block",
            "type": "paragraph",
            "paragraph": {
                "rich_text": [
                    {"type": "text", "text": {"content": chunk}}
                ]
            }
        })

    notion.pages.create(
        parent={"database_id": DATABASE_ID},
        properties={
            "Name": {
                "title": [{"text": {"content": company}}]
            },
            "Status": {
                "select": {"name": DEFAULT_STATUS}
            }
        },
        children=children
    )

    print(f"Added {company} under {DEFAULT_STATUS}")


def main():
    print(f"Press {HOTKEY} to send clipboard content to Notion.")
    while True:
        if keyboard.is_pressed(HOTKEY):
            text = pyperclip.paste()
            if text.strip():
                send_to_notion(text)
            else:
                print("Clipboard is empty.")
            keyboard.wait(HOTKEY, suppress=True)

if __name__ == "__main__":
    main()
