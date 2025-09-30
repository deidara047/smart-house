@echo off
echo Starting backend...
start cmd /k "cd backend && py app.py"

echo Starting frontend...
start cmd /k "cd frontend && npm run dev -- --host"

echo Opening browser...
start http://localhost:3000

pause