# KloudFarm CLI Documentation

## Overview
**KloudFarm CLI** is a command-line tool designed to analyze and visualize project architectures. It supports parsing application and Kubernetes architectures, and provides options to upload and view results.

---

## Installation

Ensure you have Python 3.7+ installed.

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the CLI:
   ```bash
   python cli.py --help
   ```

---

## Usage
### General Help
```bash
python cli.py --help
```

### Analyze Command Help
```bash
python cli.py analyze --help
```

---

## Commands and Options

### Basic Commands
- **Run All Parsers with Default Settings**  
  ```bash
  python cli.py analyze <directory_path>
  ```
- **Show Help for CLI**  
  ```bash
  python cli.py --help
  ```
- **Show Help for Analyze Command**  
  ```bash
  python cli.py analyze --help
  ```

### Authentication and Project Validation
- **Email**: The email address for authentication.  
- **Password**: The password for authentication.  
- **Project ID**: The unique ID of the project to associate the analysis with.

---

### Parser Selection
Use the `-p` or `--parser` flag to specify which parsers to run.  
- **Run All Parsers (Default)**  
  ```bash
  python cli.py analyze <directory_path> -p all
  ```
- **Run Only Application Parser**  
  ```bash
  python cli.py analyze <directory_path> -p application
  ```
- **Run Only Kubernetes Parser**  
  ```bash
  python cli.py analyze <directory_path> -p kubernetes
  ```

### View Options
- **View Results in CLI**  
  ```bash
  python cli.py analyze <directory_path> --view
  ```
- **Run Without Viewing Results**  
  ```bash
  python cli.py analyze <directory_path> --no-view
  ```

### Auto-Upload
- **Enable Auto-Upload (Default)**  
  ```bash
  python cli.py analyze <directory_path> --auto-upload
  ```
- **Disable Auto-Upload**  
  ```bash
  python cli.py analyze <directory_path> --no-auto-upload
  ```

---

## Example Usage

### Authenticate and Run All Parsers
```bash
python cli.py analyze /path/to/project \
    --email user@example.com \
    --password pass123 \
    --project-id proj123 \
    -p all
```

### Run Application Parser Only and View Results
```bash
python cli.py analyze /path/to/project \
    --email user@example.com \
    --password pass123 \
    --project-id proj123 \
    -p application \
    --view
```

### Disable Auto-Upload and Run Kubernetes Parser
```bash
python cli.py analyze /path/to/project \
    --email user@example.com \
    --password pass123 \
    --project-id proj123 \
    -p kubernetes \
    --no-auto-upload
```

---

## Output
- Parsed results will be displayed in the console if the `--view` flag is enabled.
- If `--auto-upload` is enabled, the results will be uploaded to KloudFarm, and a link to the visualization will be provided.

---

## Notes
- Ensure you have a valid KloudFarm account and a project ID before using the CLI.
- For troubleshooting, refer to the error messages displayed in the console.
- Results are temporarily saved in `temp.json` during processing and are deleted afterward.

---

## Troubleshooting
- **Authentication Error**: Verify email and password credentials.  
- **Invalid Project ID**: Ensure the provided project ID is correct and accessible.  
- **Parser Errors**: Check the console for specific error messages during parsing.