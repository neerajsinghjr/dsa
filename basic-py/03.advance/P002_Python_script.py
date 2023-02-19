"""
    __summary__ : 
"""

import sys
import csv
from collections import defaultdict
from app.main import db_session as db
from app.model.investment import Investment, Customer
from sqlalchemy.sql.expression import bindparam
from app.log import get_logger
from copy import deepcopy
from datetime import datetime,date

LOG = get_logger()



# Validate pan_number;;
# pans = ['AAEPP4583D', 'ABIPT3116B', 'AAOPK8930B', 'AASPW5393E', 'AAUPH6081N', 'ACAPE1380M', 'AAAPP7607G', 'AAAPS1706P', 'AEFPH2634L', 'AEFPI3478F', 'AEHPN6204L', 'AEJPD2902D', 'ACRPR9465P', 'ADKPC3210B', 'ACNPR6419F', 'ADVPB7576Q', 'AGFPG2816H', 'AIHPL5097R', 'AERPA5459C', 'AEVPI2153P', 'AFNPH7500L', 'AFEPC9763M', 'AFTPB0635C', 'AFTPM8878C', 'AFWPD9636G', 'AGNPJ5228N', 'AGSPM8528K', 'AGXPP4052E', 'AGXPV1474C', 'AHPPT7336J', 'AHSPK1151H', 'AHTPB6894P', 'AHVPL9522C', 'AHXPV8961D', 'AIAPK4081B', 'AIDPM7549M', 'AJHPG0999C', 'AKBPC4301P', 'AKBPV9625P', 'AKQPS7632A', 'ALOPK3030H', 'ALYPH5994H', 'AJPPC7282C', 'AJVPB3835A', 'AJWPM2024P', 'AKGPP9209C', 'AKJPA6815A', 'ALSPM4433G', 'AMRPB0053H', 'AMCPG6397G', 'APCPS9385K', 'APEPD1468G', 'AMXPP9751A', 'AMXPT2202N', 'AOCPM3409H', 'AODPV8898L', 'AOHPJ8919G', 'AOJPH0208N', 'AOKPL2041J', 'ANDPV7868F', 'ANFPB4675C', 'ANJPC6628G', 'ANMPT4788M', 'APKPK3015Q', 'APHPA6750P', 'ANVPS2265D', 'ANXPD8094M', 'AMFPN5498J', 'ASOPA2677H', 'ASRPV4014A', 'AQWPR0595F', 'ARDPS4660C', 'AWSPK9850E', 'ARHPK3148B', 'ATPPV6618R', 'ARTPM0774B', 'AQSPD9143M', 'AQSPP5288R', 'ATWPS8303H', 'AUBPB4625P', 'AWBPK3366N', 'APRPR8364N', 'ASIPT3109M', 'APWPH9107G', 'AWMPD3263C', 'AQEPB4611J', 'AQEPB5058P', 'BFGPM7487H', 'AYOPV0652P', 'BJSPG8906K', 'BOFPJ6394Q', 'BGKPT6530M', 'BJXPA2670R', 'AXLPB2776N', 'BEJPA2722M', 'BNBPP3682E', 'BGPPS7393E', 'BKIPD9858E', 'BKPPC6215F', 'BPJPR3108F', 'AXHPP3008P', 'BLUPD9867L', 'BISPB4381G', 'BBVPN9995G', 'BBWPN5776J', 'AYIPJ0082H', 'AYJPH4753N', 'AZJPH5418B', 'BEQPG2447N', 'BERPK1022E', 'AZBPM6288J', 'BGGPK7104J', 'BJPPS3453Q', 'BJQPD4227C', 'BMJPT5319K', 'BMLPN2552G', 'BEXPD0354J', 'BMMPM7317M', 'AYUPY1363J', 'BFKPS0772M', 'BFOPC8783E', 'AXDPA5670L', 'BPDPC4732A', 'BKWPS1087C', 'BIFPP2140A', 'BBGPP4023E', 'BFZPT3110H', 'BOVPA0031F', 'BHBPS8421G', 'BPGPP5304E', 'BBAPJ6933R', 'BBEPA8087R', 'CLVPD8989B', 'CTGPA0861C', 'CTPPS3115L', 'CWUPR4576C', 'CWYPS3768K', 'DFHPS6707F', 'BWDPK7758R', 'EBTPS2219P', 'DSHPM1092J', 'FJCPS4553L', 'FHNPM6327R', 'DWMPB1730F', 'DOMPM6087N', 'CKNPS9506A', 'DETPG3497F', 'DYMPR6612E', 'EPZPK5426N', 'EPZPP5635A', 'BVTPS4121B', 'DKCPM7292B', 'BWTPK0048L', 'BYUPP0651B', 'DMZPK3608A', 'CJNPS2578D', 'CJPPR9036M', 'BTYPD5519H', 'BUCPR1451B', 'BUHPS6192R', 'BUVPK6304H', 'CPVPR8241G', 'EAKPK9424E', 'FQHPK2124R', 'EEJPS1691A', 'EELPD3514R', 'FVVPP4856G', 'CUPPM8145P', 'BQPPC7621B', 'BQQPP3692A', 'DBWPP7954L', 'DCCPA7092H', 'BQWPJ5092A', 'BQZPV9304E', 'BRAPN9738A', 'BTXPA1487N', 'DHMPS0139G', 'DMCPS7984A', 'ECIPM3300K', 'FTFPD2632Q', 'CGZPT4311A', 'FWTPM5721G', 'CVNPG1862L', 'EFLPD0936J', 'DAUPA8534E', 'CZPPP9819L', 'CZTPM2778K', 'BTOPA9040E', 'BTPPP5499B', 'CJMPM6723K', 'CEVPN3899B', 'CEWPS3735L', 'CMYPM0059D', 'CMZPS1464D', 'CRRPK6316H', 'CRTPS2948M', 'ECRPK0301K', 'FSIPP1657M', 'DLRPM9166A', 'DBLPS1459A', 'DCUPS6454K', 'ELFPK1369N', 'CNEPK0480M', 'CNRPS4015B', 'DLNPB9655P', 'ETTPM2016J', 'CXMPK6975K', 'CXQPK1019J', 'CYLPB4450Q', 'CCMPD0403J', 'COHPS9899N', 'CPPPD3190C', 'BVOPS6182H', 'EOMPB4294F', 'FVYPK2970M', 'DTQPS9040L', 'CIDPP6040A', 'EHQPR1806A', 'BSBPA2951G', 'EKQPM5725J', 'BSYPJ7354K', 'ERXPM3678E', 'DJVPM0449A', 'BXXPS3095Q', 'EUZPS5410K', 'EVFPS3288J', 'CAYPR8216D', 'CBTPC4835M', 'CBZPK6403P', 'DQQPS9396G', 'HESPS0305R', 'HBKPK4714F', 'HCVPK0350K', 'HDEPS2385J', 'HKLPD9017E', 'HLMPS6572P', 'HNZPK2306A', 'HVPPS3677Q', 'HWUPS6228B', 'HXKPK9870G', 'IFWPK4843G', 'IIOPS4157N', 'ITLPS5056L', 'KSPPS8816B', 'JQCPS3779D', 'MLUPS0130E', 'LAIPS1779M', 'NYNPS9304B']

