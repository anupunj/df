import os
import sys
import platform
from pathlib import Path
from PyInstaller.utils.hooks import collect_dynamic_libs, collect_data_files
import rich

# Get the absolute path to the project root directory
PROJ_ROOT = os.path.abspath(os.getcwd())

# Get Rich path
RICH_PATH = os.path.dirname(rich.__file__)

# Get the virtual environment path
if hasattr(sys, 'real_prefix') or (hasattr(sys, 'base_prefix') and sys.base_prefix != sys.prefix):
    VENV_PATH = sys.prefix
else:
    VENV_PATH = os.path.join(PROJ_ROOT, '.venv')

# Base hidden imports for all platforms
base_hidden_imports = [
    'tkinter',
    'tkinter.ttk',
    'rich',
    'rich.logging',
    'rich.console',
    'rich.theme',
    'rich.traceback',
    'rich.syntax',
    'rich.markup',
    'pygments',
    'pygments.lexers',
    'pygments.formatters',
]

# Platform-specific settings
if sys.platform.startswith('win'):
    SEPARATOR = ';'
    TS_LANG_PATH = os.path.join('tree_sitter_languages', 'languages.dll')
    TS_LANG_BINARY = os.path.join(VENV_PATH, 'Lib', 'site-packages', TS_LANG_PATH)
    common_options = {
        'datas': [
            (RICH_PATH, 'rich'),
        ],
        'hiddenimports': base_hidden_imports,
        'binaries': [(TS_LANG_BINARY, 'tree_sitter_languages')],
        'noarchive': False,
    }
    TARGET_ARCH = None

elif sys.platform.startswith('darwin'):
    # macOS specific configuration
    SEPARATOR = ':'
    CONDA_ENV_PATH = "/opt/homebrew/Caskroom/miniconda/base/envs/myenv3"
    TSL_PATH = os.path.join(CONDA_ENV_PATH, "lib/python3.11/site-packages/tree_sitter_languages")
    PYTHON_DYLIB = os.path.join(CONDA_ENV_PATH, 'lib', 'libpython3.11.dylib')

    import tree_sitter
    TREE_SITTER_PATH = os.path.dirname(tree_sitter.__file__)
    BINDING_FILE = '_binding.cpython-311-darwin.so'
    TREE_SITTER_BINDING = os.path.join(TREE_SITTER_PATH, BINDING_FILE)
    LANGUAGES_FILE = os.path.join(TSL_PATH, 'languages.so')
    
    common_options = {
        'datas': [
            (RICH_PATH, 'rich'),
            (TSL_PATH, 'tree_sitter_languages'),
            (TREE_SITTER_PATH, 'tree_sitter'),
        ],
        'binaries': [
            (LANGUAGES_FILE, 'tree_sitter_languages'),
            (TREE_SITTER_BINDING, 'tree_sitter'),
            (PYTHON_DYLIB, '.'),
        ],
        'hiddenimports': base_hidden_imports + [
            'tree_sitter',
            'tree_sitter._binding',
            'tree_sitter_languages',
            'tree_sitter_languages.languages',
        ],
        'noarchive': False,
    }
    
    # Determine macOS architecture
    if platform.machine() == 'arm64':
        TARGET_ARCH = 'arm64'
    else:
        TARGET_ARCH = 'x86_64'

else:  # Linux and other Unix-like systems
    SEPARATOR = ':'
    TS_LANG_PATH = os.path.join('tree_sitter_languages', 'languages.so')
    TS_LANG_BINARY = os.path.join(VENV_PATH, 'lib', 'python*', 'site-packages', TS_LANG_PATH)
    common_options = {
        'datas': [
            (RICH_PATH, 'rich'),
        ],
        'hiddenimports': base_hidden_imports,
        'binaries': [(TS_LANG_BINARY, 'tree_sitter_languages')],
        'noarchive': False,
    }
    TARGET_ARCH = None

