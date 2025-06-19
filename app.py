from flask import Flask, jsonify
import os
import socket
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    """Main homepage - shows app info"""
    return jsonify({
        'message': 'Welcome to Trey\'s DevOps Learning Lab!',
        'app': 'Flask Demo Application',
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'hostname': socket.gethostname(),
        'timestamp': datetime.now().isoformat()
    })

@app.route('/health')
def health():
    """Health check endpoint - important for Kubernetes"""
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/ready')
def ready():
    """Readiness probe - tells Kubernetes when app is ready"""
    return jsonify({
        'status': 'ready',
        'message': 'Application is ready to serve traffic'
    })

@app.route('/info')
def info():
    """App information - useful for debugging deployments"""
    return jsonify({
        'app_name': 'flask-demo-app',
        'version': os.getenv('APP_VERSION', '1.0.0'),
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'python_version': os.sys.version,
        'hostname': socket.gethostname()
    })

if __name__ == '__main__':
    # Get port from environment variable (important for containers)
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
