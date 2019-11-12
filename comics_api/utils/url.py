def clean_url(url):
        '''Remove parameters from a URL'''
        return url.split('?')[0] if url else None
