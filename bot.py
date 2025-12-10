import logging
from pyrogram import Client, filters
from pyrogram.types import (
    Message, InlineKeyboardMarkup, InlineKeyboardButton,
    InlineQuery, InlineQueryResultArticle, InputTextMessageContent
)
from config import API_ID, API_HASH, BOT_TOKEN
from fonts import get_all_styles, apply_style, FONTS

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Client
app = Client(
    "font_bot_new",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

# In-memory cache to store text for callback handling
# Key: Message ID (of the bot's reply), Value: Original Text
TEXT_CACHE = {}

@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    """
    Handles the /start command.
    """
    welcome_text = (
        "👋 **Welcome to the Font Changer Bot!**\n\n"
        "I can convert your text into various fancy fonts.\n\n"
        "**How to use:**\n"
        "1. Send me any text in this chat.\n"
        "2. I will reply with multiple styled versions.\n"
        "3. Click the buttons to copy the style (if supported) or just copy the text.\n\n"
        "**Inline Mode:**\n"
        "Type `@YourBotName text` in any chat to see results instantly.\n\n"
        "Type /fonts to see available styles.\n\n"
        "👨‍💻 **Developer:** [MUFAZ-VK](https://github.com/MUFAZ-VK)"
    )
    
    # Add a button to the developer's profile
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("👨‍💻 Developer", url="https://github.com/MUFAZ-VK")]
    ])
    
    await message.reply_text(welcome_text, reply_markup=buttons, disable_web_page_preview=True)

@app.on_message(filters.command("fonts"))
async def fonts_command(client: Client, message: Message):
    """
    Handles the /fonts command to list available styles.
    """
    sample_text = "Font Style"
    text = "**Available Fonts:**\n\n"
    
    for style_name in FONTS.keys():
        styled_sample = apply_style(sample_text, style_name)
        text += f"• {style_name}: {styled_sample}\n"
        
    await message.reply_text(text)

@app.on_message(filters.text & filters.private)
async def handle_text(client: Client, message: Message):
    """
    Handles normal text messages in private chat.
    """
    text = message.text
    if not text:
        return

    styles = get_all_styles(text)
    
    # Create buttons for each style
    buttons = []
    row = []
    
    for style_name, styled_text in styles.items():
        # Keep button text short for grid layout
        # We can just use the style name or a very short preview
        # Let's use Style Name for clarity in grid
        btn_text = style_name
        
        row.append(InlineKeyboardButton(btn_text, callback_data=f"style|{style_name}"))
        
        if len(row) == 3:
            buttons.append(row)
            row = []
            
    # Add any remaining buttons
    if row:
        buttons.append(row)
    
    sent_msg = await message.reply_text(
        "**Here are your fonts:**\n(Tap a style to send it as a separate message for easy copying)",
        reply_markup=InlineKeyboardMarkup(buttons)
    )
    
    # Cache the text mapped to the bot's message ID
    # Use a simple limit or cleanup strategy if this was production (e.g. invalidation), 
    # but for a simple script, a dict is fine (will clear on restart).
    TEXT_CACHE[sent_msg.id] = text

@app.on_callback_query(filters.regex(r"^style\|"))
async def handle_style_callback(client: Client, callback_query):
    """
    Handles button clicks on styled text options.
    """
    try:
        data = callback_query.data.split("|")
        style_name = data[1]
        
        # Try to get text from cache first
        message_id = callback_query.message.id
        original_text = TEXT_CACHE.get(message_id)
        
        # Fallback to reply_to_message if not in cache (e.g. after restart)
        if not original_text:
            original_message = callback_query.message.reply_to_message
            if original_message and original_message.text:
                original_text = original_message.text
        
        if not original_text:
            await callback_query.answer("Original text not found (message too old or cache cleared).", show_alert=True)
            return

        styled_text = apply_style(original_text, style_name)
        
        await callback_query.message.reply_text(f"`{styled_text}`", parse_mode=None) # Code block for easy copy
        await callback_query.answer(f"Sent {style_name}!")
        
    except Exception as e:
        logger.error(f"Error in callback: {e}")
        await callback_query.answer("An error occurred.", show_alert=True)

@app.on_inline_query()
async def inline_query_handler(client: Client, query: InlineQuery):
    """
    Handles inline queries.
    """
    text = query.query.strip()
    
    if not text:
        # Show a placeholder or help
        await query.answer(
            results=[],
            switch_pm_text="Type text to see fonts",
            switch_pm_parameter="start"
        )
        return

    results = []
    styles = get_all_styles(text)
    
    for i, (style_name, styled_text) in enumerate(styles.items()):
        results.append(
            InlineQueryResultArticle(
                id=str(i),
                title=style_name,
                description=styled_text,
                input_message_content=InputTextMessageContent(
                    styled_text
                )
            )
        )
        
    await query.answer(results)

if __name__ == "__main__":
    print("Bot is running...")
    app.run()
