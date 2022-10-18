import psutil

def memory_usage(message: str = 'debug'):
    # current process RAM usage
    p = psutil.Process()
    rss = p.memory_info().rss / 2 ** 20 # Bytes to MB
    mem =  psutil.virtual_memory()
    total = mem.total/1024**2
    avail =  mem.available/1024**2
    print(f"[{message}] python memory usage: {rss: 10.5f} MB - {total: 10.1f} MB : {avail: 10.1f} MB")