# counter = 0
# for pan in pans:
#     if pan[3] == 'P':
#         counter += 1
#     else:
#         print('not found : ', pan)
# print("counter : " , counter)
# print(len(pans))


#--- Script 3 : Modify first_name, middle_name, last_name and nominee_name as per pan_name;

# file = sys.argv[1]
# result = '/home/neerajsingh/Downloads/TEST_DATA.txt'
# csv_format = []
# records = []
# f, m, l, pan = 1, 2, 3, 25
# with open(file) as f:
#     reader = csv.reader(f)
#     for row in reader:
#         # print("row :", row)
#         rw = row[0].split('|')
#         cur_row = deepcopy(rw)
#         # print("cur_row : ", cur_row)
#         # print("pan_number : ", cur_row[pan])
#         pan_name = cur_row[131]
#         # print('pan_name : ', pan_name)

#         ##--- TASK 1 : FIX NAME FROM PAN_NAME
#         p_name_split = pan_name.split(' ')
#         p_name_len = len(p_name_split)
#         # print('pan_name_split : ', p_name_split)
#         if p_name_len == 1:
#             cur_row[1] = str(p_name_split[0])
#             cur_row[2], cur_row[l] = '',''
#         elif p_name_len == 2:
#             cur_row[1] = str(p_name_split[0])
#             cur_row[2] = ''
#             cur_row[3] = str(p_name_split[1])
#         elif p_name_len > 2:
#             # print('###', p_name_split[0], p_name_split[1:p_name_len-1], p_name_split[p_name_len-1])         
#             # print('***', cur_row[1], cur_row[2], cur_row[3])   
#             ch = ''
#             for c in p_name_split[1:p_name_len-1]:
#                 ch += c
#             cur_row[1], cur_row[2], cur_row[3] = str(p_name_split[0]), ch, str(p_name_split[p_name_len-1])
#                 # str(p_name_split[1:p_name_len-1]), \
                
#             # print('***', cur_row[1], cur_row[2], cur_row[3])   

