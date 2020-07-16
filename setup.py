from cx_Freeze import setup, Executable


setup(
    name = "padding",
    version = "0.1",
    description = "Ce programme alligne correctement les informations de la journalisation",
    executables = [Executable("padding.py")],
)
