def find_candidates(keyword):
    print(f"Searching resumes for: {keyword}")
    return ["Alice Johnson", "Bob Smith"]

if __name__ == "__main__":
    result = find_candidates("Python Developer")
    print("Found:", result)
