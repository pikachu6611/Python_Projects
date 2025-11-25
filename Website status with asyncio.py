import aiohttp
import asyncio
import csv
import time


async def check_status(session, url):
    """
    Checks the status of a single URL asynchronously.
    """
    try:
        # timeout=5 prevents hanging on bad links
        async with session.get(url, timeout=5) as response:
            # We await the response status
            return [url, "Working" if response.status == 200 else f"Status {response.status}"]
    except aiohttp.ClientConnectorError:
        return [url, "Connection Error"]
    except asyncio.TimeoutError:
        return [url, "Timed Out"]
    except Exception as e:
        return [url, f"Error: {str(e)}"]


async def main():
    # Start the timer
    start_time = time.time()

    # Try to read from file, otherwise use defaults
    try:
        with open("websites.txt", "r") as fr:
            urls = [line.strip() for line in fr if line.strip()]
            # Add https if missing
            urls = [u if u.startswith("http") else f"https://{u}" for u in urls]
    except FileNotFoundError:
        print("websites.txt not found.")

    print(f"Checking {len(urls)} websites asynchronously...")

    # aiohttp.ClientSession is like opening a browser tab
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in urls:
            # Create a task for each URL, but don't wait for it yet
            task = check_status(session, url)
            tasks.append(task)

        # asyncio.gather runs all tasks concurrently and waits for them to finish
        results = await asyncio.gather(*tasks)

    # Write results to CSV
    with open("website_status_async.csv", "w", newline="") as fw:
        writer = csv.writer(fw)
        writer.writerow(["Website", "Status"])
        writer.writerows(results)

    duration = time.time() - start_time
    print(f"Done! Checked {len(urls)} sites in {duration:.2f} seconds.")


if __name__ == "__main__":
    # This is how you run an async entry point
    asyncio.run(main())