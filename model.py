from transformers import pipeline

# Initialize the summarizer pipeline
summarizer = pipeline("summarization", model="t5-small")


def summarize_text(text):
    summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
    return summary[0]['summary_text']
