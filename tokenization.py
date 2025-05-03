def tokenize(text, vocab, max_token_length):

    unk_token = "This shouldn't ever happen"

    tokens = []
    i = 0
    while i < len(text):
        match = None
        # Try to find the longest matching token up to max_token_length
        for j in range(min(i + max_token_length, len(text)), i, -1):
            sub = text[i:j]
            if sub in vocab:
                match = sub
                break
        if match:
            tokens.append(vocab[match])  # Append the token ID from vocab
            i += len(match)  # Move by the length of the matched token
        else:
            tokens.append(vocab[unk_token])  # Use unknown token if no match
            i += 1  # Move by one character if no match
    return tokens

def untokenize(token_ids, vocab):
    text = ""
    for token_id in token_ids:
        text += vocab[token_id]
    return text