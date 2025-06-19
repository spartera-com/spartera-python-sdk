# Python SDK Documentation

## Overview
The Python SDK for Spartera API provides a convenient way to interact with the Spartera platform from Python applications.

**Install:** `pip install spartera-api-sdk`

## Requirements
- Python 3.8 or higher
- pip package manager

## Quick Start

```python
from spartera_api_sdk import ApiClient, Configuration
from spartera_api_sdk.api import companies_api, assets_api

# Configure client
config = Configuration()
config.host = "https://api.spartera.com"
config.api_key = {'X-API-Key': 'your-api-key-here'}

# Create API client
client = ApiClient(config)
companies_instance = companies_api.CompaniesApi(client)

# Make API call
company = companies_instance.companies_company_id_get('your-company-id')
print(f"Company: {company.company_name}")
```

## Environment Variables

```bash
export SPARTERA_API_KEY="your-api-key"
export SPARTERA_COMPANY_ID="your-company-id"
export SPARTERA_API_BASE_URL="https://api.spartera.com"
```

## Error Handling

```python
from spartera_api_sdk.exceptions import ApiException

try:
    company = companies_instance.companies_company_id_get(company_id)
except ApiException as e:
    print(f"API Error: {e}")
    print(f"Status: {e.status}")
    print(f"Reason: {e.reason}")
```

## Package Manager
- **Platform**: PyPI
- **Install**: `pip install spartera-api-sdk`
- **Import**: `from spartera_api_sdk import ApiClient`

## Publishing
1. Build: `python setup.py sdist bdist_wheel`
2. Upload: `twine upload dist/*`
3. Install: `pip install spartera-api-sdk`
