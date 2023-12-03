def extract_brackets_content(text):
    start_index = text.find('(')
    end_index = text.find(')')
    if start_index != -1 and end_index != -1:
        return text[start_index + 1:end_index]
    else:
        return ""
input_text = "When he saw Sally (a girl he used to go to school with) in the shop, he could not believe his eyes. She was fantastic (as always)!"
result = extract_brackets_content(input_text)
print(result)