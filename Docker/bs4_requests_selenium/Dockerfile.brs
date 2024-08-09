FROM python:3-alpine
WORKDIR /bs4_requests_selenium
COPY . /bs4_requests_selenium

RUN pip install beautifulsoup4==4.12.3 && \
    pip install requests==2.31.0 && \
    pip install selenium==4.21.0

CMD ["python", "current_version_checker.py"]