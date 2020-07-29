import urllib

def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=10,
                           requestsPerConnection=100,
                           pipeline=True
                           )

    for word in open('Content-Bruteforcing-Wordlist/burp-wordlist.txt'):
        engine.queue(target.req, urllib.quote(word.rstrip()))


def handleResponse(req, interesting):
    # currently available attributes are req.status, req.wordcount, req.length and req.response
    if req.status != 400 and req.status != 404:
        table.add(req)