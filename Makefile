PYTHONPATH := .

.PHONY: run test lint format freeze clean

run:
	uvicorn src.main:app --reload --host 127.0.0.1 --port 8000

test:
	PYTHONPATH=. pytest -q

lint:
	ruff check src tests

format:
	black src tests

freeze:
	pip freeze > requirements.lock.txt

clean:
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +; \
	rm -rf .pytest_cache .ruff_cache
