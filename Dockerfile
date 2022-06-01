FROM gbimsath/logo-maker-bot:main

WORKDIR /app

COPY requirements.txt /app/

RUN pip3 install -r requirements.txt

COPY . /app

#set a default command

CMD python3 __main__.py
