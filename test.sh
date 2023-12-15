docker run --rm -it \
    --shm-size=8G \
    -v "$(pwd)"/reports:/app/reports \
    -v "$(pwd)"/tests:/app/tests \
    bqat-stateless \
    "python3 -m pytest tests -v --junitxml=reports/junit/junit.xml --html=reports/junit/report.html --self-contained-html && genbadge tests -o reports/junit/tests-badge.svg && touch config.py config-3.py && coverage run -m pytest tests -v && coverage xml -o reports/coverage/coverage.xml && coverage html -d reports/coverage/ && genbadge coverage -o reports/coverage/coverage-badge.svg"
