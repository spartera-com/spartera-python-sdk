"""
Example usage of Spartera API Python SDK

This example demonstrates how to:
1. Configure authentication with X-API-Key
2. Make basic API calls to get company and asset information
3. Handle errors properly
"""

import os
from spartera_api_sdk import ApiClient, Configuration
from spartera_api_sdk.api import companies_api, assets_api, users_api
from spartera_api_sdk.exceptions import ApiException

def main():
    # Configure the client
    configuration = Configuration()
    configuration.host = os.getenv('SPARTERA_API_BASE_URL', 'https://api.spartera.com')
    
    # IMPORTANT: Spartera uses X-API-Key header authentication
    api_key = os.getenv('SPARTERA_API_KEY', 'your-api-key-here')
    configuration.api_key = {'X-API-Key': api_key}
    
    # Create API client
    api_client = ApiClient(configuration)
    
    # Create API instances
    companies_instance = companies_api.CompaniesApi(api_client)
    assets_instance = assets_api.AssetsApi(api_client)
    users_instance = users_api.UsersApi(api_client)
    
    # Get company ID from environment or use placeholder
    company_id = os.getenv('SPARTERA_COMPANY_ID', 'your-company-id')
    
    try:
        print("🏢 Getting company details...")
        company_details = companies_instance.companies_company_id_get(company_id)
        print(f"   Company: {getattr(company_details, 'company_name', 'N/A')}")
        
        print("\n📊 Getting assets...")
        assets_response = assets_instance.companies_company_id_assets_get(company_id)
        assets_data = getattr(assets_response, 'data', [])
        print(f"   Found {len(assets_data)} assets")
        
        # Show first few assets
        for i, asset in enumerate(assets_data[:3]):
            asset_name = getattr(asset, 'name', f'Asset {i+1}')
            asset_type = getattr(asset, 'asset_type', 'Unknown')
            print(f"   - {asset_name} ({asset_type})")
        
        if assets_data:
            print(f"\n🔍 Getting details for first asset...")
            first_asset = assets_data[0]
            asset_id = getattr(first_asset, 'asset_id', None)
            
            if asset_id:
                asset_detail = assets_instance.companies_company_id_assets_asset_id_get(
                    company_id, asset_id
                )
                print(f"   Asset: {getattr(asset_detail, 'name', 'N/A')}")
                print(f"   Description: {getattr(asset_detail, 'description', 'N/A')}")
        
        print("\n👥 Getting users...")
        users_response = users_instance.companies_company_id_users_get(company_id)
        users_data = getattr(users_response, 'data', [])
        print(f"   Found {len(users_data)} users")
        
        print("\n✅ SDK test completed successfully!")
        
    except ApiException as e:
        print(f"\n❌ API Error: {e}")
        print(f"   Status: {e.status}")
        print(f"   Reason: {e.reason}")
        
        print("\n🔧 Troubleshooting:")
        if e.status == 401:
            print("   - Check your API key")
            print("   - Ensure API key is active")
        elif e.status == 403:
            print("   - Check your permissions")
            print("   - Verify company access")
        elif e.status == 404:
            print("   - Check your company ID")
            print("   - Verify the resource exists")
        else:
            print("   - Check API endpoint URL")
            print("   - Verify request parameters")
            
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        print("\n🔧 Troubleshooting:")
        print("   - Check your internet connection")
        print("   - Verify API base URL")
        print("   - Ensure all dependencies are installed")

if __name__ == "__main__":
    print("🚀 Spartera API Python SDK Example")
    print("=" * 40)
    
    # Check environment variables
    if os.getenv('SPARTERA_API_KEY') in [None, 'your-api-key-here']:
        print("⚠️  Set SPARTERA_API_KEY environment variable with your actual API key")
    if os.getenv('SPARTERA_COMPANY_ID') in [None, 'your-company-id']:
        print("⚠️  Set SPARTERA_COMPANY_ID environment variable with your company ID")
    
    print()
    main()
