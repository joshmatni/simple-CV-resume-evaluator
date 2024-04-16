# CV Analysis Tool

This tool helps analyze your CV against different job positions to determine how well your skills and experiences match the desired internship roles. It leverages the Zero-Shot Classification capabilities from the Hugging Face Transformers library to assess suitability for various tech-related internships.

## Features

- Analyze CVs for different job positions: AI Intern, DevOps Intern, and Frontend Intern.
- Provides a confidence score indicating the suitability for the chosen job position.

## Prerequisites

Before you run the program, ensure you have the following installed:

- Python 3.7 or higher
- PyPDF2
- Transformers library
- Argparse library

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-path>
   ```

2. **Install dependencies**
    ```bash
    pip install PyPDF2 transformers argparse
    ```

3. **Run the program**
    ```bash
    python cv_analysis.py <path-to-cv> <job-position>
    ```

### Arguments
- `path-to-cv`: The file path to your CV in PDF format.
- `job-position`: The job position you are applying for. It can be one of the following:
    - AI intern
    - DevOps intern
    - Frontend intern

#### Example
```bash
python cv_analysis.py example_cv.pdf AI intern
```

## Limitations
- The CV must be in a text-readable PDF format; scanned images are not supported.
- The program currently only supports predefined job positions and cannot dynamically handle other positions without additional configuration.