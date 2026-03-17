# Destroyer — Web Fuzzer

A fast, multithreaded web fuzzer inspired by [ffuf](https://github.com/ffuf/ffuf), built in Python. Supports subdomain fuzzing (DNS mode) and virtual host fuzzing (Host header mode).

---

## Requirements

```bash
pip3 install requests
pip3 install pyfiglet
```

---

## Usage

```bash
python3 destroyer.py [options] -u <host> -w <wordlist>
```

The keyword `DESTROY` in the host is replaced with each word from the wordlist.

---

## Arguments

| Argument | Description | Default |
|----------|-------------|---------|
| `-u` | Target URL with `DESTROY` as the fuzz keyword | *(required)* |
| `-w` | Path to the wordlist file | *(required)* |
| `-t` | Number of threads | `50` |
| `--only-200` | Show only HTTP 200 responses | `false` |
| `--length` | Filter by response content length | `none` |
| `--mode` | Fuzzing mode: `dns` or `host` | `dns` |
| `--http` | Use HTTP instead of HTTPS | `false` |
| `--timeout` | Request timeout in seconds | `5` |

---

## Examples

### DNS mode — subdomain fuzzing
```bash
python3 destroyer.py --http --mode dns -u DESTROY.example.com -w wordlist.txt
```

### Host header mode — virtual host fuzzing
```bash
python3 destroyer.py --http --mode host -u DESTROY.example.com -w wordlist.txt
```

### Testing locally
```bash
python3 destroyer.py --http --mode dns -u DESTROY.localhost:8000 -w wordlist.txt
```

### Filter only 200 responses
```bash
python3 destroyer.py --http --only-200 -u DESTROY.example.com -w wordlist.txt
```

### Filter by response length
```bash
python3 destroyer.py --http --length 1024 -u DESTROY.example.com -w wordlist.txt
```

### Custom threads and timeout
```bash
python3 destroyer.py --http -t 100 --timeout 10 -u DESTROY.example.com -w wordlist.txt
```

---

## DESTROY keyword

The `-u` argument **must** contain the keyword `DESTROY` in the position you want to fuzz.

```bash
# ✅ Correct
-u DESTROY.localhost:8000

# ❌ Wrong — wordlist won't load into the URL
-u localhost:8000
```

---

## Output

- 🟢 **Green** — HTTP 200 responses
- 🔴 **Red** — All other status codes (hidden with `--only-200`)

```
admin.localhost      STATUS:200 | LENGTH: 1523 | RESPONSE_TIME:0.342s
test.localhost       STATUS:403 | LENGTH: 348  | RESPONSE_TIME:0.121s
```

---

## ⚠️ Disclaimer

This tool is intended for **authorized security testing only**. Do not use against systems you do not own or have explicit permission to test.

---

## 📄 License

MIT
