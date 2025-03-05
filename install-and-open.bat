@ECHO OFF
IF NOT EXIST ".venv" (
    ECHO - Virtual environment created in %CD%\.venv
    python -m venv .venv
    CALL :ActivateEnvironment
) ELSE (
    ECHO - Virtual environment already exists
    CALL :ActivateEnvironment
)

CMD /K
GOTO :EOF

:ActivateEnvironment
    ECHO.
    ECHO - Example: python main.py - runs the main.py file.
    ECHO ----- Running in: %CD%\.venv -----
    ECHO.
    ECHO.
    CALL .venv\Scripts\activate.bat
    EXIT /B