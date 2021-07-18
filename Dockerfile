FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/matt700395/server_test.git

WORKDIR /home/pragmatics_2/

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN echo "SECRET_KEY= kl*o*f6qo_apc8$qyd2*5h9-&(v#+*bz+9a%kz2=0a@%b#ip)v" > .env

RUN pip manage.py migrate


EXPOSE 8000

CMD ["python", "manage.py" , "runserver", "0.0.0.0:8000"]