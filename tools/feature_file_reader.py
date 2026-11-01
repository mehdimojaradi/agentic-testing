from pathlib import Path
# Import the appropriate tool decorator or function from the Microsoft Agent Framework you are using

async def read_feature_file(feature_name: str) -> str:
    """Reads a BDD Gherkin .feature specification file from the features directory.
    
    Args:
        feature_name: The name of the feature file (e.g., 'api_auth.feature' or just 'api_auth').
    """
    if not feature_name.endswith(".feature"):
        feature_name += ".feature"
        
    # Resolve relative to your project root structure
    file_path = Path("features") / feature_name
    
    if not file_path.exists():
        return f"Error: Feature file '{feature_name}' not found in features/ directory."
        
    try:
        return file_path.read_text(encoding="utf-8")
    except Exception as e:
        return f"Error reading file: {str(e)}"