bind = ':8080'
threads = 1
workers = 1
timeout = 600
log_level = 'debug'

debug = True
reload = True

# Logging
accesslog = '-'
errorlog = '-'


def post_fork(server, worker):

    import ptvsd
    ptvsd.enable_attach(address=('0.0.0.0', 3000))
    # ptvsd.wait_for_attach()
    return True
