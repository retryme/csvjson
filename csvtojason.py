import os
import csv

for root, dirs, files in os.walk(r'C:\Users\erdem.eker\Desktop\Projeler\İgdaş\Postman\config\optimization\poc\samples'):
    print(files)
    len_fil = len(files)
    direc_list = list()
    for i in range(len_fil):
        dir_er = r'C:\Users\erdem.eker\Desktop\Projeler\İgdaş\Postman\config\optimization\poc\samples' + '\\' + files[i]
        print(dir_er)
        direc_list.append(dir_er)

leng_of_direclist = len(direc_list)

for file_co in range(leng_of_direclist):
    with open(direc_list[file_co], encoding='utf-8') as csv_file:
        row_count = sum(1 for row_2 in csv_file)
        # print("row_count",row_count)

    with open(direc_list[file_co], encoding='utf-8') as csv_file:
        name_1 = files[file_co] + '.json'
        text_file = open(name_1, "a+")
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        prnt = 1
        for row in csv_reader:
            if line_count == 0:
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # print(f'\t{row[0]} works in the {row[1]} department, and was born in {row[2]}.')
                if (prnt == 1):
                    print("{")
                    print("\"sebekeSefligiID\"", ":", row[8] + ",")
                    print("\"isEmriID\"", ":", "\"" + str(line_count) + "\"" + ",")
                    print("\"isEmriTipi\"", ":", "\"" + row[11] + "\"" + ",")
                    print("\"isEmriKategorisi\"", ":", "\"" + row[10] + "\"" + ",")
                    print("\"isEmriKoordinati\"", ":", "\"" + str(float(row[0].replace(',', '.'))) + ",",
                          str(float(row[1].replace(',', '.'))) + "\"" + ",")
                    print("\"baslangicTarihi\"", ":", "\"{{baslangicTarihi}}\"", ",")
                    print("\"bitisTarihi\"", ":", "\"{{bitisTarihi}}\"")
                    print("}", end='')
                    if line_count == row_count - 1:
                        pass
                    else:
                        print(",")
                    line_count += 1

                else:
                    text_file.write('{' + '\n')
                    text_file.write('\"sebekeSefligiID\"' + ':' + row[8] + ',' + '\n')
                    text_file.write('\"isEmriID\"' + ':' + '\"' + str(line_count) + '\"' + ',' + '\n')
                    text_file.write('\"isEmriTipi\"' + ':' + '\"' + row[11] + '\"' + ',' + '\n')
                    text_file.write('\"isEmriKategorisi\"' + ':' + '\"' + row[10] + '\"' + ',' + '\n')
                    text_file.write(
                        '\"isEmriKoordinati\"' + ':' + '\"' + str(float(row[0].replace(',', '.'))) + ',' + str(
                            float(row[1].replace(',', '.'))) + '\"' + ',' + '\n')
                    text_file.write('\"baslangicTarihi\"' + ':' + '\"{{baslangicTarihi}}\"' + ',' + '\n')
                    text_file.write('\"bitisTarihi\"' + ':' + '\"{{bitisTarihi}}\"' + '\n')

                    if line_count == row_count - 1:
                        text_file.write('}')
                    else:
                        text_file.write('},')
                        text_file.write('\n')
                    line_count += 1

        # print(f'Processed {line_count} lines.')
        text_file.close()

