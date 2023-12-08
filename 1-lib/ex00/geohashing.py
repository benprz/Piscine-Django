import sys, antigravity

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python geohashing.py [latitude] [longitude] [date]")
        sys.exit(1)
    try:
        antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3].encode('utf-8'))
    except Exception as e:
        print(e)
        sys.exit(1)