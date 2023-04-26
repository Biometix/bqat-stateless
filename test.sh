docker run --rm -it \
    --shm-size=2G \
    -v "$(pwd)"/reports:/app/reports \
    -v "$(pwd)"/data:/app/data \
    bqat-stateless \
    "python3.8 -m pytest tests -v --junitxml=reports/junit/junit.xml --html=reports/junit/report.html --self-contained-html && genbadge tests -o reports/junit/tests-badge.svg && touch config.py config-3.py && coverage run -m pytest tests -v && coverage xml -o reports/coverage/coverage.xml && coverage html -d reports/coverage/ && genbadge coverage -o reports/coverage/coverage-badge.svg"
