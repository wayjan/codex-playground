def main():
    message = "Hello from Codex!"
    print(message)

    with open("output.txt", "w") as f:
        f.write(message)

if __name__ == "__main__":
    main()
