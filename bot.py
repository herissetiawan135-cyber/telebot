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

# Cache untuk menyimpan teks asli agar callback button bisa dipakai
TEXT_CACHE = {}

# ====================== START COMMAND ======================
@app.on_message(filters.command("start"))
async def start_command(client: Client, message: Message):
    """
    Menangani perintah /start.
    """
    welcome_text = (
        "👋 **Selamat datang di Font Changer Bot!**\n\n"
        "Aku bisa mengubah teks kamu menjadi berbagai gaya font menarik.\n\n"
        "**Cara pakai:**\n"
        "1. Kirim teks apa saja di chat ini.\n"
        "2. Aku akan membalas dengan beberapa versi bergaya.\n"
        "3. Klik tombol untuk menyalin gaya (jika tersedia) atau cukup salin teksnya.\n\n"
        "**Mode Inline:**\n"
        "Ketik `@NamaBotKamu teks` di chat mana saja untuk melihat hasil langsung.\n\n"
        "Ketik /fonts untuk melihat gaya font yang tersedia.\n\n"
        "👨‍💻 **Developer:** [dotzbaik80](https://te.me/dotzbaik80)"
    )
    
    # Tombol untuk developer
    buttons = InlineKeyboardMarkup([
        [InlineKeyboardButton("👨‍💻 Developer", url="https://te.me/dotzbaik80")]
    ])
    
    await message.reply_text(
        welcome_text,
        reply_markup=buttons,
        disable_web_page_preview=True,
        parse_mode="markdown"
    )

# ====================== FONTS COMMAND ======================
@app.on_message(filters.command("fonts"))
async def fonts_command(client: Client, message: Message):
    """
    Menangani perintah /fonts untuk menampilkan semua gaya font.
    """
    sample_text = "Font Style"
    text = "**Daftar Font Tersedia:**\n\n"
    
    for style_name in FONTS.keys():
        styled_sample = apply_style(sample_text, style_name)
        text += f"• {style_name}: {styled_sample}\n"
        
    await message.reply_text(text, parse_mode="markdown")

# ====================== HANDLE PRIVATE TEXT ======================
@app.on_message(filters.text & filters.private)
async def handle_text(client: Client, message: Message):
    """
    Menangani teks normal di chat pribadi.
    """
    text = message.text
    if not text:
        return

    styles = get_all_styles(text)
    
    # Membuat tombol untuk setiap gaya font
    buttons = []
    row = []
    
    for style_name, styled_text in styles.items():
        btn_text = style_name
        row.append(InlineKeyboardButton(btn_text, callback_data=f"style|{style_name}"))
        
        if len(row) == 3:  # 3 tombol per baris
            buttons.append(row)
            row = []
    
    if row:
        buttons.append(row)
    
    sent_msg = await message.reply_text(
        "**Berikut hasil font kamu:**\n(Klik gaya untuk mengirimnya sebagai pesan terpisah agar mudah disalin)",
        reply_markup=InlineKeyboardMarkup(buttons),
        parse_mode="markdown"
    )
    
    # Simpan teks asli di cache
    TEXT_CACHE[sent_msg.id] = text

# ====================== CALLBACK STYLE BUTTON ======================
@app.on_callback_query(filters.regex(r"^style\|"))
async def handle_style_callback(client: Client, callback_query):
    """
    Menangani klik tombol gaya font.
    """
    try:
        data = callback_query.data.split("|")
        style_name = data[1]
        
        message_id = callback_query.message.id
        original_text = TEXT_CACHE.get(message_id)
        
        if not original_text:
            # Fallback jika teks tidak ada di cache
            original_message = callback_query.message.reply_to_message
            if original_message and original_message.text:
                original_text = original_message.text
        
        if not original_text:
            await callback_query.answer(
                "Teks asli tidak ditemukan (mungkin sudah lama atau cache dibersihkan).",
                show_alert=True
            )
            return

        styled_text = apply_style(original_text, style_name)
        
        await callback_query.message.reply_text(
            f"`{styled_text}`", parse_mode=None
        )
        await callback_query.answer(f"Gaya {style_name} dikirim!")

    except Exception as e:
        logger.error(f"Error di callback: {e}")
        await callback_query.answer("Terjadi kesalahan.", show_alert=True)

# ====================== INLINE QUERY ======================
@app.on_inline_query()
async def inline_query_handler(client: Client, query: InlineQuery):
    """
    Menangani inline query.
    """
    text = query.query.strip()
    
    if not text:
        await query.answer(
            results=[],
            switch_pm_text="Ketik teks untuk melihat font",
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
                input_message_content=InputTextMessageContent(styled_text)
            )
        )
        
    await query.answer(results)

# ====================== RUN BOT ======================
if __name__ == "__main__":
    print("Bot berjalan...")
    app.run()
