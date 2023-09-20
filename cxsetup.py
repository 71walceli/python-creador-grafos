"""
    Código que usa cx_Freeze para generar ejecutables y y sus librerías correspondientes.
"""

import sys

import cx_Freeze as cx

PROGRAMA_EMAIL = 'walter.celi.vaca@uagraria.edu.ec'
PROGRAMA_VERSION = '0.2'
PROGRAMA_DESCRIPCION = "Creador de grafos por medio de matrices de adyacencia"
PROGRAMA_AUTORES = 'Anastacio, Bohórquez, Celi, Freire'
PROGRAMA_NOMBRE = 'creadorGrafos'
PROGRAMA_LOGO = 'logo.ico'

base = None
if sys.platform == "win32":
    base = "Win32GUI"

cx.setup(
    name=PROGRAMA_NOMBRE,               # Datos genrrales del programa
    version=PROGRAMA_VERSION,           #
    author=PROGRAMA_AUTORES,            #
    author_email=PROGRAMA_EMAIL,        #
    description=PROGRAMA_DESCRIPCION,   #
    packages = [],
    executables=[
        cx.Executable(  # Programa principal
            'Main.py',
            target_name=PROGRAMA_NOMBRE,
            base=base,
            icon=PROGRAMA_LOGO
        )
    ],
    options={   # Opciones de compilación
        'build_exe': {  # Opciones del ejecutable
            'packages': ["tkinter", "numpy"],
            'includes': [],
        },
        "bdist_msi": {  # Opciones del instalador
            'data': {
                "Shortcut": [   # Accesos directos creados
                    (
                        "DesktopShortcut",                      # Shortcut
                        "DesktopFolder",                        # Directory_
                        PROGRAMA_NOMBRE,                        # Name
                        "TARGETDIR",                            # Component_
                        f"[TARGETDIR]{PROGRAMA_NOMBRE}.exe",    # Target
                        None,                                   # Arguments
                        PROGRAMA_DESCRIPCION,                   # Description
                        None,                                   # Hotkey
                        None,                                   # Icon
                        None,                                   # IconIndex
                        None,                                   # ShowCmd
                        'TARGETDIR'                             # WkDir
                    ),
                    (
                        "StartMenuShortcut",                    # Shortcut
                        "StartMenuFolder",                      # Directory_
                        PROGRAMA_NOMBRE,                        # Name
                        "TARGETDIR",                            # Component_
                        f"[TARGETDIR]{PROGRAMA_NOMBRE}.exe",    # Target
                        None,                                   # Arguments
                        PROGRAMA_DESCRIPCION,                   # Description
                        None,                                   # Hotkey
                        None,                                   # Icon
                        None,                                   # IconIndex
                        None,                                   # ShowCmd
                        'TARGETDIR'                             # WkDir
                    )
                ]
            }
        }
    }
)
