[![Mastodon badge](https://img.shields.io/badge/Mastodon-Toot-purple?logo=mastodon&&labelColor=450657)](https://masto.ai/@robertoprevato/109401142597221543)

# temp-httpx-tests

Temporary repository to share some performance checks for HTTP clients using
asyncio.

It compares:

- HTTP GET requests made using the built-in `urllib` package inside a executor
- HTTP GET requests made using `httpx.AsyncClient`
- HTTP GET requests made using `blacksheep.client.session`

This test was only done because I am planning to remove the implementation of
[HTTP Client in BlackSheep](https://www.neoteroi.dev/blacksheep/#timeline) and
remove the parts that use `urllib`, and to include `httpx` as a dependency.
Note: `urllib` was used because in this case `blacksheep` is only using it to
make web requests to implement `OpenID Connect` integration and to fetch
well-known configuration (this kind of web requests happen seldomly during web
applications life time).

See [this discussion on Mastodon for more information](https://masto.ai/@robertoprevato/109401142597221543).

## How to run

1. create a virtual environment `python3.11 -m venv venv && source venv/bin/activate`
2. install `pip install -r requirements.txt`
3. start the `Flask` server in a terminal (`python server.py`)
4. start `test.ipy` using `iPython` with `ipython test.ipy`
5. compare the results

The test server is just a development server, but I got similar results using
`uvicorn` as HTTP server (of course, with overall better response times,
depending on the HTTP server).

---

Example results:

```bash
*** Plain text ***
Running %timeit using urllib in executor:
1.19 ms ± 70.7 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

Running %timeit using httpx.AsyncClient:
2.01 ms ± 40.3 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

Running %timeit using blacksheep.client:
1.05 ms ± 20.8 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

*** JSON ***
Running %timeit using urllib in executor:
1.2 ms ± 62.5 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

Running %timeit using httpx.AsyncClient:
2.53 ms ± 172 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

Running %timeit using blacksheep.client:
1.13 ms ± 52.3 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

```bash
*** Plain text ***
Running %timeit using urllib in executor:
1.2 ms ± 43 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

Running %timeit using httpx.AsyncClient:
2.01 ms ± 28.5 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

Running %timeit using blacksheep.client:
1.04 ms ± 29.6 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

*** JSON ***
Running %timeit using urllib in executor:
1.22 ms ± 16.8 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)

Running %timeit using httpx.AsyncClient:
2.23 ms ± 100 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

Running %timeit using blacksheep.client:
1.03 ms ± 26 µs per loop (mean ± std. dev. of 7 runs, 1,000 loops each)
```

---

Maybe using iPython %timeit is not the right way to run performance checks,
however all three clients are tested in the same way and consistent results
were obtained testing with different HTTP servers.
