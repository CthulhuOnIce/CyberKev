# Stasi
## Moderation bot

[![forthebadge](https://forthebadge.com/images/badges/fuck-it-ship-it.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/open-source.svg)](https://forthebadge.com)
[![forthebadge](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxODQuMjUiIGhlaWdodD0iMzUiIHZpZXdCb3g9IjAgMCAxODQuMjUgMzUiPjxyZWN0IGNsYXNzPSJzdmdfX3JlY3QiIHg9IjAiIHk9IjAiIHdpZHRoPSI5MS43NiIgaGVpZ2h0PSIzNSIgZmlsbD0iI0ZGMDAwMCIgZGF0YS1kYXJrcmVhZGVyLWlubGluZS1maWxsPSIiIHN0eWxlPSItLWRhcmtyZWFkZXItaW5saW5lLWZpbGw6I2NjMDAwMDsiLz48cmVjdCBjbGFzcz0ic3ZnX19yZWN0IiB4PSI4OS43NiIgeT0iMCIgd2lkdGg9Ijk0LjQ5MDAwMDAwMDAwMDAxIiBoZWlnaHQ9IjM1IiBmaWxsPSIjRDUzODM4IiBkYXRhLWRhcmtyZWFkZXItaW5saW5lLWZpbGw9IiIgc3R5bGU9Ii0tZGFya3JlYWRlci1pbmxpbmUtZmlsbDojYTIyMjIyOyIvPjxwYXRoIGNsYXNzPSJzdmdfX3RleHQiIGQ9Ik0xOS41NyAyMkwxNC4yMiAyMkwxNC4yMiAxMy40N0wxNS43MCAxMy40N0wxNS43MCAyMC44MkwxOS41NyAyMC44MkwxOS41NyAyMlpNMjUuMjYgMjJMMjMuNzkgMjJMMjMuNzkgMTMuNDdMMjUuMjYgMTMuNDdMMjUuMjYgMjJaTTI5LjgwIDE4LjE5TDI5LjgwIDE4LjE5TDI5LjgwIDE3LjM5UTI5LjgwIDE2LjE5IDMwLjIzIDE1LjI3UTMwLjY2IDE0LjM1IDMxLjQ2IDEzLjg1UTMyLjI2IDEzLjM1IDMzLjMxIDEzLjM1TDMzLjMxIDEzLjM1UTM0LjcyIDEzLjM1IDM1LjU4IDE0LjEyUTM2LjQ0IDE0Ljg5IDM2LjU4IDE2LjI5TDM2LjU4IDE2LjI5TDM1LjExIDE2LjI5UTM1LjAwIDE1LjM3IDM0LjU3IDE0Ljk2UTM0LjE0IDE0LjU1IDMzLjMxIDE0LjU1TDMzLjMxIDE0LjU1UTMyLjM0IDE0LjU1IDMxLjgyIDE1LjI2UTMxLjMwIDE1Ljk2IDMxLjI5IDE3LjMzTDMxLjI5IDE3LjMzTDMxLjI5IDE4LjA5UTMxLjI5IDE5LjQ3IDMxLjc5IDIwLjIwUTMyLjI4IDIwLjkyIDMzLjI0IDIwLjkyTDMzLjI0IDIwLjkyUTM0LjExIDIwLjkyIDM0LjU1IDIwLjUzUTM0Ljk5IDIwLjE0IDM1LjExIDE5LjIyTDM1LjExIDE5LjIyTDM2LjU4IDE5LjIyUTM2LjQ1IDIwLjU5IDM1LjU3IDIxLjM1UTM0LjcwIDIyLjEyIDMzLjI0IDIyLjEyTDMzLjI0IDIyLjEyUTMyLjIyIDIyLjEyIDMxLjQ0IDIxLjYzUTMwLjY2IDIxLjE1IDMwLjI0IDIwLjI2UTI5LjgyIDE5LjM3IDI5LjgwIDE4LjE5Wk00Ni40NyAyMkw0MC44OSAyMkw0MC44OSAxMy40N0w0Ni40MyAxMy40N0w0Ni40MyAxNC42Nkw0Mi4zOCAxNC42Nkw0Mi4zOCAxNy4wMkw0NS44OCAxNy4wMkw0NS44OCAxOC4xOUw0Mi4zOCAxOC4xOUw0Mi4zOCAyMC44Mkw0Ni40NyAyMC44Mkw0Ni40NyAyMlpNNTIuMTUgMjJMNTAuNjcgMjJMNTAuNjcgMTMuNDdMNTIuMTUgMTMuNDdMNTUuOTcgMTkuNTRMNTUuOTcgMTMuNDdMNTcuNDQgMTMuNDdMNTcuNDQgMjJMNTUuOTUgMjJMNTIuMTUgMTUuOTVMNTIuMTUgMjJaTTYxLjc0IDE5LjQyTDYxLjc0IDE5LjQyTDYzLjIzIDE5LjQyUTYzLjIzIDIwLjE1IDYzLjcxIDIwLjU1UTY0LjE5IDIwLjk1IDY1LjA4IDIwLjk1TDY1LjA4IDIwLjk1UTY1Ljg2IDIwLjk1IDY2LjI1IDIwLjYzUTY2LjY0IDIwLjMyIDY2LjY0IDE5LjgwTDY2LjY0IDE5LjgwUTY2LjY0IDE5LjI0IDY2LjI0IDE4Ljk0UTY1Ljg0IDE4LjYzIDY0LjgxIDE4LjMyUTYzLjc4IDE4LjAxIDYzLjE3IDE3LjYzTDYzLjE3IDE3LjYzUTYyLjAxIDE2LjkwIDYyLjAxIDE1LjcyTDYyLjAxIDE1LjcyUTYyLjAxIDE0LjY5IDYyLjg1IDE0LjAyUTYzLjY5IDEzLjM1IDY1LjAzIDEzLjM1TDY1LjAzIDEzLjM1UTY1LjkyIDEzLjM1IDY2LjYyIDEzLjY4UTY3LjMxIDE0LjAxIDY3LjcxIDE0LjYxUTY4LjExIDE1LjIyIDY4LjExIDE1Ljk2TDY4LjExIDE1Ljk2TDY2LjY0IDE1Ljk2UTY2LjY0IDE1LjI5IDY2LjIyIDE0LjkxUTY1LjgwIDE0LjU0IDY1LjAyIDE0LjU0TDY1LjAyIDE0LjU0UTY0LjI5IDE0LjU0IDYzLjg5IDE0Ljg1UTYzLjQ5IDE1LjE2IDYzLjQ5IDE1LjcxTDYzLjQ5IDE1LjcxUTYzLjQ5IDE2LjE4IDYzLjkyIDE2LjUwUTY0LjM2IDE2LjgxIDY1LjM1IDE3LjEwUTY2LjM1IDE3LjQwIDY2Ljk1IDE3Ljc4UTY3LjU2IDE4LjE2IDY3Ljg0IDE4LjY1UTY4LjEyIDE5LjEzIDY4LjEyIDE5Ljc5TDY4LjEyIDE5Ljc5UTY4LjEyIDIwLjg2IDY3LjMwIDIxLjQ5UTY2LjQ4IDIyLjEyIDY1LjA4IDIyLjEyTDY1LjA4IDIyLjEyUTY0LjE2IDIyLjEyIDYzLjM4IDIxLjc3UTYyLjYwIDIxLjQzIDYyLjE3IDIwLjgzUTYxLjc0IDIwLjIyIDYxLjc0IDE5LjQyWk03Ny45OCAyMkw3Mi40MSAyMkw3Mi40MSAxMy40N0w3Ny45NCAxMy40N0w3Ny45NCAxNC42Nkw3My44OSAxNC42Nkw3My44OSAxNy4wMkw3Ny4zOSAxNy4wMkw3Ny4zOSAxOC4xOUw3My44OSAxOC4xOUw3My44OSAyMC44Mkw3Ny45OCAyMC44Mkw3Ny45OCAyMloiIGZpbGw9IiMwMDAwMDAiIGRhdGEtZGFya3JlYWRlci1pbmxpbmUtZmlsbD0iIiBzdHlsZT0iLS1kYXJrcmVhZGVyLWlubGluZS1maWxsOiMwMDAwMDA7Ii8+PHBhdGggY2xhc3M9InN2Z19fdGV4dCIgZD0iTTEwNS4zNyAyMkwxMDIuOTQgMjJMMTA2LjY1IDEzLjYwTDEwOC45OSAxMy42MEwxMTIuNzEgMjJMMTEwLjI0IDIyTDEwOS41OCAyMC4zN0wxMDYuMDMgMjAuMzdMMTA1LjM3IDIyWk0xMDcuODAgMTUuOTNMMTA2LjcyIDE4LjYxTDEwOC44OCAxOC42MUwxMDcuODAgMTUuOTNaTTExNi40MyAxNy44MEwxMTYuNDMgMTcuODBRMTE2LjQzIDE2LjU0IDExNy4wMyAxNS41NFExMTcuNjMgMTQuNTUgMTE4LjcwIDEzLjk5UTExOS43NyAxMy40MyAxMjEuMTEgMTMuNDNMMTIxLjExIDEzLjQzUTEyMi4yOSAxMy40MyAxMjMuMjMgMTMuODNRMTI0LjE2IDE0LjIyIDEyNC43OCAxNC45N0wxMjQuNzggMTQuOTdMMTIzLjI3IDE2LjMzUTEyMi40MyAxNS40MCAxMjEuMjUgMTUuNDBMMTIxLjI1IDE1LjQwUTEyMS4yNCAxNS40MCAxMjEuMjMgMTUuNDBMMTIxLjIzIDE1LjQwUTEyMC4xNSAxNS40MCAxMTkuNDkgMTYuMDZRMTE4LjgzIDE2LjcxIDExOC44MyAxNy44MEwxMTguODMgMTcuODBRMTE4LjgzIDE4LjUwIDExOS4xMyAxOS4wNFExMTkuNDMgMTkuNTkgMTE5Ljk3IDE5Ljg5UTEyMC41MSAyMC4yMCAxMjEuMjEgMjAuMjBMMTIxLjIxIDIwLjIwUTEyMS45MCAyMC4yMCAxMjIuNDkgMTkuOTNMMTIyLjQ5IDE5LjkzTDEyMi40OSAxNy42MkwxMjQuNTkgMTcuNjJMMTI0LjU5IDIxLjEwUTEyMy44NyAyMS42MSAxMjIuOTQgMjEuODlRMTIyLjAwIDIyLjE3IDEyMS4wNiAyMi4xN0wxMjEuMDYgMjIuMTdRMTE5Ljc0IDIyLjE3IDExOC42OSAyMS42MVExMTcuNjMgMjEuMDUgMTE3LjAzIDIwLjA1UTExNi40MyAxOS4wNiAxMTYuNDMgMTcuODBaTTEzMS45NiAyMkwxMjkuNTggMjJMMTI5LjU4IDEzLjYwTDEzMy40MyAxMy42MFExMzQuNTYgMTMuNjAgMTM1LjQwIDEzLjk4UTEzNi4yNCAxNC4zNSAxMzYuNzAgMTUuMDZRMTM3LjE2IDE1Ljc2IDEzNy4xNiAxNi43MUwxMzcuMTYgMTYuNzFRMTM3LjE2IDE3LjY2IDEzNi43MCAxOC4zNVExMzYuMjQgMTkuMDUgMTM1LjQwIDE5LjQyUTEzNC41NiAxOS44MCAxMzMuNDMgMTkuODBMMTMzLjQzIDE5LjgwTDEzMS45NiAxOS44MEwxMzEuOTYgMjJaTTEzMS45NiAxNS40N0wxMzEuOTYgMTcuOTNMMTMzLjI4IDE3LjkzUTEzNC4wMSAxNy45MyAxMzQuMzggMTcuNjFRMTM0Ljc2IDE3LjI5IDEzNC43NiAxNi43MUwxMzQuNzYgMTYuNzFRMTM0Ljc2IDE2LjEyIDEzNC4zOCAxNS44MFExMzQuMDEgMTUuNDcgMTMzLjI4IDE1LjQ3TDEzMy4yOCAxNS40N0wxMzEuOTYgMTUuNDdaTTE0OC4zMCAyMkwxNDEuOTEgMjJMMTQxLjkxIDEzLjYwTDE0NC4yOSAxMy42MEwxNDQuMjkgMjAuMTFMMTQ4LjMwIDIwLjExTDE0OC4zMCAyMlpNMTU1LjMwIDIyTDE1MS43MSAxMy42MEwxNTQuMjggMTMuNjBMMTU2LjU2IDE5LjA3TDE1OC44OSAxMy42MEwxNjEuMjMgMTMuNjBMMTU3LjY0IDIyTDE1NS4zMCAyMlpNMTY0LjUwIDIxLjM0TDE2NC41MCAyMS4zNEwxNjUuMzcgMTkuNTVRMTY1Ljg2IDE5Ljg4IDE2Ni40OCAyMC4wN1ExNjcuMDkgMjAuMjUgMTY3LjcwIDIwLjI1TDE2Ny43MCAyMC4yNVExNjguMzEgMjAuMjUgMTY4LjY3IDIwLjAyUTE2OS4wMyAxOS43OSAxNjkuMDMgMTkuMzdMMTY5LjAzIDE5LjM3UTE2OS4wMyAxOC41NSAxNjcuNzQgMTguNTVMMTY3Ljc0IDE4LjU1TDE2Ni43NSAxOC41NUwxNjYuNzUgMTcuMDVMMTY4LjI1IDE1LjQ0TDE2NC45NCAxNS40NEwxNjQuOTQgMTMuNjBMMTcxLjAxIDEzLjYwTDE3MS4wMSAxNS4wOUwxNjkuMjcgMTYuOTZRMTcwLjMxIDE3LjE4IDE3MC44NyAxNy44MlExNzEuNDMgMTguNDYgMTcxLjQzIDE5LjM3TDE3MS40MyAxOS4zN1ExNzEuNDMgMjAuMTEgMTcxLjAzIDIwLjc1UTE3MC42MiAyMS4zOSAxNjkuODAgMjEuNzhRMTY4Ljk4IDIyLjE3IDE2Ny43NyAyMi4xN0wxNjcuNzcgMjIuMTdRMTY2Ljg4IDIyLjE3IDE2Ni4wMSAyMS45NVExNjUuMTQgMjEuNzQgMTY0LjUwIDIxLjM0WiIgZmlsbD0iI0RGREZERiIgeD0iMTAyLjc2IiBkYXRhLWRhcmtyZWFkZXItaW5saW5lLWZpbGw9IiIgc3R5bGU9Ii0tZGFya3JlYWRlci1pbmxpbmUtZmlsbDojMmEyZTJmOyIvPjwvc3ZnPg==)](https://forthebadge.com)