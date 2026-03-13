"""
Test that all modules import correctly
"""

def test_imports():
    try:
        import src.data_fetcher
        import src.indicators
        import src.display
        print("✅ All imports successful")
        return True
    except Exception as e:
        print(f"❌ Import failed: {e}")
        return False

if __name__ == "__main__":
    test_imports()
