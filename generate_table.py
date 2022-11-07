import csv

FILENAME = "acal_data.csv"
OUTFILE = "acal_table.html"
BLANK = "-----"

def open_file(fname):
    with open(fname) as fp:
        return list(csv.reader(fp))

def write_header(opath):
    opath.write("<figure class=\"wp-block-table\" style=\"font-size:0.9rem\"><table style=\"height: 503px;\" width=\"803\">")
    opath.write("<tbody>")

def write_footer(opath):
    opath.write("</tbody></table></figure>")

def write_item(item, opath):
    if item:
        opath.write(item)
    else:
        opath.write(BLANK)

def write_column_headers(entry, opath):
    opath.write("<tr>")
    opath.write("<td><strong>" \
            + entry[0] + ", " + entry[1] \
            + "<br>" \
            + entry[2])
    opath.write("</strong></td>")
    opath.write("<td><strong>")
    write_item(entry[3], opath)
    opath.write("<br>")
    write_item(entry[4], opath)
    opath.write("</strong></td>")
    opath.write("<td><strong>")
    write_item(entry[6], opath)
    opath.write("<br>")
    write_item(entry[5], opath)
    opath.write("</strong></td>")
    opath.write("</tr>")

def write_entry(entry, opath):
    opath.write("<tr>")
    opath.write("<td>" \
            + entry[0] + ", " + entry[1] \
            + "<br>" \
            + entry[2])
    opath.write("<td>")
    write_item(entry[3], opath)
    opath.write("<br>")
    write_item(entry[4], opath)
    opath.write("<td>")
    write_item(entry[6], opath)
    opath.write("<br>")
    write_item(entry[5], opath)
    opath.write("</td>")
    opath.write("</tr>")


def main():
    data = open_file(FILENAME)
    with open(OUTFILE, "w") as op:
        write_header(op)
        write_column_headers(data[0], op)
        for entry in data[1:]:
            write_entry(entry, op)
        write_footer(op)


if __name__ == "__main__":
    main()
