def remove_excluded_urls(line, exclude_urls):
    urls = line.split('=')[1].strip().split(',')
    filtered_urls = [url.strip() for url in urls if url.strip() not in exclude_urls]
    return 'hostname = ' + ', '.join(filtered_urls) + '\n'

def main():
    exclude_file = 'QuantumultX/rewrite/exclude.txt'
    target_file = 'QuantumultX/rewrite/chongxie.txt'

    with open(exclude_file, 'r', encoding='utf-8') as f:
        exclude_urls = {line.strip() for line in f}

    with open(target_file, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in lines:
            if line.startswith('hostname'):
                line = remove_excluded_urls(line, exclude_urls)
            f.write(line)

if __name__ == "__main__":
    main()

