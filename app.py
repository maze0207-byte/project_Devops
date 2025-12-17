import os
import sys

# Ensure the frontend directory is on sys.path so we can import `front`
ROOT = os.path.dirname(__file__)
FRONT_DIR = os.path.join(ROOT, 'frontend-html')
if FRONT_DIR not in sys.path:
    sys.path.insert(0, FRONT_DIR)

try:
    from front import app
except Exception as e:
    raise RuntimeError(f"Failed to import frontend app: {e}")

if __name__ == '__main__':
    # Run the frontend Flask app
    app.run(debug=True, host='0.0.0.0', port=5001)
