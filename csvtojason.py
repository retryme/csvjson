import os
import csv
# this loop finds files and folders in the given directory
## For windows
##for root, dirs, files in os.walk(r'C:\Users\Desktop'):
for root, dirs, files in os.walk('/home/root1/Desktop/samples'):
    #print(files)
    len_fil = len(files)
    direc_list = list()
    for i in range(len_fil):
        #for windows
        # dir_er = r'C:\Users\Desktop' + '\\' + files[i]
        dir_er = '/home/root1/Desktop/samples' + '/' + files[i]
        #print(dir_er)
        direc_list.append(dir_er)
#deneme

leng_of_direclist = len(direc_list)

for file_co in range(leng_of_direclist):
    with open(direc_list[file_co], encoding='utf-8') as csv_file:
        row_count = sum(1 for row_2 in csv_file)
        # print("row_count",row_count)

    with open(direc_list[file_co], encoding='utf-8') as csv_file:
        #files listesinde dosya adları var tekil isim için listeden adı çekiliyor
        name_1 = files[file_co] + '.json'
        #Yazılacak text dosyası adı burada tanımlandı ve append yapmak için a+ ile açıldı
        text_file = open(name_1, "a+")
        #csv delimiter tanımı yapılmalı
        csv_reader = csv.reader(csv_file, delimiter=';')
        line_count = 0
        prnt = 0
        for row in csv_reader:
            if line_count == 0:
                #sütun adlarını gösterir
                print(','.join(row))
                #print(f'Column names are {",".join(row)}')
                line_count += 1
            else:
                if (prnt == 1):
                    print("{")
                    print("\"alan1\"", ":", row[8] + ",")
                    print("\"alan2\"", ":", "\"" + str(line_count) + "\"" + ",")
                    print("\"alan3\"", ":", "\"" + row[11] + "\"" + ",")
                    print("\"alan4\"", ":", "\"" + row[10] + "\"" + ",")
                    #vigülü noktaya çevirip float değeri stringe çeviriyor
                    print("\"alan5\"", ":", "\"" + str(float(row[0].replace(',', '.'))) + ",",
                          str(float(row[1].replace(',', '.'))) + "\"" + ",")
                    print("\"alan6\"", ":", "\"{{alan6}}\"", ",")
                    print("\"alan7\"", ":", "\"{{alan7}}\"")
                    print("}", end='')
                    if line_count == row_count - 1:
                        pass
                    else:
                        print(",")
                    line_count += 1

                else:
                    # dosyaya yazmak için text_file.write
                    text_file.write('{' + '\n')
                    text_file.write('\"alan1\"' + ':' + row[8] + ',' + '\n')
                    text_file.write('\"alan2\"' + ':' + '\"' + str(line_count) + '\"' + ',' + '\n')
                    text_file.write('\"alan3\"' + ':' + '\"' + row[11] + '\"' + ',' + '\n')
                    text_file.write('\"alan4\"' + ':' + '\"' + row[10] + '\"' + ',' + '\n')
                    text_file.write(
                        '\"alan5\"' + ':' + '\"' + str(float(row[0].replace(',', '.'))) + ',' + str(
                            float(row[1].replace(',', '.'))) + '\"' + ',' + '\n')
                    text_file.write('\"alan6\"' + ':' + '\"{{alan6}}\"' + ',' + '\n')
                    text_file.write('\"alan7\"' + ':' + '\"{{alan7}}\"' + '\n')

                    if line_count == row_count - 1:

                        text_file.write('}')
                    else:
                        text_file.write('},')
                        text_file.write('\n')
                    line_count += 1

        # print(f'Processed {line_count} lines.')
        #text dosyası kapatıldı
        text_file.close()

