import re

def filter_input(string, special_characters):
    strip_space = string.strip()
    strip_tags = re.sub(r"(<.*?)", "", strip_space)
    strip_chars = re.sub(special_characters, "", strip_tags)
    return strip_chars

def format_name(name):
    filtered = filter_input(name, r"([^a-zA-Z ]+)")
    formatted = filtered[0].upper() + filtered[1:]
    return formatted

def escape_html(string):
    neutralize_amp = string.replace("&", "&amp;")
    neutralize_quote = neutralize_amp.replace('"', "&quot;")
    neutralize_lt = neutralize_quote.replace('<', "&lt;")
    neutralize_gt = neutralize_lt.replace('>', "&gt;")
    return neutralize_gt