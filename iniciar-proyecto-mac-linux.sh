#!/bin/bash

echo "Starting backend..."
(cd backend && python app.py &)

echo "Starting frontend..."
(cd frontend && npm run dev -- --host &)

echo "Opening browser..."
open http://localhost:3000

wait