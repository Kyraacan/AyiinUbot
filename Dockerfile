FROM ayiinxd/ayiin-userbot:buster
#AyiinXd
RUN git clone -b AyiinUbot https://github.com/AyiinXd/AyiinUbot /home/ayiinuserbot/ \
    && chmod 777 /home/ayiinuserbot \
    && mkdir /home/ayiinuserbot/bin/

COPY ./sample_config.env ./config.env* /home/ayiinuserbot/

WORKDIR /home/ayiinuserbot/

CMD ["bash","start"]
