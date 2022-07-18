def sortLineNumbers(data):
    def natural_key(string_):
     try:
        import re
     except ImportError:
        print("Please install the 're' module.")
        return
     return [int(s) if s.isdigit() else s for s in re.split(r'(\d+)', string_) if s]  

    x = sorted(data, key=natural_key)
    return x