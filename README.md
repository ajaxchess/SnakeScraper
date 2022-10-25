RC_host: SnakeScraper
Python Web Scraper

RC_host:# Prerequisites:

I ran this on a Macintosh:
```bash
RC_host: uname -a
Darwin Richards-MacBook-Pro.local 21.6.0 Darwin Kernel Version 21.6.0: Mon Aug 22 20:19:52 PDT 2022; root:xnu-8020.140.49~2/RELEASE_ARM64_T6000 arm64
RC_host: which python3
/usr/bin/python3
RC_host: python3 --version
Python 3.9.6
RC_host: python3 -m pip install requests
RC_host: python3 -m pip install bs4
RC_host: python3 -m pip uninstall lxml
```

RC_host:# Test Your Environment:

```bash
RC_host: python3 test_scrape_env.py
“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
Albert Einstein
change
deep-thoughts
thinking
world
...
```

You should see Quotes from Famous People and Tags related to those quotes.
This shows that you can read files from the web and your parser works.
