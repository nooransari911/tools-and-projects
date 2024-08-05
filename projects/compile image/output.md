## Run on render.com
==> Uploading build...
info==> Build uploaded in 8s
info==> Build successful 🎉
info==> Deploying...
info==> Using Node version 20.15.1 (default)
info==> Docs on specifying a Node version: https://render.com/docs/node-version
info==> Using Bun version 1.1.0 (default)
info==> Docs on specifying a bun version: https://render.com/docs/bun-version
info==> Running 'gunicorn compile_image:app'
info==> No open ports detected, continuing to scan...
info==> Docs on specifying a port: https://render.com/docs/web-services#port-binding
infoDownloading stackoverflow-dev-survey-2024-technology-admired-and-desired-webframe-desire-admire-social.png 100%.
infoDownloading stackoverflow-dev-survey-2024-technology-admired-and-desired-platform-desire-admire-social.png 100%.
infoDownloading stackoverflow-dev-survey-2024-technology-admired-and-desired-database-desire-admire-social.png 100%.
infoDownloading stackoverflow-dev-survey-2024-technology-admired-and-desired-language-desire-admire-social.png 100%.
infoDownloading index_im.html 100%.
infoDownloading results_im.html 100%.
info[2024-08-05 11:40:41 +0000] [93] [INFO] Starting gunicorn 22.0.0
info[2024-08-05 11:40:41 +0000] [93] [INFO] Listening at: http://0.0.0.0:10000 (93)
info[2024-08-05 11:40:41 +0000] [93] [INFO] Using worker: sync
info[2024-08-05 11:40:41 +0000] [108] [INFO] Booting worker with pid: 108
info127.0.0.1 - - [05/Aug/2024:11:40:41 +0000] "HEAD / HTTP/1.1" 404 0 "-" "Go-http-client/1.1"
info==> Your service is live 🎉
info127.0.0.1 - - [05/Aug/2024:11:40:44 +0000] "GET / HTTP/1.1" 404 207 "-" "Go-http-client/2.0"
info['/static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-database-desire-admire-social.png', '/static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-language-desire-admire-social.png', '/static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-platform-desire-admire-social.png', '/static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-webframe-desire-admire-social.png']
info127.0.0.1 - - [05/Aug/2024:11:40:57 +0000] "GET /comm HTTP/1.1" 200 3610 "-" "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
info127.0.0.1 - - [05/Aug/2024:11:40:57 +0000] "GET /static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-language-desire-admire-social.png HTTP/1.1" 200 0 "https://tools-and-projects.onrender.com/comm" "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
info127.0.0.1 - - [05/Aug/2024:11:40:57 +0000] "GET /static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-database-desire-admire-social.png HTTP/1.1" 200 0 "https://tools-and-projects.onrender.com/comm" "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
info127.0.0.1 - - [05/Aug/2024:11:40:57 +0000] "GET /static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-platform-desire-admire-social.png HTTP/1.1" 200 0 "https://tools-and-projects.onrender.com/comm" "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"
info127.0.0.1 - - [05/Aug/2024:11:40:57 +0000] "GET /static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-webframe-desire-admire-social.png HTTP/1.1" 200 0 "https://tools-and-projects.onrender.com/comm" "Mozilla/5.0 (X11; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0"



## ~/Downloads/tools and projects/projects/compile image git:(master)±1 python3 ./compile_image.py
 * Serving Flask app 'compile_image' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Running on http://127.0.0.1:8156/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 648-332-664
['/static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-database-desire-admire-social.png', '/static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-language-desire-admire-social.png', '/static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-platform-desire-admire-social.png', '/static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-webframe-desire-admire-social.png']
127.0.0.1 - - [05/Aug/2024 14:57:58] "GET /comm HTTP/1.1" 200 -
127.0.0.1 - - [05/Aug/2024 14:57:58] "GET /static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-platform-desire-admire-social.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Aug/2024 14:57:58] "GET /static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-webframe-desire-admire-social.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Aug/2024 14:57:58] "GET /static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-language-desire-admire-social.png HTTP/1.1" 304 -
127.0.0.1 - - [05/Aug/2024 14:57:58] "GET /static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-database-desire-admire-social.png HTTP/1.1" 304 -
['/static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-database-desire-admire-social.png', '/static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-language-desire-admire-social.png', '/static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-platform-desire-admire-social.png', '/static/image/stackoverflow-dev-survey-2024-technology-admired-and-desired-webframe-desire-admire-social.png']
127.0.0.1 - - [05/Aug/2024 14:59:04] "POST /comm HTTP/1.1" 200 -
127.0.0.1 - - [05/Aug/2024 14:59:17] "GET /static/generated_file.docx HTTP/1.1" 200 -
