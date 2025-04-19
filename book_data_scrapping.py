from youtube_transcript_api import YouTubeTranscriptApi
import ollama
import json
import os
import re

#settings
video_id = "wp7Lz1svVro"
book_title = "Rich Dad Poor Dad"
max_words_per_chunk = 300
output_path = "data/Rich_Dad_Poor_Dad_chapter_chunks.json"

#Normalizer
def normalize_fields(raw_dict):
    return {
        "chapter": raw_dict.get("Inferred Chapter Title") or raw_dict.get("chapter") or "unknown",
        "summary": raw_dict.get("Short Paragraph Summary") or raw_dict.get("summary") or "",
        "takeaways": raw_dict.get("Key Actionable Takeaways") or
                     raw_dict.get("Two Key Actionable Takeaways") or
                     raw_dict.get("takeaways") or [],
        "quote": raw_dict.get("Motivational Quote") or raw_dict.get("quote") or ""
    }


try:
    transcript=YouTubeTranscriptApi.get_transcript(video_id)
    print(f"Fetched the transcript with {len(transcript)} segments.")
except Exception as e:
    print(f"Error fetching transcript: {e}")
    exit()


def chunk_transcript(entries, max_words=300):
    chunks = []
    current_chunk = ""
    for entry in entries:
        text = entry['text']
        words = text.split()
        if len(current_chunk.split()) + len(words) <= max_words:
            current_chunk += " " + text
        else:
            chunks.append(current_chunk.strip())
            current_chunk = text
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

chunks = chunk_transcript(transcript, max_words=max_words_per_chunk)
print(f" Created {len(chunks)} chunks.")

summarized_chunks = []

for i, chunk in enumerate(chunks):
    prompt = f"""
You are a helpful summarizer AI. You will read a section from the book 'The 7 habits of highly effective people' and return structured summary data in JSON format.

Please return:
1. The inferred chapter title.
2. A short paragraph summary.
3. Two key actionable takeaways.
4. One motivational quote.

Transcript Chunk:
\"\"\"{chunk}\"\"\"

Return only JSON.
"""
    print(f" Summarizing chunk {i+1}...")
    response = ollama.chat(
        model="mistral",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    try:
        raw_output = response['message']['content']
        match = re.search(r"\{.*\}", raw_output, re.DOTALL)
        if match:
            parsed_json = json.loads(match.group())
            summary_data = normalize_fields(parsed_json)
        else:
            raise ValueError("No JSON found in response")
    except Exception as e:
        print(f" Chunk {i+1} response was not valid JSON: {e}")
        summary_data = {
            "chapter": "unknown",
            "summary": "",
            "takeaways": [],
            "quote": "",
            "raw_response": response['message']['content']
        }

    summary_data["book"] = book_title
    summary_data["chunk_id"] = i + 1
    summary_data["text"] = chunk

    summarized_chunks.append(summary_data)

# Save File
os.makedirs("data", exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(summarized_chunks, f, indent=2)

print(f" Final summarized RAG data saved to: {output_path}")