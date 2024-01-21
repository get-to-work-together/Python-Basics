
def print_banner(text, star_character = '*'):
    """Print a banner with stars

    @Copywrite Rik 2024"""
    
    n = len(text)
    stars = (n + 6) * star_character
    print(stars)
    print(star_character + '  ' + text.upper() + '  ' + star_character)
    print(stars)


if __name__ == '__main__':
    print_banner('testing')

