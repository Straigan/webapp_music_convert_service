FROM python:3
ENV PYTHONUNBUFFERED=1
ENV FLASK_APP=webapp
ENV FLASK_RUN_HOST=0.0.0.0
WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
ENV TZ=Asia/Yekaterinburg
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
EXPOSE 50000
COPY . .
CMD ["flask" "run_web"]
