"""
Load and display Seed Equation analysis results
"""
import numpy as np

def load_findings(filepath='data/findings_complete.npz'):
    """Load complete findings from analysis"""
    data = np.load(filepath, allow_pickle=True)
    return {key: data[key] for key in data.files}

def print_summary():
    """Print key statistics"""
    findings = load_findings()
    
    print("=" * 50)
    print("THE SEED EQUATION - Key Results")
    print("=" * 50)
    print(f"φ (golden ratio) = 1.618")
    print(f"")
    print(f"REST α/θ:  Mean alpha/theta ratio during rest")
    print(f"TASK α/θ:  Mean alpha/theta ratio during task")
    print(f"")
    print(f"Available data keys: {list(findings.keys())}")
    print("=" * 50)

if __name__ == "__main__":
    print_summary()
