import csv
import os
import re
def translate(file, path):
    csv_file = open(file, 'r')
    csv_reader = csv.reader(csv_file, delimiter=',')

    locales = [
        {'identifier' : 'en', 'column' : 2},
        {'identifier' : 'fr', 'column' : 3},
        {'identifier' : 'es', 'column' : 4},
        {'identifier' : 'de', 'column' : 5},
        {'identifier' : 'ja', 'column' : 6},
        {'identifier' : 'sv', 'column' : 7},
        {'identifier' : 'it', 'column' : 8},
        {'identifier' : 'sc', 'column' : 9},
        {'identifier' : 'nl', 'column' : 10},
        {'identifier' : 'fi', 'column' : 11},
        {'identifier' : 'no', 'column' : 12},
        {'identifier' : 'da', 'column' : 13}
                ]


    for aLocale in locales:
        if not os.path.exists(path+'localization'):
            os.makedirs(path+'localization')

#         file = open(path+aLocale['identifier']+'.lproj/Localizable.strings','w')
        file = open(path+'localization/string_'+aLocale['identifier']+".txt",'w')
        for row in csv_reader:
            #Sample Code - You should override it
                key = row[0]
                value = row[aLocale['column']]
                if (len(key) > 0):
                	file.write("\""+key+"\" = \""+escape(value)+"\";\n")
                else:
                	file.write("\n")
        csv_file.seek(0)
        file.close()


def escape(str):
    return str.replace("\"","\\\"").replace("\\\\n","\\n")


def is_valid_android_key(str):
    """
    In android xml file, the key must follow some requirements :
    - the key should not contain uppercased letter
    - The key should not beggin with a number
    - The only special accepted character is _

    You can edit the regexp as you required
    """
    prog = re.compile("([a-z]+)(([a-z]*)(_)*([0-9])*)*")
    result = prog.match(str)
    return result


def escape_android(str):
    """
    This function escape common symbol from iOS to Android ( %@ -> %s )
    You can add your own rules
    """
    tmp = str.replace("\"", "\\\"")\
                .replace("\n", "\\n")\
                .replace("'", "\\'")\
                .replace("%@", "%s")\
                .replace("&", "&amp;")
    if "<" in str or ">" in str:
        return "<![CDATA["+tmp+"]]>"
    else:
        return tmp


def translate_android(file, path):
    """
    This function parse the file located at {file} and export it in files located into {path}
    """

    #Provide here mapping between your CSV columns and the desired output file
    #The key is never write into the output file, use it for clarity
    #The file value is the name of the folder which will be generated by the program
    #The column value should be an integer which represent the column of the desired local in the CSV file
    #
    locales = {
                'en': {'file': 'values/', 'column': 2},
                'fr': {'file': 'values-fr/', 'column': 3},
                'es': {'file': 'values-es/', 'column': 4},
                'de': {'file': 'values-de/', 'column': 5},
                'ja': {'file': 'values-ja/', 'column': 6},
                'sv': {'file': 'values-sv/', 'column': 7},
                'it': {'file': 'values-it/', 'column': 8},
                'sc': {'file': 'values-zh/', 'column': 9},
                'nl': {'file': 'values-nl/', 'column': 10},
                'fi': {'file': 'values-fi/', 'column': 11},
                'no': {'file': 'values-nb/', 'column': 12},
                'da': {'file': 'values-da/', 'column': 13}
                }

    #iterate over all locales to generate the translation file
    for aLocal in locales.keys():

        csv_file = open(file, 'r')
        csv_reader = csv.reader(csv_file, delimiter=',')
        _path = path+'/'+locales[aLocal]['file']
        if not os.path.exists(path):
            os.makedirs(path)
        if not os.path.exists(_path):
            os.makedirs(_path)
        file_pointer = open(_path+'strings.xml', 'w')
        #Add default text to xml file
        file_pointer.write('<?xml version="1.0" encoding="utf-8"?>\n')
        file_pointer.write('<resources xmlns:tools="http://schemas.android.com/tools">\n')

        i = 0
        for row in csv_reader:
            #You have to implement your own parser rules here.
            key = row[0]
            remark = row[1]

           
            value = row[locales[aLocal]['column']]
            value = escape_android(value)

            #Check if the key is valid for android usage. See is_valid_android_key documentation for more infos
            if remark == 'ignore':
                if aLocal == 'en':
                    file_pointer.write("<string name=\"" + key + "\" tools:ignore=\"MissingTranslation\">" + value + "</string>\n")
                    print (key + " " + remark + " " + aLocal)
               

            else:
                if not is_valid_android_key(key):
                    file_pointer.write('\n')
                else:
                    file_pointer.write("<string name=\"" + key + "\">" + value +
                                    "</string>\n")
        file_pointer.write('</resources>\n')
        csv_file.seek(0)
        file_pointer.close()







