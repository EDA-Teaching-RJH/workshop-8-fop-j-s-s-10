import csv

def main():
    with open("contacts.csv", "r") as file:
        print(f"Name\t\t\tEmail")

        for row in csv.DictReader(file):
            print(f"{row["name"]}\t\t\t{row["email"]}")

if __name__ == "__main__":
    main()
