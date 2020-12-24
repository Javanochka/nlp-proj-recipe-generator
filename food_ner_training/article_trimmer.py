import csv

SOURCE = "articles1"  # CSV file without the extension.


def remove_artefacts_from_title():
    """Remove the artefacts from titles, such as the newspaper's name."""
    r[2] = r[2].replace(" - Breitbart", "")
    r[2] = r[2].replace(" - The New York Times", "")


with open(f"articles_trimmed.csv", "wt", encoding="utf8", newline='') as result:
    wtr = csv.writer(result)
    csv.field_size_limit(100000000)
    for file in ["articles1", "articles2", "articles3"]:
        with open(f"{file}.csv", "rt", encoding="utf8") as source:
            for r in csv.reader(source):
                remove_artefacts_from_title()
                wtr.writerow((r[0], r[1], r[2]))  # Only keep the ids and the titles.
