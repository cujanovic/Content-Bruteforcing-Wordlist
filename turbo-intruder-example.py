import urllib

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=10,
                           requestsPerConnection=100,
                           pipeline=True
                           )

    for i in range(3, 8):
        engine.queue(target.req, randstr(i), learn=1)
        engine.queue(target.req, target.baseInput, learn=2)

    for word in open('Content-Bruteforcing-Wordlist/burp-wordlist.txt'):
        engine.queue(target.req, urllib.quote(word.rstrip()))


def handleResponse(req, interesting):
    if interesting:
        table.add(req)