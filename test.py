with open("test.txt", "r") as f:
    payloads = [linha.strip() for linha in f if linha.strip()]


print(payloads)