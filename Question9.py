import re

def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails

def validate_date(date_str):
    date_pattern = r'^\d{4}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$'
    return bool(re.match(date_pattern, date_str))

def replace_word(text, old_word, new_word):
    pattern = r'\b' + re.escape(old_word) + r'\b'
    return re.sub(pattern, new_word, text)

def split_non_alphanumeric(text):
    return re.split(r'[^a-zA-Z0-9]+', text)

def main():
    sample_text = """
    Contact us at info@example.com or support@company.co.uk.
    My personal email is john.doe123@gmail.com
    """
    emails = extract_emails(sample_text)
    print("I. Extracted emails:", emails)

    dates = ["2023-05-15", "2023-13-01", "2023-04-31", "23-05-15"]
    print("\nII. Date validation:")
    for date in dates:
        print(f"{date}: {'Valid' if validate_date(date) else 'Invalid'}")

    text = "The cat sat on the mat. The cat was happy."
    replaced_text = replace_word(text, "cat", "dog")
    print("\nIII. Word replacement:")
    print("Original:", text)
    print("Replaced:", replaced_text)

    sample_string = "Hello, World! How-are_you? 123"
    split_result = split_non_alphanumeric(sample_string)
    print("\nIV. Split by non-alphanumeric:")
    print("Original:", sample_string)
    print("Split:", split_result)

if __name__ == "__main__":
    main()