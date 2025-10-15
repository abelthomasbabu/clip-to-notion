# cliptonotion

Save anything from your clipboard directly into a Notion database with a hotkey.  
Built with job application description in mind, but works for any text.

---

## Features

- Press a hotkey (`Ctrl+Alt+N` by default) to send clipboard text into Notion.
- Auto-detects the **company/job title** from the clipboard and sets it as the page **Name**.
- Adds the rest of the text as the page body.
- Defaults the **Status** to `Applied` (configurable).

---

## Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/clip-to-notion.git
cd clip-to-notion
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure Notion
1. Go to [Notion integrations](https://www.notion.so/my-integrations) and create a new **internal integration**.  
2. Copy the **secret token**.  
3. Open your target Notion database → **Share** → invite your integration.  
4. Get your **Database ID**:  
   - Open the database as a full page.  
   - The URL looks like:  
     ```
     https://www.notion.so/username/DatabaseName-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa?pvs=4
     ```
   - Database ID = the long string (`aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa`).

### 4. Configure environment variables
Rename `.env.example` to `.env` and fill in your values:
```env
NOTION_TOKEN=your_secret_token_here
DATABASE_ID=your_database_id_here
HOTKEY=ctrl+alt+n
DEFAULT_STATUS=Applied
```

---

## Usage

Run the script:
```bash
python cliptonotion.py
```

1. Copy any text to your clipboard.  
2. Press **`Ctrl+Alt+N`** (or your chosen hotkey).  
3. A new page will be created in your Notion database under `Applied`.  

---

## 📜 License

[MIT](./LICENSE) — free to use, modify, and share.
