@echo off
echo Starting ResPro AI Server...
python -m uvicorn backend.main:app --port 8088 --host 127.0.0.1
pause
