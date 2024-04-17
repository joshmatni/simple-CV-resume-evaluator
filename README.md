# CV Analysis Tool

This tool helps analyze your CV against different job positions to determine how well your skills and experiences match the desired internship roles. It leverages the Zero-Shot Classification capabilities from the Hugging Face Transformers library to assess suitability for various tech-related internships.

## Features

- Analyze CVs for different job positions, Example: AI Intern, DevOps Intern, Frontend Intern.
- Provides a confidence score indicating the suitability for the chosen job position.

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-path>
   ```
2. ** Create virtual environment**
    ```bash
    python -m venv venv
    ```
### Activate the virtual environment
#### On Windows
    ```bash
    .\venv\Scripts\activate
    ```

#### On Unix or MacOS
    ```bash
    source venv/bin/activate
    ```

3. **Install Dependencies**
    ```bash
    pip install -r requirements.txt
    ```

3. **Run the program**
    ```bash
    python cv_analysis.py <path-to-cv> --label <job-position>
    ```

### Arguments
- `path-to-cv`: The file path to your CV in PDF format.
- `job-position`: The job position you are applying for! Example:
    - AI
    - DevOps
    - Frontend

## Limitations
- The CV must be in a text-readable PDF format; scanned images are not supported.
- The program currently only supports predefined job positions and cannot dynamically handle other positions without additional configuration.