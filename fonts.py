import string

# Define the standard character set
LOWERCASE = string.ascii_lowercase
UPPERCASE = string.ascii_uppercase
DIGITS = string.digits

# Font style mappings
# Each key is a style name, and the value is a dictionary for replacement
FONTS = {
    "Bold": {
        # A-Z
        **dict(zip(UPPERCASE, "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙")),
        # a-z
        **dict(zip(LOWERCASE, "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳")),
        # 0-9
        **dict(zip(DIGITS, "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗"))
    },
    "Italic": {
        **dict(zip(UPPERCASE, "𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍")),
        **dict(zip(LOWERCASE, "𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧")),
        **dict(zip(DIGITS, "0123456789")) # Italic numbers mostly same or not standard in some sets
    },
    "Bold Italic": {
        **dict(zip(UPPERCASE, "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁")),
        **dict(zip(LOWERCASE, "𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛")),
    },
     "Monospace": {
        **dict(zip(UPPERCASE, "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉")),
        **dict(zip(LOWERCASE, "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣")),
        **dict(zip(DIGITS, "𝟶𝟷𝟸𝟹𝟺𝟻𝟼𝟽𝟾𝟿"))
    },
    "Script": {
        **dict(zip(UPPERCASE, "𝒜𝐵𝒞𝒟𝐸𝐹𝒢𝐻𝐼𝒥𝒦𝐿𝑀𝒩𝒪𝒫𝒬𝑅𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵")),
        **dict(zip(LOWERCASE, "𝒶𝒷𝒸𝒹𝑒𝒻𝑔𝒽𝒾𝒿𝓀𝓁𝓂𝓃𝑜𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏")),
    },
    "Bold Script": {
        **dict(zip(UPPERCASE, "𝓐𝓑𝓒𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩")),
        **dict(zip(LOWERCASE, "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃")),
    },
    "Fraktur": {
        **dict(zip(UPPERCASE, "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ")),
        **dict(zip(LOWERCASE, "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷")),
    },
    "Bold Fraktur": {
        **dict(zip(UPPERCASE, "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅")),
        **dict(zip(LOWERCASE, "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟")),
    },
    "Double Struck": {
        **dict(zip(UPPERCASE, "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ")),
        **dict(zip(LOWERCASE, "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫")),
        **dict(zip(DIGITS, "𝟘𝟙𝟚𝟛𝟜𝟝𝟞𝟟𝟠𝟡"))
    },
    "Sans Serif": {
        **dict(zip(UPPERCASE, "𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸 زی")),
        **dict(zip(LOWERCASE, "𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓")),
        **dict(zip(DIGITS, "𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫"))
    },
    "Sans Serif Bold": {
        **dict(zip(UPPERCASE, "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭")),
        **dict(zip(LOWERCASE, "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗉𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇")),
        **dict(zip(DIGITS, "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"))
    },
    "Sans Serif Italic": {
        **dict(zip(UPPERCASE, "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡")),
        **dict(zip(LOWERCASE, "𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻")),
        **dict(zip(DIGITS, "𝟢𝟣𝟤𝟥𝟦𝟧𝟨𝟩𝟪𝟫")) # Often same as regular sans digits
    },
    "Sans Serif Bold Italic": {
        **dict(zip(UPPERCASE, "𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕")),
        **dict(zip(LOWERCASE, "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯")),
        **dict(zip(DIGITS, "𝟬𝟭𝟮𝟯𝟰𝟱𝟲𝟳𝟴𝟵"))
    },
    "Small Caps": {
         **dict(zip(LOWERCASE, "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ")),
         **dict(zip(UPPERCASE, "ᴀʙᴄᴅᴇғɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢ")),
    },
    "Circles": {
        **dict(zip(UPPERCASE, "ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ")),
        **dict(zip(LOWERCASE, "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ")),
        **dict(zip(DIGITS, "⓪①②③④⑤⑥⑦⑧⑨"))
    },
    "Circles Dark": {
        **dict(zip(UPPERCASE, "🅐𝑩𝑸𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁")), # Partial mapping approximation or mix, prefer clean full sets if possible
        # Better mapping for Circles Dark (Negative Circled):
        **dict(zip(UPPERCASE, "🅐𝑩𝑸𝑸𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁")), # Placeholder, actually:
        **dict(zip(UPPERCASE, "🅐𝝗𝝠𝝡𝝢𝝣𝝤𝝥𝝦𝝧𝝨𝝩𝝪𝝫𝝬𝝭𝝮𝝯𝝰𝝱𝝲𝝳𝝴𝝵𝝶𝝷")), # No simple unicode block for A-Z negative circles except in supplement.
        # Let's use standard negative circled latin
        **dict(zip(UPPERCASE, "🅐𝑩𝑸𝑸𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁")), # Actually let's stick to reliable ranges.
        # A-Z negative circles are 1F150..1F169
        **dict(zip(UPPERCASE, [chr(0x1F150 + i) for i in range(26)])),
        **dict(zip(LOWERCASE, [chr(0x1F150 + i) for i in range(26)])), # Map lower to upper for this style
        **dict(zip(DIGITS, "⓿❶❷❸❹❺❻❼❽❾"))
    },
    "Squares": {
         **dict(zip(UPPERCASE, "🅰🅱🅲🅳🅴🅵🅶🅷🅸🉹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉")),
         **dict(zip(LOWERCASE, "🅰🅱🅲🅳🅴🅵🅶🅷🅸🉹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉")), 
    },
    "Squares White": {
         **dict(zip(UPPERCASE, "🄰𝓑🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉")),
         **dict(zip(LOWERCASE, "🄰𝓫🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉")),
    },
    "Inverted": {
        # Upside down map
        **dict(zip(UPPERCASE + LOWERCASE + DIGITS, "zʎxʍʌnʇsɹbdouɯlʞɾıɥƃɟǝpɔqɐZ⅄XϺΛ∩⊥SᴚΌԀONW˥➦ſIH⅁ℲƎpƆq∀68ㄥ9ϛㄣƐᴤƖ0"[::-1]))
    },
    "Mirrored": {
        **dict(zip(UPPERCASE + LOWERCASE + DIGITS, "ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba9876543210"[::-1]))
        # Note: True mirrored requires different chars like Ƨ for S, but simpler mirroring (reverse) is this.
        # Actually let's do character mapping for "Reflected" if possible, otherwise simple reverse is "Reverse".
    },
    "Slash": {
        **dict(zip(UPPERCASE + LOWERCASE + DIGITS, "ȺƀȼđɇfǥħɨɉꝁłmꞥøᵽꝗɍsŧᵾvẇxɏƶȺƀȼđɇfǥħɨɉꝁłmꞥøᵽꝗɍsŧᵾvẇxɏƶ0123456789"))     
    },
    "Strike": {
        # Using combining strike
        **{c: c + "\u0336" for c in UPPERCASE + LOWERCASE + DIGITS}
    },
    "Underline": {
        # Using combining underline
        **{c: c + "\u0332" for c in UPPERCASE + LOWERCASE + DIGITS}
    },
    "Wide": {
        **dict(zip(UPPERCASE, "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ")),
        **dict(zip(LOWERCASE, "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ")),
        **dict(zip(DIGITS, "０１２３４５６７８９"))
    },
    "Medieval": {
         **dict(zip(UPPERCASE, "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅")),
         **dict(zip(LOWERCASE, "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟")),
    },
    "Currency": {
        # Fun currency mapping
         **dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ", "₳฿₵ĐɆ₣₲ⱧłJ₭Ⱡ₥₦Ø₱QⱤ₴₮ɄV₩Ӿ¥Ⱬ")),
         **dict(zip("abcdefghijklmnopqrstuvwxyz", "₳฿₵ĐɆ₣₲ⱧłJ₭Ⱡ₥₦Ø₱QⱤ₴₮ɄV₩Ӿ¥Ⱬ")),
    },
    "Parentheses": {
         **dict(zip(UPPERCASE, [f"({c})" for c in UPPERCASE])),
         **dict(zip(LOWERCASE, [f"({c})" for c in LOWERCASE])),
         **dict(zip(DIGITS, [f"({c})" for c in DIGITS])),
    },
    "Regional": {
         # Regional Indicator Symbols (Flags) for A-Z
         **dict(zip(UPPERCASE, [chr(0x1F1E6 + i) for i in range(26)])),
         **dict(zip(LOWERCASE, [chr(0x1F1E6 + i) for i in range(26)])),
    },
    "Superscript": {
        **dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789", "ᴬᴮᶜᴰᴱᶠᴳᴴᴵᴶᴷᴸᴹᴺᴼᴾᵠᴿˢᵀᵁⱽᵂˣʸᶻᵃᵇᶜᵈᵉᶠᵍʰⁱʲᵏˡᵐⁿᵒᵖqʳˢᵗᵘᵛʷˣʸᶻ⁰¹²³⁴⁵⁶⁷⁸⁹"))
         # Note: lowercase q is often missing in standard superscript sets, using q or small replacement if available
    }
}

def apply_style(text: str, style_name: str) -> str:
    """
    Applies a specific font style to the text.
    """
    if style_name not in FONTS:
        return text
    
    mapping = FONTS[style_name]
    return "".join(mapping.get(char, char) for char in text)

def get_all_styles(text: str) -> dict[str, str]:
    """
    Returns a dictionary of {style_name: styled_text} for all available styles.
    """
    return {name: apply_style(text, name) for name in FONTS.keys()}
