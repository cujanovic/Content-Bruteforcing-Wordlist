# Content Bruteforcing Wordlist
  
#### Wordlist for content(directory) bruteforce discovering with Burp or dirsearch

- burp-wordlist.txt - size: 51868500 - sha256sum: e22db98135b9165cf5c7b8325bb57dd1f042603fc70508a81cd947299d182b4d

`wget https://localdomain.pw/Content-Bruteforcing-Wordlist/burp-wordlist.txt`
- dirsearch-wordlist.txt - size: 128932911 - sha256sum: bd4004a295b8bb3fa3aed8fec5c197321a571e55ea0333513ffe4635e4143ade

`wget https://localdomain.pw/Content-Bruteforcing-Wordlist/dirsearch-wordlist.txt`

Usage example:

`python3 dirsearch.py -u https://example.com -e "php" -w ../Content-Bruteforcing-Wordlist/dirsearch-wordlist.txt`
