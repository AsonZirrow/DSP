

import pytest
import time
import os


def run_tests():
    print("\n" + "=" * 60)
    print("🧪 FILE ANALYZER V3 - TEST SUITE")
    print("=" * 60)

    start_time = time.time()

    print("\n📦 Running pytest suite...\n")

    # Run pytest programmatically
    exit_code = pytest.main([
        "tests",
        "-v"
    ])

    end_time = time.time()

    print("\n" + "=" * 60)
    print("📊 TEST SUMMARY")
    print("=" * 60)

    print(f"Exit Code      : {exit_code}")
    print(f"Duration       : {round(end_time - start_time, 3)} seconds")

    if exit_code == 0:
        print("Status         : ✅ ALL TESTS PASSED")
    else:
        print("Status         : ❌ SOME TESTS FAILED")

    print("=" * 60 + "\n")


if __name__ == "__main__":
    run_tests()