from bot.client import get_client

def main():
    try:
        client = get_client()

        # Simple request to verify the API is reachable
        response = client.futures_ping()

        print("✅ Connected successfully!")
        print(response)

    except Exception as e:
        print("❌ Connection failed")
        print(e)

if __name__ == "__main__":
    main()
    