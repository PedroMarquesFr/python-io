import json
import csv


def retrieve_books(file):
    return [json.loads(line) for line in file]


def count_books_by_category(books):
    categories = {}
    for book in books:
        for category in book["categories"]:
            if not categories.get(category):
                categories[category] = 0
            categories[category] += 1
    return categories


def count_books_percentage_by_category(categories, num_of_books):
    percentage = {}
    pecentage = [
        [category, categories.get(category) / num_of_books]
        for category in categories
    ]
    print(pecentage)
    return percentage


if __name__ == "__main__":
    with open("books.json") as file:
        books = retrieve_books(file)

    categories = count_books_by_category(books)
    percentage = count_books_percentage_by_category(categories, len(books))
    with open("report.csv", "w") as file:
        writer = csv.writer(file)
        headers = ["categoria", "porcentagem"]
        writer.writerow(headers)
        writer.writerows(percentage)