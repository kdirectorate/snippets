def ourip(testip=None,testport=None):
    """Attempts to determine our routable IP to the rest of the world."""
    if not testip: testip = "8.8.8.8"  # Can be anything that has fantastic uptime
    if not testport: testport = 80

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.connect((testip, testport))
        return s.getsockname()[0]
