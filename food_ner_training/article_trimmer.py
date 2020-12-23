import csv

SOURCE = "articles1"  # CSV file without the extension.


def remove_artefacts_from_title():
    """Remove the artefacts from titles, such as the newspaper's name."""
    r[2] = r[2].replace(" - Breitbart", "")
    r[2] = r[2].replace(" - The New York Times", "")


with open(f"{SOURCE}.csv", "rt", encoding="utf8") as source:
    csv.field_size_limit(100000000)
    rdr = csv.reader(source)
    with open(f"{SOURCE}_trimmed.csv", "wt", encoding="utf8", newline='') as result:
        wtr = csv.writer(result)
        for r in rdr:
            remove_artefacts_from_title()
            wtr.writerow((r[0], r[1], r[2]))  # Only keep the ids and the titles.
