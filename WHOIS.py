import whois


def WHOIS(**kwargs):
    website = input("website URL: ")
    res = whois.whois(website)
    print(res)
