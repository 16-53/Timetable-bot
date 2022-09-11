FROM python:3.10
WORKDIR /timetable-bot-Pascal-Private-English-School-6A
COPY requirements.txt /timetable-bot-Pascal-Private-English-School-6A/
RUN pip install -r requirements.txt
COPY . /timetable-bot-Pascal-Private-English-School-6A
CMD python main.py