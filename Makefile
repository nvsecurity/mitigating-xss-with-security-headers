setup-env:
	@echo "Setting up Python virtual environment..."
	python3 -m venv venv && source venv/bin/activate
	@echo "Installing dependencies..."
	. venv/bin/activate && pip install -r requirements.txt
	@echo "Setup complete."
run-insecure: setup-env
	@echo "Running insecure Flask app..."
	python3 insecure.py & sleep 2 && \
	open "http://127.0.0.1:5001/?name=<script>alert('XSS')</script>"
run-secure: setup-env
	@echo "Running secure Flask app..."
	python3 secure.py & sleep 2 && \
	open "http://127.0.0.1:5001/?name=<script>alert('XSS')</script>"
