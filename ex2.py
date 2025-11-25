# import csv
# import requests
#
# status_dict = {"Website": "Status"}
#
# def main():
#     with open("websites.txt", "r") as fr:
#         for line in fr:
#             website = line.strip()
#             status = requests.get(website).status_code
#             status_dict[website] = "working" if status == 200 \
#                 else "not working"
#
#     #print (status_dict)
#     with open("website_status.csv", "w", newline="") as fw:
#         csv_writers = csv.writer(fw)
#         for key in status_dict.keys():
#             csv_writers.writerow([key, status_dict[key]])
#
#
#
# if __name__ == "__main__":
#     main()


import csv
import requests


def main():
    # 1. Read the websites first
    websites = []
    try:
        with open("websites.txt", "r") as fr:
           # filters out empty lines just in case
#            websites = [line.strip() for line in fr if line.strip()]
    except FileNotFoundError:
        print("Error: 'websites.txt' file not found.")
        return

    # 2. Prepare the CSV file
    with open("website_status.csv", "w", newline="") as fw:
        csv_writer = csv.writer(fw)

        # Write the header row first
        csv_writer.writerow(["Website", "Status"])

        print(f"Checking {len(websites)} websites...")

        # 3. Loop through websites and check status
        for website in websites:
            # Ensure URL has a schema (http/https)
            if not website.startswith(('http://', 'https://')):
                url_to_check = f"https://{website}"
            else:
                url_to_check = website

            try:
                # Add a timeout so the script doesn't hang forever
                response = requests.get(url_to_check, timeout=5)

                if response.status_code == 200:
                    status = "Working"
                else:
                    status = f"Issue (Code: {response.status_code})"

            except requests.exceptions.ConnectionError:
                status = "Connection Error (Site might be down)"
            except requests.exceptions.Timeout:
                status = "Timed Out"
            except requests.exceptions.RequestException as e:
                status = f"Error: {e}"

            print(f"{website}: {status}")
            csv_writer.writerow([website, status])

    print("Done! Results saved to website_status.csv")


if __name__ == "__main__":
    main()