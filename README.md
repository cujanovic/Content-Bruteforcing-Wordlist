# Content Bruteforcing Wordlist
  
#### Wordlist for content(directory) bruteforce discovering with Burp or dirsearch

- burp-wordlist.txt - size: 40M 

`wget https://localdomain.pw/Content-Bruteforcing-Wordlist/burp-wordlist.txt`
- dirsearch-wordlist.txt - size: 102M

`wget https://localdomain.pw/Content-Bruteforcing-Wordlist/dirsearch-wordlist.txt`

Usage example:

`python3 dirsearch.py -u https://example.com -e "php" -w ../Content-Bruteforcing-Wordlist/dirsearch-wordlist.txt`
