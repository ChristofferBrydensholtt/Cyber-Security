import dns.resolver
import sys

DNStypes = ["A", "AAAA", "ALIAS", "CNAME", "MX", "TXT"]
DNSdict = {

    "A:": " ",
    "AAAA:": " ",
    "ALIAS:": " ",
    "CNAME:": " ",
    "MAX:": "",
    "TXT:": ""
}

for x in DNStypes:
    try:
        answer = dns.resolver.resolve(sys.argv[1], x)
        for ip in answer:
            print(x + " result is " + ip.to_text())
            DNSdict[x] = ip.to_text()
    except dns.resolver.NoAnswer:
        print("Could not resolve DNS type: " + x)
        continue
    except dns.rdatatype.UnknownRdatatype:
        print("Unknown datatype")
        continue
    except KeyboardInterrupt:
        print("User interrupted this")
        quit()
    except dns.resolver.NXDOMAIN:
        print("Your domain is wrong, try again")
        quit()
