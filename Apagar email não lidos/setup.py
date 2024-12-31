from cx_Freeze import setup, Executable

build_exe_options = {
    "packages": ["time"], "includes": ["keyboard", "pyautogui"], "excludes": ["tkinter"]
}

setup(
    name="Apagador_de_email",
    version="1.0",
    description="E um apagador de email n�o lidos, simples",
    options={"build_exe": build_exe_options},
    executables=[Executable("Apagador_email_n�o_lidos.py", base="base")],
)