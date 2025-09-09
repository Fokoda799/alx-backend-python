def retry_on_failure(retries=3, delay=2):
    def decorator(func):   # this is the actual decorator
        def wrapper(*args, **kwargs):
            print(f"{retries} - {delay}")
            func(*args, **kwargs)
        return wrapper
    return decorator   # outer function returns the real decorator


@retry_on_failure(5, 1)
def test():
    print("Test function")
    return 8

print(test())
