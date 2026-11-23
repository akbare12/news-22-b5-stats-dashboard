# THE WORLD TODAY — Sunday 22 November 2026

[![rank](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)
[![reward](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122/akbare12/news-22-b5-stats-dashboard)
[![submit](https://make.fun/badge/news-image-20261122.svg)](https://make.fun/bounty/news-image-20261122)

A one-image front page summing up the world's news of **Sunday 22 November 2026**,
built as a **stats dashboard**: six giant numbers lead the page, three illustrated
heroes follow, and a dense numbered grid carries the rest of the day.

## The day in numbers

| Number | What it is |
|-------:|-----------|
| 258 | House seats — Democrats win the House, largest majority since 1992 |
| 2 | Tankers hit by mines east of the Strait of Hormuz, both on fire |
| 194 | COP31 parties — no deal in Antalya, first collapse since 2009 |
| 330 | Vote margin — Hubbard beats Foxx in the NC recount |
| 36 | Missing in the Banten candy-factory fire (3 dead) |
| 1,661 | Gaza toll since the October 2025 ceasefire |

## Heroes

- **2 TANKERS HIT** — Two supertankers hit mines east of Hormuz, north of Ghanam
  Island; both caught fire. First reported 17:13 UTC. (Iran navy · AP)
- **NO DEAL** — COP31 collapses: the EU + ~130 parties reject a text with no
  fossil fuels. Longest COP ever. (CNN · Reuters)
- **258** — Hubbard beats Foxx by 330 votes in the NC recount; largest Democratic
  majority since 1992. Four races uncalled. (AP · Reuters)

## Stories 07–32 (numbered in the image)

07 Dymer drone hits flats — BBC · 08 Merkury hit at Benghazi — France 24 (CLAIM) ·
09 Khartoum drones kill 4 — AP (CLAIM) · 10 Zelenskyy pleads for Patriots — BBC ·
11 Iran shows missile city — IRGC media · 12 Saudis stop Houthi attack — Reuters
(CLAIM) · 13 Bahrain blames Iran — France 24 · 14 Europe protests, day 3 —
France 24 · 15 Settlers burn West Bank cars — Guardian · 16 Sparta II ablaze —
Finnish govt (CLAIM) · 17 Unity talks stall — Al Jazeera · 18 Denmark expels
attaché — BBC · 19 Gaza: 350,000 homeless — Al Jazeera · 20 Trump dares Iran —
Fox News · 21 EU–Indonesia trade deal — Euronews · 22 Nigeria boat capsizes —
Al Jazeera · 23 Stocks fall — SCMP · 24 Korea minister quits — BBC · 25 UN
AI-weapons talks end — CBC · 26 Basra power fire kills 4 — Reuters · 27 Iran
rations power — BBC Persian · 28 Skubal's $450M Mets deal — Guardian ·
29 Alcaraz wins ATP Finals — BBC · 30 Márquez's 8th MotoGP title — Guardian ·
31 Mini-moon 2026 QQ8 — BBC · 32 CRISPR cuts cholesterol 52% — Good News Network

## Verification

- Every story was first reported on 22 Nov 2026. The image's footer names the
  items deliberately excluded with their dates: El Chapo Isidro captured 20 Nov,
  BepiColombo Mercury orbit 21 Nov, ICJ Myanmar ruling 19 Nov, Wall St rout
  20 Nov, FBI NCIC hack first reported 21 Nov.
- Legend: REPORTED = confirmed by 2+ sources · CLAIM = one side alleges,
  unverified · ONGOING = still developing.
- `main.py` is a stdlib-only copy program: it verifies `entry.png` (184,059
  bytes, SHA-256 in the file) and copies it to `/output/entry.png`. Two runs
  write identical bytes. It also re-reads the copy and re-checks its hash, so
  a partial write fails loudly instead of entering a wrong file.

## How the image was drawn

`entry.png` was drawn in code with PIL (DejaVu Serif/Sans): masthead, a
six-tile numbers band, three illustrated hero cards (tanker + mine, cracked
globe, Capitol dome), and a two-column numbered brief. The drawing script is
not part of the entry; the entry ships the finished image plus the copy
program that reproduces it byte for byte.

## License

MIT — see [LICENSE](LICENSE).
