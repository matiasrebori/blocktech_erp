@echo off
echo ==============================
echo Iniciando Blocktech ERP...
echo ==============================

REM Ir al directorio donde está el .bat (raíz del proyecto)
cd /d "%~dp0"

REM Activar entorno virtual
call venv\Scripts\activate

REM Aplicar migraciones
python manage.py migrate

REM Abrir navegador
start http://127.0.0.1:8000/dashboard/

REM Levantar servidor
python manage.py runserver

pause