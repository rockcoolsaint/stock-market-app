import sqlite3
import alpaca_trade_api as tradeapi

# Connect to database
connection = sqlite3.connect('app.db')
cursor = connection.cursor()

# API credentials (move these to environment variables for security)
API_KEY = 'PKJRMFCYWYBVZBT49PRR'
SECRET_KEY = '0QHeDMtPJYkXzb7b6RsDvif2WVHEbffzLVIewp7f'

# Create API connection - try different base_url formats
try:
    # Option 1: Use the correct paper trading URL
    api = tradeapi.REST(API_KEY, SECRET_KEY, base_url='https://paper-api.alpaca.markets')
    
    # Test the connection first
    account = api.get_account()
    print("Connection successful!")
    print(f"Account status: {account.status}")
    
    # Get assets
    assets = api.list_assets()
    
    # Print first few assets to test
    for asset in assets:  # Only print first 5 for testing
        # print(f"Symbol: {asset.symbol}, Name: {asset.name}, Exchange: {asset.exchange}")
        if asset.status == 'active' and asset.tradable:
            cursor.execute("INSERT INTO stock (symbol, company) VALUES (?, ?)", (asset.symbol, asset.name))
    
    print(f"Total assets found: {len(assets)}")
    
    connection.commit()
    
except Exception as e:
    print(f"Error: {e}")
    
    # Try alternative connection method
    try:
        print("Trying alternative connection...")
        api = tradeapi.REST(API_KEY, SECRET_KEY, api_version='v2')
        account = api.get_account()
        print("Alternative connection successful!")
        assets = api.list_assets()
        print(f"Total assets found: {len(assets)}")
        
    except Exception as e2:
        print(f"Alternative connection also failed: {e2}")

finally:
    connection.close()