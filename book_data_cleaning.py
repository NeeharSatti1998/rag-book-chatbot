import json
import re
from pathlib import Path

# Load the raw JSON file
file_path = Path(r"C:/Users/neeha/Downloads/RAG chatbot/data/The_7_habits_of_highly_effective_people_chapter_chunks.json")
with open(file_path, "r", encoding="utf-8") as f:
    chunks = json.load(f)

def extract_json_from_raw(raw_text):
    """Extract a JSON object from a raw string (if present)."""
    try:
        match = re.search(r"\{.*\}", raw_text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except:
        return None
    return None

def normalize_fields(raw_dict):
    """Normalize field names from raw LLM output."""
    return {
        "chapter": raw_dict.get("Inferred Chapter Title") or raw_dict.get("chapter") or "unknown",
        "summary": raw_dict.get("Short Paragraph Summary") or raw_dict.get("summary") or "",
        "takeaways": raw_dict.get("Key Actionable Takeaways") or
                     raw_dict.get("Two Key Actionable Takeaways") or
                     raw_dict.get("takeaways") or [],
        "quote": raw_dict.get("Motivational Quote") or raw_dict.get("quote") or ""
    }

# Clean and normalize
cleaned_chunks = []

for chunk in chunks:
    if chunk.get("chapter") == "unknown" and "raw_response" in chunk:
        extracted = extract_json_from_raw(chunk["raw_response"])
        if extracted:
            normalized = normalize_fields(extracted)
            chunk.update(normalized)
            chunk.pop("raw_response", None)
    cleaned_chunks.append(chunk)

# Save the cleaned file
cleaned_path = Path(r"C:/Users/neeha/Downloads/RAG chatbot/data/The_7_habits_of_highly_effective_people_chapter_chunks.json")
with open(cleaned_path, "w", encoding="utf-8") as f:
    json.dump(cleaned_chunks, f, indent=2)

cleaned_path.name