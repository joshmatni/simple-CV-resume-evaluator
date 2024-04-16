# Brokee project!
import argparse
import PyPDF2
from transformers import pipeline

def get_model() -> pipeline:
    return pipeline("zero-shot-classification", model="facebook/bart-large-mnli")

def analyze_cv(file_path: str, job_position: str, model: pipeline):
    text = get_pdf_text(file_path)
    if not text:
        print("Failed to extract text from the PDF. Please ensure the file is not a scanned image.")
        return

    job_categories = {
        "AI intern": {
            "labels": [
                "AI", "Machine Learning", "Data Science"
            ],
            "threshold": 0.25
        },
        "DevOps intern": {
            "labels": [
                "DevOps", "System Administration", "Infrastructure"
            ],
            "threshold": 0.3
        },
        "Frontend intern": {
            "labels": [
                "Frontend", "Web Development", "JavaScript"
            ],
            "threshold": 0.22
        }
    }

    results = model(text, candidate_labels=job_categories[job_position]['labels'])
    job_confidence_score = sum(results['scores']) / len(results['scores'])

    if job_confidence_score > job_categories[job_position]['threshold']:
        print(f"You are a great candidate for a {job_position} position with a confidence score of {job_confidence_score:.2f}!")
    else:
        print(f"More information might be needed to determine suitability for a {job_position} position. The confidence score is {job_confidence_score:.2f}.")


def get_pdf_text(file_path: str) -> str:
    try:
        with open(file_path, "rb") as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = "".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
        return text
    except FileNotFoundError:
        print("The specified file was not found.")
        return None

def get_args():
    parser = argparse.ArgumentParser(description="Analyze your CV for different job positions")
    parser.add_argument("file_path", type=str, help="Path to your CV")
    parser.add_argument("job_position", type=str, help="The job position you are applying for")
    return parser.parse_args()

def main() -> None:
    args = get_args()
    try:
        model = get_model()
        analyze_cv(args.file_path, args.job_position, model)
    except KeyError:
        print(f"The job position '{args.job_position}' is not recognized. Please specify one of the predefined positions.")

if __name__ == "__main__":
    main()