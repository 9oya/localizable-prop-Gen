import csv


def gen_swift_properties():
    with open('localizedStringsSample.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            key = row['Key']
            if "%" in key:
                continue
            word_arr = key.split('-')
            print("static let ", end='')
            if word_arr[0] == "title":
                print("title", end='')
            elif word_arr[0] == "msg":
                print("msg", end='')

            for idx, word in enumerate(word_arr):
                if idx == 0:
                    continue
                print(word.capitalize(), end='')
            val_txt = " = NSLocalizedString(\"{0}\", comment: \"\")".format(key)
            print(val_txt)


gen_swift_properties()
