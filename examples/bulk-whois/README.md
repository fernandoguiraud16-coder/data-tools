# Bulk WHOIS lookup in Python

Check hundreds of domains at once with the [Bulk WHOIS Domain Lookup](https://apify.com/fguiraud/bulk-whois-domain-lookup) Actor: registrar, creation and expiry dates, domain age and whether the domain is registered at all. Uses RDAP with a WHOIS fallback, and works with country-code domains like `.co.uk`.

```bash
python check_domains.py domains.txt --expiring-days 60
```

```text
Checked 4 domains

Not registered (1):
  this-domain-surely-does-not-exist-9x7q.com

Expiring within 60 days (0):

Full results saved to whois.csv
```

## Use cases

- **Domain investing**: check availability and age for a list of names.
- **Brand protection**: watch expiry dates of your own and look-alike domains.
- **Lead scoring**: domain age is a simple signal of how established a company is.

Full field reference: [`sample-output.json`](sample-output.json) and the [Actor page](https://apify.com/fguiraud/bulk-whois-domain-lookup).
