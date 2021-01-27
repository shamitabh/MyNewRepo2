import random
import string


def random_string_generator(size=6, chars=string.ascii_lowercase+string.digits+string.ascii_uppercase+string.punctuation[26]):
    """generate a unique code of a given length using string library"""
    return ''.join(random.choice(chars) for _ in range(size))


def unique_shortcode_generator(instance, new_code=None):
    """return a unique shortcode for an instance"""
    if new_code is not None:
        shortcode = new_code
    else:
        shortcode = random_string_generator(size=6)

    Klass = instance.__class__
    qs_exists = Klass.objects.filter(shortcode=shortcode).exists()
    if qs_exists:
        new_code = random_string_generator(size=6)
        # this makes the function recursive till a unique slug is generated.
        return unique_shortcode_generator(instance, new_code=new_code)
    return shortcode
