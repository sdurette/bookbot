def sort_on(dict):
    return dict["value"]

def count_letters(in_text):
    lower_text = in_text.lower()
    num_letters = len(lower_text)
    letter_counts = {}

    for char_key in lower_text:
        if char_key.isalpha():
            if not char_key in letter_counts:
                letter_counts[char_key] = 0

            current_val = letter_counts[char_key]
            letter_counts[char_key] += 1

    #letter_counts.sort(reverse=True, key="value")
    sorted_letter_counts_list = sorted(
        letter_counts.items(),
        key=lambda x:x[1],
        reverse=True
    )

    sorted_letter_counts_dict = dict(sorted_letter_counts_list)

    for key in sorted_letter_counts_dict:
        print(f"The '{key}' character was found {letter_counts[key]} times")

    #return letter_counts

def count_words(words):
    word_list = words.split()
    return len(word_list)

def main():
    full_file = "books/frankenstein.txt"
    with open(full_file) as f:
        file_contents = f.read()

    print(f"--- Begin report of {full_file} ---")
    print(f"{count_words(file_contents)} words found in the document")
    print(" ")
    count_letters(file_contents)
    print("--- End report ---")
main()
