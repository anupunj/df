import sys
import os
import logging
from pathlib import Path

def get_log_directory():
    """Get platform-specific log directory"""
    if sys.platform.startswith('darwin'):  # macOS
        return os.path.join(str(Path.home()), 'Library', 'Logs', 'KloudfarmClient')
    elif sys.platform.startswith('win'):  # Windows
        return os.path.join(os.getenv('APPDATA'), 'KloudfarmClient', 'logs')
    else:  # Linux and others
        return os.path.join(str(Path.home()), '.kloudfarm', 'logs')

def setup_logging():
    """Set up logging configuration"""
    # Create platform-specific log directory
    log_dir = get_log_directory()
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, 'kloudfarm.log')
    
    # Configure logging
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )
    
    logger = logging.getLogger('KloudfarmClient')
    logger.info('=== Application Starting ===')
    logger.info(f'Platform: {sys.platform}')
    logger.info(f'Python Version: {sys.version}')
    
    return logger

if __name__ == "__main__":
    logger = setup_logging()
    
    try:
        if len(sys.argv) > 1:
            # CLI mode
            logger.info('Starting CLI interface')
            from gui_app.cli_interface import cli_interface
            cli_interface()
        else:
            # GUI mode
            logger.info('Starting GUI interface')
            from gui_app.login_window import ModernLoginWindow
            login_window = ModernLoginWindow()
            login_window.root.mainloop()
    except Exception as e:
        logger.exception('Unexpected error in main application:')
        raise