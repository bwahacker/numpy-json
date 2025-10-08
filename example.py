"""
Example usage of numpy-json encoder

Copyright (c) 2025 Featrix, Inc.
"""

import json
import numpy as np
from datetime import datetime
from uuid import uuid4
from pathlib import Path
from numpy_json import NumpyJSONEncoder, sanitize_nans


def basic_example():
    """Basic usage with NumPy arrays"""
    print("=" * 60)
    print("Basic Example")
    print("=" * 60)
    
    data = {
        "array": np.array([1, 2, 3, 4, 5]),
        "matrix": np.array([[1, 2], [3, 4]]),
        "scalar": np.float64(3.14159),
        "date": np.datetime64('2025-01-15'),
    }
    
    json_str = json.dumps(data, cls=NumpyJSONEncoder, indent=2)
    print(json_str)
    print()


def complex_example():
    """Complex data types example"""
    print("=" * 60)
    print("Complex Data Types Example")
    print("=" * 60)
    
    complex_data = {
        "id": uuid4(),
        "timestamp": datetime.now(),
        "measurements": np.array([1.5, 2.3, 3.7, 4.1]),
        "metadata": {
            "path": Path("/tmp/data.csv"),
            "tags": {"ml", "experiment", "2025"},
            "coordinates": (40.7128, -74.0060),
        },
        "config": {
            "enabled": np.bool_(True),
            "threshold": np.float32(0.85),
            "max_items": np.int64(1000),
        }
    }
    
    json_str = json.dumps(complex_data, cls=NumpyJSONEncoder, indent=2)
    print(json_str)
    print()


def nan_handling_example():
    """Handling NaN and Infinity values"""
    print("=" * 60)
    print("NaN/Infinity Handling Example")
    print("=" * 60)
    
    data = {
        "valid": np.array([1.0, 2.0, 3.0]),
        "invalid": np.array([1.0, np.nan, np.inf, -np.inf]),
    }
    
    print("Before sanitization:")
    print(json.dumps(data, cls=NumpyJSONEncoder, indent=2))
    print()
    
    print("After sanitization:")
    clean_data = sanitize_nans(data)
    json_str = json.dumps(clean_data, cls=NumpyJSONEncoder, indent=2, allow_nan=False)
    print(json_str)
    print()


if __name__ == "__main__":
    basic_example()
    complex_example()
    nan_handling_example()

