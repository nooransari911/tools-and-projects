 kill -9 $(lsof -t -i:5000 -sTCP:LISTEN)
python3 ./source/main.py