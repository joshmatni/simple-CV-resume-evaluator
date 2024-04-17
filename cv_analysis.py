# Brokee project!
import argparse
import PyPDF2
from transformers import pipeline
import os

def get_model() -> pipeline:
    return pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def analyze_cv(file_path: str, label: str, model) -> None:
    text = extract_cv(file_path)
    if not text:
        print("Failed to extract text from the file. Please ensure the file is not a scanned image or an unsupported format.")
        return

    results = model(text, candidate_labels=label)
    scores = results['scores']
    
    if scores:
        job_confidence_score = sum(scores) / len(scores)
    else:
        print("No scores were generated, unable to compute a confidence score.")
        return

    if job_confidence_score > 0.5:  # threshold
        print(f"You are a great candidate for the position with a confidence score of {job_confidence_score:.2f}!")
    else:
        print(f"More information might be needed to determine suitability for the position. The confidence score is {job_confidence_score:.2f}.")


def extract_cv(file_path: str) -> str:
    try:
        file_extension = os.path.splitext(file_path)[1].lower()
        if file_extension == '.pdf':
            with open(file_path, "rb") as file:
                pdf_reader = PyPDF2.PdfReader(file)
                text = "".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
            #print(text)
            return text
        elif file_extension == '.txt':
            with open(file_path, "r") as file:
                text = file.read()
            return text
        else:
            print("Unsupported file type. Please provide a PDF or text file.")
            return None
    except FileNotFoundError:
        print("The specified file was not found.")
        return None


def get_args():
    parser = argparse.ArgumentParser(description="Analyze your CV for suitability to a job position")
    parser.add_argument("file_path", type=str, help="Path to your CV")
    parser.add_argument("--label", type=str, required=True, help="Job label keyword")
    #parser.add_argument("--threshold", type=float, required=True, help="Threshold for determining candidate suitability")
    return parser.parse_args()

def main() -> None:
    args = get_args()
    try:
        model = get_model()
        analyze_cv(args.file_path, args.label, model)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()