#!/bin/bash
# Test script for Python SDK

echo "🧪 Testing Python SDK..."

# Install in development mode
echo "Installing SDK in development mode..."
pip install -e . --quiet

if [ $? -eq 0 ]; then
    echo "✅ SDK installed successfully"
    echo "📝 To test with real API calls:"
    echo "   export SPARTERA_API_KEY='your-api-key'"
    echo "   export SPARTERA_COMPANY_ID='your-company-id'"
    echo "   python example.py"
else
    echo "❌ SDK installation failed"
    exit 1
fi
