FROM ayiinxd/ayiin-userbot:buster
#AyiinXd
RUN git clone -b AyiinUbot https://github.com/AyiinXd/AyiinUbot /home/ayiinubot/ \
    && chmod 777 /home/ayiinubot \
    && mkdir /home/ayiinubot/bin/

COPY ./sample_config.env ./config.env* /home/ayiinubot/

WORKDIR /home/ayiinubot/

CMD ["bash","start"]
