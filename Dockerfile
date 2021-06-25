FROM python:3.9.0

WORKDIR /home/

RUN echo "testing"

RUN git clone https://github.com/songjungboss95/pragmatics_2.git

WORKDIR /home/pragmatics_2/

RUN python -m pip install --upgrade pip

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

RUN echo "SECRET_KEY= kl*o*f6qo_apc8$qyd2*5h9-&(v#+*bz+9a%kz2=0a@%b#ip)v" > .env

RUN python manage.py collectstatic

EXPOSE 8000

CMD ["bash", "-c","python manage.py migrate --settings=pragmatics_2.settings.deploy && gunicorn pragmatics_2.wsgi --env DJANGO_SETTINGS_MODULE=pragmatics_2.settings.deploy  --bind 0.0.0.0:8000"]