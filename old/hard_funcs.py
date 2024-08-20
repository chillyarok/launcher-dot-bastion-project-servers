import psutil
def get_ram_in_gb():
    ram = psutil.virtual_memory()
    return round(ram.total / (1024.0 ** 3), 2)
def get_ram_in_mb():
    ram = psutil.virtual_memory()
    return round(ram.total / (1024.0 ** 2), 2)