#         ##--- TASK 2 : TRUNCATE SPECIAL CHAR FROM NOM_NAME;
#         nom_name = cur_row[93]
#         if '@' in nom_name:
#             # print(">>>>>>>>>>>>>>>>> nom_name : ", nom_name)
#             cur_row[93] = nom_name[0: nom_name.index('@')]
#             # print("nom changed : ", cur_row[93])
#         if '.' in nom_name:
#             # print(">>>>>>>>>>>>>>>>> nom_name : ", nom_name)
#             cur_row[93] = nom_name.replace('.', '')
#             # print("nom changed : ", cur_row[93])
#         if '-' in nom_name:
#             # print(">>>>>>>>>>>>>>>>> nom_name : ", nom_name)
#             cur_row[93] = nom_name.replace('-', '')
#             # print("nom changed : ", cur_row[93])
#         if '_' in nom_name:
#             # print(">>>>>>>>>>>>>>>>> nom_name : ", nom_name)
#             cur_row[93] = nom_name.replace('_', '')
#             # print("nom changed : ", cur_row[93])

#         # nom_n, nom_f, nom_dob, nom_g = 93, 96, 97, 98
#         ##--- TASK 3 : CHECK FOR MINOR FLAG AND GUARDIAN NAME;
#         nom_dob = cur_row[97]
#         if nom_dob:
#             nom_dob = nom_dob.split('/')
#             # print(nom_dob)
#             today = date.today()
#             dob = datetime(day=int(nom_dob[0]), month=int(nom_dob[1]), year=int(nom_dob[2]))
#             # print(today, dob)
#             age = today.year - dob.year
#             # set minor;
#             if age <= 18:
#                 cur_row[96] = 'Y'
#             elif age > 18:
#                 cur_row[96] = 'N'
    
#         records.append(cur_row[0:131])

# if not records:
#     print("No Records Found")

# for record in records:
#     row = ''
#     cur_count = 0
#     end_count = len(record)-1
#     for data in record:
#         # print(">>>>>>>>> data : ", data)
#         row += data
#         cur_count += 1
#         if not(cur_count == end_count):
#             row += '|'
    
#     # print('\n')
#     # print("single csv row :", row)
#     csv_format.append(row)

# # print(">>>>>>>>>>> csv format : ", csv_format)

# with open(result, mode='w') as wf:
#     writer = csv.writer(wf)
#     writer.writerows(csv_format)

# print("EOF reached !!!")
        

#--- Script 2 : To Crawl the error files;

# error = '/home/neerajsingh/Downloads/co_task/err/main_error_new.csv'
error = '/home/neerajsingh/Downloads/TEST_ERROR_NEW.csv'
files = [
    '/home/neerajsingh/Downloads/TEST_ERROR.csv',
    
    # # Read using utf-8 encoding;
    # '/home/neerajsingh/Downloads/co_task/err/err_01.csv',
    # '/home/neerajsingh/Downloads/co_task/err/err_02.csv',

    # # Reading using utf-16 encoding;
    # '/home/neerajsingh/Downloads/co_task/err/err_03.csv',
    # '/home/neerajsingh/Downloads/co_task/err/err_04.csv',
    # '/home/neerajsingh/Downloads/co_task/err/err_05.csv',
    # '/home/neerajsingh/Downloads/co_task/err/err_06.csv',
    # '/home/neerajsingh/Downloads/co_task/err/err_07.csv',
    # '/home/neerajsingh/Downloads/co_task/err/err_08.csv',
    # '/home/neerajsingh/Downloads/co_task/err/err_09_1_1.csv',
    # '/home/neerajsingh/Downloads/co_task/err/err_09_1_2.csv',
    # '/home/neerajsingh/Downloads/co_task/err/err_09_1_3.csv',
    # '/home/neerajsingh/Downloads/co_task/err/err_09_2.csv',
    # '/home/neerajsingh/Downloads/co_task/err/err_09_3.csv',
    # '/home/neerajsingh/Downloads/co_task/err/err_10.csv',
]
## fetching all errors store it in csv;;
pan_number = ''
for file in files:
    records = []
    print(f"reading starting ... ({file})")
    with open(file, errors='ignore') as rf:
    # with open(file, encoding="utf16", errors='ignore') as rf:
        reader = csv.reader(rf)
        for row in reader:
            if '|FAILED' in row[0]:
                data = row[0].split('|')
                records.append(
                    [
                        data[-1], data[25], row[0]
                    ]
                )
    print(f"reading done... ({file})")
    if not records:
        print(f"No error found for this file ... ({file})")
        continue
    
    print(f"writing starting ... ({file})")
    with open(error, mode='a') as wf:
        writer = csv.writer(wf)
        writer.writerows(records)
    pass
    
    print(f"writing done ... ({file})")
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> END !!!")
    

#--- Script 1 : fetching pan_number;;

# file = sys.argv[1]
# records = ""
# pan_numers = ""
# err_msg = "NEFT/IFSC CODE DOES NOT EXISTS FOR BANK 1"
# counter = 20
# with open(file) as f:
#     rows = csv.reader(f)
#     for row in rows:
#         if err_msg in row[0]:
#             records += "ROW " + str(counter)  + " --> " +  row[0] + " \n\n"
#             counter += 1

#     print(records)
