import os
import glob
import xml.etree.ElementTree as ET

dt = []
t_name = 'dung'
folder = 'xmls'
files = glob.glob(os.path.join(folder,'*.xml'))

for file in glob.glob(os.path.join(folder,'*.xml')):
    tree = ET.parse(file)
    root= tree.getroot()
    count = 0
    bounding = []

    for child in root:
        if child.tag == 'filename':
            name = child.text
        if child.tag == 'object':
            flag = False
            label_name = ''
            for ob_c in child:

                if ob_c.tag == 'name':
                    if ob_c.text == t_name:
                        label_name = ob_c.text + '/'




                if ob_c.tag == 'deleted' and ob_c.text == '0' and label_name == t_name +'/':
                    sub_bounding = [0,0,0,0]
                    bounding_x = []
                    bounding_y = []
                    count +=1
                    flag = True


                if ob_c.tag == 'polygon' and flag == True:
                    flag = False
                    for taget in ob_c:
                        if taget.tag == 'pt':
                            for cor in taget:
                                #print(cor.text)
                                if cor.tag == 'x':
                                    bounding_x.append(cor.text)
                                if cor.tag == 'y':
                                    bounding_y.append(cor.text)
                    sub_bounding[0] = bounding_x[0]
                    sub_bounding[1] = bounding_y[0]
                    sub_bounding[2] = str(abs(int(bounding_x[1]) - int(bounding_x[0])))
                    sub_bounding[3] = str(abs(int(bounding_y[3]) - int(bounding_y[0])))
                    bounding.append([sub_bounding,label_name])
                    #print(bounding[-1])
    if count != 0:
        dt.append([name,count, bounding])


with open(t_name +'.dat','w') as info:
    for element in dt:
        for bounding_box in element[2]:
            temp_str = bounding_box[1] + element[0] + ' ' + str(element[1]) + ' '
            info.write(temp_str)
            for unit in bounding_box[0]:
                info.write(unit)
                info.write(' ')
            #info.write('\n')
        info.write('\n')



