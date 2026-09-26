# Competitor Google ads in Python

Get every Google ad (Search, Display and YouTube) of any competitor from the [Google Ads Transparency Center](https://adstransparency.google.com), with preview images and how long each ad has been running, through the [Google Ads Transparency Scraper](https://apify.com/fguiraud/google-ads-transparency-scraper) Actor.

## Longest-running ads of your competitors

```bash
python competitor_ads.py "Notion" clickup.com --region US --max 10
```

Real output (September 2026):

```text
20 ads. Longest running:
    327 days  text   Mango Technologies, Inc.        https://adstransparency.google.com/advertiser/AR15602211594623254529/creative/CR00308453401463619585?region=US
    256 days  video  Mango Technologies, Inc.        https://adstransparency.google.com/advertiser/AR15602211594623254529/creative/CR18191257712178757633?region=US
    150 days  text   Notion Labs, Inc                https://adstransparency.google.com/advertiser/AR13309761427309854721/creative/CR04412979949183434753?region=US
    101 days  video  Notion Labs, Inc                https://adstransparency.google.com/advertiser/AR13309761427309854721/creative/CR15742237192149270529?region=US

Saved to competitor_ads.csv
```

Ads that run for months are usually the ones that convert, so sort by `daysRunning` first. Note how the domain search found ClickUp's ads under its legal name, **Mango Technologies, Inc.**: search by domain when you don't know the advertiser's registered name.

## Alerts for new competitor ads

```bash
python new_ads_alert.py "competitor one" competitor-two.com --region US
```

Run it weekly. The Actor remembers which ads it already returned, so each run gives only the ads launched since the last one, and you pay only for those.

## Use cases

- **Ad copy and creative research** before launching your own campaigns.
- **Competitor monitoring**: new ads usually mean a new offer, product or market.
- **Brand protection**: search your own domain to find resellers advertising with your brand.

Full field reference: [`sample-output.json`](sample-output.json) and the [Actor page](https://apify.com/fguiraud/google-ads-transparency-scraper).
