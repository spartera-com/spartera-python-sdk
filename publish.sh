#!/bin/bash
# =============================================================================
# Python SDK Publisher for PyPI
# =============================================================================
# 
# PREREQUISITES:
# 1. Install twine: pip install twine
# 2. Create PyPI account: https://pypi.org/account/register/
# 3. Get API token: https://pypi.org/manage/account/token/
# 4. Configure credentials:
#    - Option A: ~/.pypirc file
#    - Option B: Environment variables (TWINE_USERNAME=__token__, TWINE_PASSWORD=your-token)
#
# FOR TESTING: Use TestPyPI first
# 1. Create TestPyPI account: https://test.pypi.org/account/register/
# 2. Upload to test: twine upload --repository testpypi dist/*
# 3. Test install: pip install --index-url https://test.pypi.org/simple/ spartera-api-sdk
# =============================================================================

set -e  # Exit on any error

echo "🐍 Publishing Python SDK to PyPI..."

# Check if we're in the right directory
if [ ! -f "setup.py" ]; then
    echo "❌ setup.py not found. Are you in the SDK directory?"
    exit 1
fi

# Clean previous builds
echo "🧹 Cleaning previous builds..."
rm -rf build/ dist/ *.egg-info/

# Install/upgrade publishing tools
echo "📦 Installing publishing tools..."
pip install --upgrade pip setuptools wheel twine

# Install package dependencies
echo "📚 Installing dependencies..."
if [ -f "requirements.txt" ]; then
    pip install -r requirements.txt
fi

# Build package
echo "🔨 Building package..."
python setup.py sdist bdist_wheel

# Check the package
echo "🔍 Checking package..."
twine check dist/*

if [ $? -ne 0 ]; then
    echo "❌ Package check failed"
    exit 1
fi

# Show what we built
echo "📋 Built packages:"
ls -la dist/

# Ask for publishing confirmation
echo ""
read -p "🚀 Upload to PyPI? (y/N): " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo "📡 Uploading to PyPI..."
    twine upload dist/*
    
    if [ $? -eq 0 ]; then
        echo "✅ Python SDK published successfully!"
        echo "📦 Install with: pip install spartera-api-sdk"
        echo "🔗 View at: https://pypi.org/project/spartera-api-sdk/"
    else
        echo "❌ Upload failed"
        exit 1
    fi
else
    echo "❌ Upload cancelled"
    echo ""
    echo "💡 To test on TestPyPI first:"
    echo "   twine upload --repository testpypi dist/*"
    echo "   pip install --index-url https://test.pypi.org/simple/ spartera-api-sdk"
fi
