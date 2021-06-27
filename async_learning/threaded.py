import requests
import time
import concurrent.futures
import threading

thread_local = threading.local()


def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session


def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")


def download_all_sites(websites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as executor:
        executor.map(download_site, websites)


if __name__ == "__main__":
    sites = [
                "https://www.jython.org",
                "https://google.com",
                "http://olympus.realpython.org/dice",
            ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
