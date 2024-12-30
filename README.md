# KloudFarm Parser

A desktop application for parsing and generating diagrams from code. This application provides both a GUI interface and CLI capabilities for processing code and generating visual outputs.

## Features

- User authentication with session management
- Project selection and management
- Code parsing and diagram generation
- Dual interface: GUI and CLI
- Automated token refresh
- Secure credential storage

## Prerequisites

- Python 3.11
- Miniconda/Anaconda

## Installation

1. Install Miniconda (if not already installed):
   ```bash
   # macOS
   brew install --cask miniconda
   
   # Windows
   # Download and install from: https://docs.conda.io/en/latest/miniconda.html
   ```

2. Create and activate a new conda environment:
   ```bash
   conda create -n kloudfarm python=3.11 tk
   conda activate kloudfarm
   ```

3. Clone the repository:
   ```bash
   git clone git@github.com:Kloudfarm-io/kfclient.git
   cd kfclient
   ```

4. Install required packages:
   ```bash
   pip install requests jwt
   ```

## Project Structure

```
kfclient/
├── main.py                 # Application entry point
├── gui_app/
│   ├── __init__.py
│   ├── login_window.py     # Login GUI implementation
│   ├── project_window.py   # Project selection window
│   ├── main_window.py      # Main application window
│   ├── cli_interface.py    # CLI implementation
│   └── config.py          # Configuration settings
└── README.md
```

## Usage

### GUI Mode

Run the application in GUI mode:
```bash
python main.py
```

The application will:
1. Launch a login window
2. Check for existing sessions
3. Navigate to project selection or main window based on authentication status

### CLI Mode

Run the application in CLI mode by providing arguments:
```bash
python main.py --help  # Show CLI options
python main.py parse <filename>  # Parse a specific file
```

## Authentication

The application uses token-based authentication:
- Access tokens for API requests
- Refresh tokens for session maintenance
- Secure local storage of credentials
- Automatic token refresh when expired

## Configuration

Configuration settings can be found in `gui_app/config.py`:
- API endpoints
- File paths
- Authentication settings

## Development

To set up the development environment:

1. Create a development conda environment:
   ```bash
   conda create -n kloudfarm-dev python=3.11 tk
   conda activate kloudfarm-dev
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt  # If available
   ```

## Troubleshooting

### Common Issues

1. Tkinter Issues
   ```bash
   # If Tkinter is missing, ensure it's installed in conda
   conda install tk
   ```

2. Authentication Errors
   - Check your internet connection
   - Verify API endpoints in config
   - Ensure credentials are correct

3. Parser Errors
   - Verify input code format
   - Check file permissions
   - Ensure output directory exists

### CLI Tool Usage
General Command Format
python cli.py <command> [OPTIONS]
Available Commands
1. Analyze
Analyze a project directory and generate architecture diagrams.

python cli.py analyze PATH --email <EMAIL> --password <PASSWORD> --project-id <PROJECT_ID> [OPTIONS]
Options
PATH (required): Path to the project directory to analyze.
--email (required): Email address for authentication.
--password (required): Password for authentication.
--project-id (required): The project ID to associate the analysis with.
--parser (optional):
Specify the parsers to use.
Possible values: all, application, kubernetes.
Default: all.
Multiple parsers can be specified with -p <parser_name>.
--auto-upload/--no-auto-upload (optional):
Automatically upload results after parsing.
Default: --auto-upload.
--view/--no-view (optional):
Display parsed results in the CLI.
Default: --no-view.




## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

[Your License Here]

## Contact

For support or queries:
- Email: support@kloudfarm.io
- Website: https://www.kloudfarm.io