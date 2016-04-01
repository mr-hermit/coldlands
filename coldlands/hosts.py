from django_hosts import patterns, host

host_patterns = patterns('',
    host(r'www', 'coldlands.urls', name='main'),
    host(r'blog', 'blog.urls', name='photo'),
)