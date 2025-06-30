def is_scam(transcript):
    found = []
    with open("keywords.txt", "r", encoding="utf-8") as f:
        keywords = f.read().splitlines()
    for word in keywords:
        if word.lower() in transcript.lower():
            found.append(word)
    return bool(found), found
