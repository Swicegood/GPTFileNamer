import hashlib
import time

def cache_md5sum(file_path, filename, cache_file='cache.txt'):
    """
    This function takes a file path, computes the MD5 checksum,
    and appends the checksum to a cache file.
    """
    # Compute MD5 checksum
    hash_md5 = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    md5sum = hash_md5.hexdigest()
    
    # Cache the MD5 checksum
    with open(cache_file, 'a') as cache:
        cache.write(f"{md5sum}: {filename}\n")

    return md5sum

def get_md5sum(filepath):
    """
    This function takes a file path and returns the MD5 checksum.
    """
    hash_md5 = hashlib.md5()
    try:
    # Your file processing code here
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)
    except OSError as e:
        if e.errno == 11:
            print("Resource deadlock avoided, trying again")
            time.sleep(5)
            get_md5sum(filepath)
    
    return hash_md5.hexdigest()
      
def get_cached_filename(md5sum, cache_file='cache.txt'):
    """
    This function takes the MD5 checksum and searches the cache file
    for the corresponding filename.
    """
    time.sleep(5)
    with open(cache_file, 'r') as cache:
        for line in cache:
            if md5sum in line:
                return line.split(':')[1].strip()