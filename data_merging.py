import json
from pathlib import Path

files = [
    Path(r"C:/Users/neeha/Downloads/RAG chatbot/data/atomic_habits_chapter_chunks.json"),
    Path(r"C:/Users/neeha/Downloads/RAG chatbot/data/The_7_habits_of_highly_effective_people_chapter_chunks_cleaned.json"),
    Path(r"C:/Users/neeha/Downloads/RAG chatbot/data/Rich_Dad_Poor_Dad_chapter_chunks.json")
]

all_chunks = []

for file in files:
    with open(file, "r", encoding="utf-8") as f:
        chunks = json.load(f)
        all_chunks.extend(chunks)


merged_path = Path(r"C:/Users/neeha/Downloads/RAG chatbot/data/merged_book_chunks.json")

with open(merged_path, "w", encoding="utf-8") as f:
    json.dump(all_chunks, f, indent=2)


print(f" Merged data saved to: {merged_path}")
merged_path.name