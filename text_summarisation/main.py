from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

class SummarizationRequest(BaseModel):
    text: str
    style: str

class EvaluationRequest(BaseModel):
    reference: str
    hypothesis: str

# Initialize the summarization pipeline with BART model
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

@app.post("/summarize")
async def summarize(request: SummarizationRequest):
    if request.style not in ["bullet_points", "paragraph", "headline"]:
        raise HTTPException(status_code=400, detail="Invalid style")
    
    # Generate the summary using the BART model
    summary = summarizer(request.text, max_length=150, min_length=30, do_sample=False)[0]['summary_text']
    
    # Format the summary based on the user's preference
    formatted_summary = format_summary(summary, request.style)
    return {"summary": formatted_summary}

def format_summary(summary: str, style: str) -> str:
    if style == "bullet_points":
        return "\n".join([f"- {point.strip()}" for point in summary.split(". ") if point])
    elif style == "paragraph":
        return summary
    elif style == "headline":
        return summary.split(". ")[0]
    else:
        return summary

def evaluate_summary(reference: str, hypothesis: str) -> dict:
    from rouge import Rouge
    rouge = Rouge()
    scores = rouge.get_scores(hypothesis, reference, avg=True)
    return scores

@app.post("/evaluate")
async def evaluate(request: EvaluationRequest):
    scores = evaluate_summary(request.reference, request.hypothesis)
    return scores