if sys.platform.startswith('darwin'):
    CONDA_ENV_PATH = "/opt/homebrew/Caskroom/miniconda/base/envs/myenv3"
    PYTHON_DYLIB = os.path.join(CONDA_ENV_PATH, 'lib', 'libpython3.11.dylib')
    # macOS build
    a = Analysis(
        ['main.py'],
        pathex=[PROJ_ROOT],
        **common_options
    )

    pyz = PYZ(a.pure, a.zipped_data)

    exe = EXE(
        pyz,
        a.scripts,
        [],
        exclude_binaries=True,
        name='Kloudfarm Client',
        debug=True,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=False,  # Keep True for debugging
        argv_emulation=True,
        target_arch=TARGET_ARCH
    )

    # Create an intermediate COLLECT
    coll = COLLECT(
        exe,
        a.binaries,
        a.zipfiles,
        a.datas,
        strip=False,
        upx=True,
        name='Kloudfarm Client'
    )

    app = BUNDLE(
        coll,
        name='Kloudfarm Client.app',
        icon='./icon.icns',
        bundle_identifier='io.kloudfarm.kfclient',
        info_plist={
            'NSHighResolutionCapable': 'True',
            'LSBackgroundOnly': 'False',
            'CFBundleName': 'Kloudfarm Client',
            'CFBundleDisplayName': 'Kloudfarm Client',
            'CFBundleExecutable': 'Kloudfarm Client',
            'CFBundleGetInfoString': "Kloudfarm Client",
            'CFBundleIdentifier': "io.kloudfarm.kfclient",
            'CFBundleVersion': "1.0.0",
            'CFBundleShortVersionString': "1.0.0",
            'CFBundlePackageType': 'APPL',
            'CFBundleSignature': '????',
            'NSRequiresAquaSystemAppearance': 'False',
            'LSMinimumSystemVersion': '10.12.0',
            'LSApplicationCategoryType': 'public.app-category.developer-tools',
            'NSHumanReadableCopyright': '© 2024 KloudFarm',
            'NSPrincipalClass': 'NSApplication',
            'LSEnvironment': {
                'LANG': 'en_US.UTF-8',
                'DYLD_LIBRARY_PATH': '@executable_path/../Resources:@executable_path/../Frameworks',
                'DYLD_FRAMEWORK_PATH': '@executable_path/../Frameworks',
                'PYTHONHOME': '@executable_path/../Resources',
                'PYTHONPATH': '@executable_path/../Resources',
                'PATH': '/usr/bin:/bin:/usr/sbin:/sbin',
                'KLOUDFARM_LOG_DIR': '${HOME}/Library/Logs/KloudfarmClient',
            },
            'NSAppleEventsUsageDescription': 'This app needs to write log files.',
            'LSMultipleInstancesProhibited': True,
        },
    )

else:
    # Windows/Linux build
    gui_a = Analysis(
        ['main.py'],
        pathex=[PROJ_ROOT],
        **common_options
    )

    gui_pyz = PYZ(gui_a.pure, gui_a.zipped_data)

    gui_exe = EXE(
        gui_pyz,
        gui_a.scripts,
        gui_a.binaries,
        gui_a.zipfiles,
        gui_a.datas,
        name='kfclient-gui',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=False,
    )

    cli_a = Analysis(
        ['main.py'],
        pathex=[PROJ_ROOT],
        **common_options
    )

    cli_pyz = PYZ(cli_a.pure, cli_a.zipped_data)

    cli_exe = EXE(
        cli_pyz,
        cli_a.scripts,
        cli_a.binaries,
        cli_a.zipfiles,
        cli_a.datas,
        name='kfclient-cli',
        debug=False,
        bootloader_ignore_signals=False,
        strip=False,
        upx=True,
        console=True,
    )

    COLLECT(
        gui_exe,
        cli_exe,
        strip=False,
        upx=True,
        name='kfclient'
    )