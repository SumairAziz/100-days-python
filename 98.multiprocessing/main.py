import os
import multiprocessing
import requests
import concurrent.futures

# Function to download image
def download(url, name):
    try:
        print(f"Started downloading {name}")
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        file_path = f"files/{name}.jpg"
        
        # Ensure the directory exists
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        with open(file_path, "wb") as file:
            file.write(response.content)
        
        print(f"Finished downloading {name}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {name}: {e}")

# URL to download from
url = "https://picsum.photos/200/300"

# List to hold processes
pros = []

# Loop to create and start processes

if __name__ == '__main__':
#     for i in range(5):
#         p = multiprocessing.Process(target=download, args=[url, i])
#         p.start()
#         pros.append(p)

#     # Join processes to wait for them to finish
#     for p in pros:
#         p.join()


    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1=[i for i in range(5,10)]
        l2=[url for i in range(5,10)]
        results=executor.map(download,l2,l1)
        for r in results:
            print(r)