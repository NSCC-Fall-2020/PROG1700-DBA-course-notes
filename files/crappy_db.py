import os

# file format:
# <student id>,<first name>,<last name>


def setup():
    if not os.path.isdir('data'):
        os.mkdir('data')
    else:
        print("'data' directory already exists.")
    os.chdir('data')


def write_record(file, id, first_name, last_name):
    file.write(f"{id},{first_name},{last_name}\n")


def insert_data():
    records = [
        ['w0000001', 'john', 'smith'],
        ['w0000002', 'jane', 'doe'],
        ['w0000003', 'jack', 'sprat'],
    ]
    f = open('crappy_db.txt', 'w')
    for r in records:
        write_record(f, *r)
    f.close()


def select_data():
    with open("crappy_db.txt") as f:
        for line in f:
            fields = line.rstrip('\n').split(',')
            print(fields)


def open_file():
    outfile = open("updated_db.txt", "w")
    infile = open("crappy_db.txt")
    return infile, outfile


def get_record(infile):
    line = infile.readline()
    fields = line.rstrip('\n').split(',')
    id, first_name, last_name = fields
    return id, first_name, last_name


def close_file(infile, outfile):
    infile.close()
    outfile.close()
    os.replace("updated_db.txt", "crappy_db.txt")


def delete_data():
    infile, outfile = open_file()
    id, first_name, last_name = get_record(infile)
    if id != 'w0000002':
        write_record(outfile, id, first_name, last_name)
    close_file(infile, outfile)


def update_data():
    infile, outfile = open_file()
    id, first_name, last_name = get_record(infile)
    if id == 'w0000003':
        id = 'w0000002'
    write_record(outfile, id, first_name, last_name)
    close_file(infile, outfile)


if __name__ == "__main__":
    setup()
    insert_data()
    select_data()
    delete_data()
    update_data()

