import os
import sys
from dotenv import load_dotenv

# Try to load .env, but don't fail if it's missing or empty,
# because the user might hardcode values below.
load_dotenv()

# ------------------------------------------------------------------
# ENTER YOUR CREDENTIALS HERE IF NOT USING .ENV
# ------------------------------------------------------------------
# You can get these from my.telegram.org and @BotFather
API_ID = "YOUR_API_ID"      # e.g., 123456
API_HASH = "YOUR_API_HASH"  # e.g., "0123456789abcdef0123456789abcdef"
BOT_TOKEN = "YOUR_BOT_TOKEN" # e.g., "123456789:ABCdef..."

# Overwrite with environment variables if they exist
API_ID = os.getenv("API_ID", API_ID)
API_HASH = os.getenv("API_HASH", API_HASH)
BOT_TOKEN = os.getenv("BOT_TOKEN", BOT_TOKEN)

# ------------------------------------------------------------------

# Validate credentials
# Check if they are still the default placeholders or empty
if API_ID == "YOUR_API_ID_HERE" or API_HASH == "YOUR_API_HASH_HERE" or BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
    print("\n[ERROR] Credentials missing!")
    print("Please open 'config.py' and replace the placeholders with your actual API_ID, API_HASH, and BOT_TOKEN.")
    print("OR ensure your .env file is correct and saved.\n")
    sys.exit(1)

try:
    API_ID = int(API_ID)
except ValueError:
    print(f"\n[ERROR] API_ID must be an integer. Got: {API_ID}\n")
    sys.exit(1)
