import requests
import os
import threading
import argparse

def download_part(url, start_byte, end_byte, part_number, file_name):
    headers = {'Range': f'bytes={start_byte}-{end_byte}'}
    try:
        response = requests.get(url, headers=headers, stream=True)
        if response.status_code == 206:  # Partial Content status code
            with open(file_name + f'.part{part_number}', 'wb') as file:
                for chunk in response.iter_content(chunk_size=1024):
                    if chunk:
                        file.write(chunk)
            print(f"Part {part_number} downloaded successfully")
        else:
            print(f"Failed to download part {part_number}")
    except Exception as e:
        print(f"An error occurred while downloading part {part_number}: {str(e)}")

def download_file_in_parts(url, num_parts, file_name):
    try:
        response = requests.head(url)
        file_size = int(response.headers.get('content-length', 0))

        parts = []
        part_size = file_size // num_parts
        for i in range(num_parts):
            start_byte = part_size * i
            end_byte = start_byte + part_size - 1 if i != num_parts - 1 else file_size - 1
            parts.append((start_byte, end_byte))

        threads = []
        for i, (start_byte, end_byte) in enumerate(parts):
            thread = threading.Thread(target=download_part, args=(url, start_byte, end_byte, i+1, file_name))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        # Merge parts into a single file
        with open(file_name, 'wb') as output_file:
            for i in range(num_parts):
                part_file = file_name + f'.part{i+1}'
                with open(part_file, 'rb') as part:
                    output_file.write(part.read())
                os.remove(part_file)
        print(f"File downloaded successfully as '{file_name}'")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--parti",
        type=bool,
        default=True,
        help="download file as partition",
    )
    parser.add_argument(
        "--source", type=str, default="", help="link source file"
    )
    parser.add_argument(
        "--numpart", type=int, default=4, help="Number of paritition"
    )
    parser.add_argument(
        "--name", type=str, default="", help="name of downloaded file"
    )
    opt = parser.parse_args()

    url_to_file = opt.source
    if opt.name == "": 
        parts = (opt.source).split("/")
        file_name = parts[-1]
    else:
        file_name = opt.name
    num_parts = opt.numpart  # You can adjust this value based on the number of threads you want to use
    download_file_in_parts(url_to_file, num_parts, file_name)



