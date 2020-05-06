import csv


file_name = "localizable_strings.csv"


def props():
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            key = row['key']
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


def loc_strings(lang: str):
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            key = row['key']
            txt = row['en']
            if lang == "kr":
                txt = row['kr']
            print("\"{0}\" = \"{1}\";".format(key, txt))


# gen_swift_properties()
# gen_swift_localizable_strings('English')
# gen_swift_localizable_strings('Korean')
