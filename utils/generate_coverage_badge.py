"""
Generate a static coverage badge for README
"""
import subprocess
import re

def get_coverage_percentage():
    """Run coverage and extract percentage"""
    try:
        # Run coverage
        subprocess.run(
            ["python", "-m", "coverage", "run", "-m", "unittest", "discover", "-s", "tests", "-p", "test_*.py"],
            capture_output=True,
            check=True
        )
        
        # Get report
        result = subprocess.run(
            ["python", "-m", "coverage", "report"],
            capture_output=True,
            text=True,
            check=True
        )
        
        # Extract percentage from TOTAL line
        for line in result.stdout.split('\n'):
            if 'TOTAL' in line:
                match = re.search(r'(\d+)%', line)
                if match:
                    return int(match.group(1))
        
        return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def get_badge_color(percentage):
    """Get badge color based on coverage percentage"""
    if percentage >= 90:
        return "brightgreen"
    elif percentage >= 80:
        return "green"
    elif percentage >= 70:
        return "yellowgreen"
    elif percentage >= 60:
        return "yellow"
    elif percentage >= 50:
        return "orange"
    else:
        return "red"

def generate_badge_markdown(percentage):
    """Generate markdown badge"""
    color = get_badge_color(percentage)
    return f"![Coverage](https://img.shields.io/badge/coverage-{percentage}%25-{color})"

if __name__ == "__main__":
    print("Running tests and calculating coverage...")
    percentage = get_coverage_percentage()
    
    if percentage is not None:
        badge = generate_badge_markdown(percentage)
        print(f"\nCoverage: {percentage}%")
        print(f"\nBadge markdown:")
        print(badge)
        print(f"\nCopy this to your README.md to update the coverage badge")
    else:
        print("Failed to calculate coverage")
