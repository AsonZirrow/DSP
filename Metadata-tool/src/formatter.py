

# report/formatter.py

def print_report(results):
    print("\n" + "=" * 60)
    print(" FILE ANALYSIS REPORT (MODULAR V3) ")
    print("=" * 60)

    section_id = 1

    for section, data in results.items():
        print(f"\n[{section_id}] {section.upper()}")

        if isinstance(data, dict):
            for i, (k, v) in enumerate(data.items(), 1):
                print(f"  {i}. {k}: {v}")
        else:
            print(data)

        section_id += 1