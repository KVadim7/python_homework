def stop_words(words: list):
    def inner_func(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for word in words:
                result = result.replace(word, "*")
            return result
        return wrapper
    return inner_func

@stop_words(['pepsi', 'BMW'])
def create_slogan(name="Vadim"):
    return f"{name} drinks pepsi in his brand new BMW"

print(create_slogan())
