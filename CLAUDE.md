# Project notes for Claude

## Binance.US API access (cloud sessions)

Credentials for `api.binance.us` are injected by the session's network proxy
(credential name "ClaudeUS"); they are not environment variables, and Claude
never sees their values.

What is known from testing (2026-10-08):

- Public market data works with no auth, e.g.
  `GET https://api.binance.us/api/v3/ticker/price?symbol=BTCUSDT`.
- The proxy is currently set to inject the API key and secret as **body
  parameters**. On a request with no form body (any GET, or a POST without
  `--data`), the proxy fails with `injection failed ("ClaudeUS")`. With a form
  body it appends two extra parameters, which Binance does not use.
- Binance.US does not accept credentials this way:
  - The API key must be sent in the `X-MBX-APIKEY` **header**.
  - The secret is never sent. It is used to make an HMAC-SHA256 `signature`
    parameter over the query/body. The proxy cannot compute that signature,
    so signed endpoints (`/api/v3/account`, `/api/v3/order`, ...) fail with
    `-1102 signature was not sent`.
  - An earlier header-based setup (API key in a header, secret in a custom
    `BINANCE_SECRET_KEY` header) gave `-2015 Invalid API-key, IP, or
    permissions` even on the key-only endpoint `POST /api/v3/userDataStream`.
    That points to the key's IP restriction (cloud containers have no fixed
    IP) or a wrong/disabled key.

Setup that can work:

1. Proxy injects only the API key, as header `X-MBX-APIKEY`.
2. The secret is available to the session as an environment variable (set in
   the environment settings; only new sessions pick it up), so requests can be
   signed locally.
3. Use a key with withdrawals disabled, trading disabled unless needed, and no
   IP restriction (or one that matches the container's egress).

Status update (2026-10-08, later): the secret is now available as env var
`secretkey` (sign with `openssl dgst -sha256 -hmac "$secretkey"`). The proxy
no longer fails on GET/empty-body requests. But both the key-only
`userDataStream` and a correctly signed `/api/v3/account` still return
`-2015`, so the API key itself is rejected: check the injected header is
named exactly `X-MBX-APIKEY`, the key is the one paired with this secret, and
the key has no IP restriction.

Safe endpoints for checking credentials:
- `POST /api/v3/userDataStream`: needs the API key only, no signature.
- `POST /api/v3/order/test`: validates a signed order without placing it.
