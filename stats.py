def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def count_chars(text: str):
    letter_dict = {}
    for ch in text:
        if not ch.isalpha():
            continue

        if ch.lower() not in letter_dict:
            letter_dict[ch.lower()] = 1
        
        else:
            letter_dict[ch.lower()] += 1

    return letter_dict


def sort_result(results: dict):
    results_list = []
    for key in results:
        results_list.append({"char": key, "num": results[key]})

    results_list.sort(reverse=True, key=lambda x: x["num"])
    return results_list
    