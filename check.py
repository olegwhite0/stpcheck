try:
    from puresnmp import get
except ImportError:
    print('\033[36m pip3 install puresnmp \033[0m\n')
    break
import sys
import os
import re
import struct

file=sys.argv[1]
os.system("clear")
sys.stdout.write('\033[36m')
sys.stdout.write('+----------------------------+\n')
sys.stdout.write('|    SNMP CHECK STP PARAM    |\n')
sys.stdout.write('+----------------------------+\033[0m\n')
#os.system("echo "+ipaddr    )
#DEFINE_VARS
COMMUNITY="public"

#END_DEFINE_VARS
def typedev(ip):
    OID = '1.3.6.1.2.1.1.1.0'
    try:
        snmp_result = get(ip, COMMUNITY, OID)
    except (IOError, Exception) as e:
        return '\033[31mnotresp \033[0m'
    #print(snmp_result)
    if (re.search(r'DES-3052', str(snmp_result))!=None):
        return "3052"
    if (re.search(r'S2326TP-EI', str(snmp_result))!=None):
        return "2326"
    if (re.search(r'S2328P-EI', str(snmp_result))!=None):
        return "2328"
    if (re.search(r'DES-1210-28/ME/B2', str(snmp_result))!=None):
        return "1210-28"
    if (re.search(r'DES-1228/ME', str(snmp_result))!=None):
        return "1228"
    if (re.search(r'DES-3028', str(snmp_result))!=None):
        return "3028"
    if (re.search(r'DES-3200-28/C1', str(snmp_result))!=None):
        return "3200-28"
    if (re.search(r'DES-3200-52/C1', str(snmp_result))!=None):
        return "3200-52"
    if (re.search(r'24-port 10/100', str(snmp_result))!=None):
        return "linksys"
    if (re.search(r'4820-52T-XL', str(snmp_result))!=None):
        return "Fiber_XL"
    if (re.search(r'S4820-52T-X', str(snmp_result))!=None):
        return "Fiber_X"
    if (re.search(r'DGS-1210-10/ME', str(snmp_result))!=None):
        return "1210-10GE"

    return "unknown"


stp_enabled = {
    '3052': ['.1.3.6.1.4.1.171.12.15.1.1.0','other','\033[30;41m disabled \033[0m', ' enabled'],
    '2326': ['1.3.6.1.4.1.2011.5.25.42.4.1.1.0',' enabled','\033[30;41m disabled \033[0m'],
    '2328': ['1.3.6.1.4.1.2011.5.25.42.4.1.1.0',' enabled','\033[30;41m disabled \033[0m'],
    '1210-28': ['.1.3.6.1.4.1.171.10.75.15.2.6.1.1.0',' enabled', '\033[30;41m disabled \033[0m'],#1-enabled  2-disabled
    '1228': ['.1.3.6.1.4.1.171.12.15.1.1.0','other','\033[30;41m disabled \033[0m', ' enabled'],
    '3028': ['.1.3.6.1.4.1.171.12.15.1.1.0','other','\033[30;41m disabled \033[0m', ' enabled'],
    '3200-28': ['.1.3.6.1.4.1.171.12.15.1.1.0','other','\033[30;41m disabled \033[0m', ' enabled'],
    '3200-52': ['.1.3.6.1.4.1.171.12.15.1.1.0','other','\033[30;41m disabled \033[0m', ' enabled'],
    'linksys': '',
    'Fiber_XL': '',
    'Fiber_X': '',
    }
stp_rootbridge = {
    '3052': '1.3.6.1.4.1.171.12.15.2.3.1.13.0',
    '2326': '.1.3.6.1.4.1.2011.5.25.42.4.1.19.1.4.0',
    '2328': '.1.3.6.1.4.1.2011.5.25.42.4.1.19.1.4.0',
    '1210-28': '.1.3.6.1.4.1.171.10.75.15.2.6.1.9.0',
    '1228': '1.3.6.1.4.1.171.12.15.2.3.1.13.0',
    '3028': '1.3.6.1.4.1.171.12.15.2.3.1.13.0',
    '3200-28': '1.3.6.1.2.1.17.2.5.0',
    '3200-52': '1.3.6.1.2.1.17.2.5.0',
    'linksys': '1.3.6.1.2.1.17.2.5.0',
    'Fiber_XL': '.1.3.6.1.4.1.3807.2.1908.13.1.4.0',
    'Fiber_X': '.1.3.6.1.4.1.3807.2.1908.13.1.4.0',
    }
stp_priority = {
    '3052': '1.3.6.1.4.1.171.12.15.2.3.1.12.0',
    '2326': '.1.3.6.1.2.1.17.2.2.0',
    '2328': '.1.3.6.1.2.1.17.2.2.0',
    '1210-28': '1.3.6.1.4.1.171.10.75.15.2.6.1.3.0',
    '1228': '1.3.6.1.4.1.171.12.15.2.3.1.12.0',
    '3028': '1.3.6.1.4.1.171.12.15.2.3.1.12.0',
    '3200-28': '1.3.6.1.4.1.171.12.15.2.3.1.12.0',
    '3200-52': '1.3.6.1.4.1.171.12.15.2.3.1.12.0',
    'linksys': '1.3.6.1.2.1.17.2.2.0',
    'Fiber_XL': '1.3.6.1.4.1.3807.2.1908.13.1.2.0',
    'Fiber_X': '1.3.6.1.4.1.3807.2.1908.13.1.2.0',
    }

port_uplink = {
        '3052': ['49','50', '51','52'],
        '2326': ['25','26'],
        '2328': ['25','26','27','28'],
        '1210-28': ['25','26','27','28'],
        '1228': ['25','26','27','28'],
        '3028': ['25','26','27','28'],
        '3200-28': ['25','26','27','28'],
        '3200-52': ['49','50', '51','52'],
        'linksys': ['25','26', '27','28'],
        'Fiber_XL': ['17474','17475', '17538','17539'],
        'Fiber_X': ['17474','17475', '17538','17539']
        }

port_stp_state = {
        '2326': ['1.3.6.1.2.1.17.2.15.1.3','\033[30;44mdisbl \033[0m ','\033[30;41mdscrd \033[0m ','', 'lerning', '\033[30;43m frwd \033[0m '],
        '2328': ['1.3.6.1.2.1.17.2.15.1.3','\033[30;44mdisbl \033[0m ','\033[30;41mdscrd \033[0m ','', 'lerning', '\033[30;43m frwd \033[0m '],
        '1210-28': ['.1.3.6.1.4.1.171.10.75.15.2.6.2.1.12','\033[30;44mdisbl \033[0m ','\033[30;41mdscrd \033[0m ','', 'lerning', '\033[30;43m frwd \033[0m '],
        '1228': ['1.3.6.1.4.1.171.12.15.2.5.1.6','other','\033[30;44mdisbl \033[0m ','\033[30;41mdscrd \033[0m ', 'lerning', '\033[30;43m frwd \033[0m ','broken','non-stp','err-disabled'],
        '3052': ['1.3.6.1.4.1.171.12.15.2.5.1.6','','\033[30;44mdisbl \033[0m ','\033[30;41mdscrd \033[0m ', 'lerning', '\033[30;43m frwd \033[0m '],
        '3028': ['1.3.6.1.4.1.171.12.15.2.5.1.6','','\033[30;44mdisbl \033[0m ','\033[30;41mdscrd \033[0m ', 'lerning', '\033[30;43m frwd \033[0m '],
        '3200-28': ['1.3.6.1.4.1.171.12.15.2.5.1.6','other','\033[30;44mdisbl \033[0m ','\033[30;41mdscrd \033[0m ', 'lerning', '\033[30;43m frwd \033[0m ','broken','non-stp','err-disabled'],
        '3200-52': ['1.3.6.1.4.1.171.12.15.2.5.1.6','other','\033[30;44mdisbl \033[0m ','\033[30;41mdscrd \033[0m ', 'lerning', '\033[30;43m frwd \033[0m ','broken','non-stp','err-disabled'],
        'linksys': ['1.3.6.1.2.1.17.2.15.1.3','\033[30;44mdisbl \033[0m ','\033[30;41mdscrd \033[0m ','', 'lerning', '\033[30;43m frwd \033[0m '],
        'Fiber_XL': ['1.3.6.1.4.1.3807.2.1908.14.1.3.0','\033[30;44mdisbl \033[0m ','\033[30;41mdscrd \033[0m ', 'lerning', '\033[30;43m frwd \033[0m ','\033[30;43m frwd \033[0m '],
        'Fiber_X':  ['1.3.6.1.4.1.3807.2.1908.14.1.3.0','\033[30;44mdisbl \033[0m ','\033[30;41mdscrd \033[0m ', 'lerning', '\033[30;43m frwd \033[0m ','\033[30;43m frwd \033[0m ']
        }


def format_mac_snmp(macvalue):
    mac=struct.unpack("BBBBBBBB",macvalue)[2:]
    mac_hex=''
    for x in mac: mac_hex=mac_hex+hex(x).split('x')[-1].zfill(2)+':'
    return mac_hex[:17]


ISOK=0
MAC_EQUAL=''
MAC_EQUAL_TEMP=''
COUNTER=0
with open(file) as f:
    for line in f:
        HARDWARE=''

        #MAC_EQUAL_TEMP=''
        if line.rstrip()=='--':
            COUNTER=COUNTER+1
            print('------------------------------------------------------  delimiter  ----------------------------------------------------------')
            sys.stdout.write(str(COUNTER)+' : ')
            if ISOK==3:
                print('GOOD')
                #os.system("clear")
            else:
                #print(ISOK)
                #sys.stdout.write('\033[36m')
                #sys.stdout.write('+----------------------------+\n')
                sys.stdout.write('\033[30;44m      BAD     \033[0m\n')
                #sys.stdout.write('+----------------------------+\033[0m\n')
            ISOK=0
            MAC_EQUAL_TEMP=''
            MAC_EQUAL=''
            print('------------------------------------------------------  delimiter  ----------------------------------------------------------')
            continue
        HARDWARE=typedev(line.rstrip())
        if HARDWARE=='\033[31mnotresp \033[0m':
            print('Device '+ line.rstrip()+' not responding.')
            continue
        HARDWARE=typedev(line.rstrip())
        if HARDWARE=='unknown':
            print('Device '+ line.rstrip()+' unknown type.')
            continue
        try:
            sysname = get(line.rstrip(), COMMUNITY, '1.3.6.1.2.1.1.5.0')
        except (IOError, Exception) as e:
            sys.stdout.write('')
        sys.stdout.write('\033[31mIP:\033[0m '+line.rstrip().ljust(15)+' '+str(sysname.decode("utf-8")).ljust(18)+'\033[31mType:\033[0m '+HARDWARE.ljust(8)+' \033[31mStp status:\033[0m  ')

        try:
            snmp_result = get(line.rstrip(), COMMUNITY, str(stp_enabled[HARDWARE][0]))
        except (IOError, Exception) as e:
            sys.stdout.write('')
            #continue
        try:
            sys.stdout.write(stp_enabled[HARDWARE][int(snmp_result)].ljust(10))
            if str(stp_enabled[HARDWARE][int(snmp_result)])=='\033[30;41m disabled \033[0m':
                print()
                continue
        except (IOError, Exception) as e:
            sys.stdout.write('  stpERR  '.ljust(10))

        try:

            snmp_root = get(line.rstrip(), COMMUNITY, str(stp_rootbridge[HARDWARE]))
            sys.stdout.write('\033[31m  Root: \033[0m'+format_mac_snmp(snmp_root).ljust(15)+' ')
            MAC_EQUAL_TEMP=MAC_EQUAL
            MAC_EQUAL=format_mac_snmp(snmp_root)

        except (IOError, Exception) as e:
            sys.stdout.write('        rootERR      '.ljust(17))

        try:

            snmp_root = get(line.rstrip(), COMMUNITY, str(stp_priority[HARDWARE]))
            if snmp_root!=32768 :  sys.stdout.write('\033[31m Priority: \033[0m\033[34m' + str(snmp_root).ljust(6)+'\033[0m')
            else: sys.stdout.write('\033[31m Priority: \033[0m' + str(snmp_root).ljust(6))
            if snmp_root==4096 or snmp_root==8192:ISOK=ISOK+1
        except (IOError, Exception) as e:
            sys.stdout.write('              prioERR '.ljust(17))

        try:
            sys.stdout.write('\033[31m Ports: '+'\033[0m [ ')
            for ports in port_uplink[HARDWARE]:
                TMP_PORT=ports
                if (HARDWARE=='2326' or HARDWARE=='2328'):
                    huawei_china_strange_portnumber = get(line.rstrip(), COMMUNITY, '1.3.6.1.2.1.17.1.4.1.2.'+ports)
                    portstatus = get(line.rstrip(), COMMUNITY, '1.3.6.1.2.1.2.2.1.8.'+str(huawei_china_strange_portnumber))
                else:
                    portstatus = get(line.rstrip(), COMMUNITY, '1.3.6.1.2.1.2.2.1.8.'+ports)
                    #portstatus=1
                if portstatus==1 :
                    #sys.stdout.write('\033[30;41m'+' up '+'\033[0m'.ljust(5))
                    if(HARDWARE=='1210-28' or HARDWARE=='2326' or HARDWARE=='2328' or HARDWARE=='linksys' or HARDWARE=='Fiber_XL'or HARDWARE=='Fiber_X'):
                        stp_portstatus = get(line.rstrip(), COMMUNITY, port_stp_state[HARDWARE][0]+'.'+ports)
                        #sys.stdout.write('+'+port_stp_state[HARDWARE][0]+'.'+ports+'<<<<<<<<<'+str(stp_portstatus))
                    else:
                        stp_portstatus = get(line.rstrip(), COMMUNITY, port_stp_state[HARDWARE][0]+'.'+ports+'.0')
                        if get(line.rstrip(), COMMUNITY, '1.3.6.1.4.1.171.12.15.2.4.1.4.'+ports)==2:stp_portstatus=2
                    #sys.stdout.write(str(stp_portstatus))
                    sys.stdout.write(str(port_stp_state[HARDWARE][int(stp_portstatus)]))
                    if str(port_stp_state[HARDWARE][int(stp_portstatus)])=='\033[30;41mdscrd \033[0m ':ISOK=ISOK+1
                else:
                    sys.stdout.write(' down '.ljust(7))
                    if(HARDWARE=='3028') :
                        if (get(line.rstrip(), COMMUNITY, '.1.3.6.1.4.1.171.12.15.2.5.1.7.'+ports+'.0')==6):sys.stdout.write('nonstp'.ljust(7))
                ports=TMP_PORT
            sys.stdout.write(']')
        except (IOError, Exception) as e:
            print('\033[30;44m           ERR'.ljust(28)+'\033[0m]')
            #print()
            continue
        if MAC_EQUAL_TEMP!='':
            if MAC_EQUAL_TEMP!=MAC_EQUAL : ISOK=ISOK-1
        if HARDWARE=='2326':print('\033[32m               --> [ Pass ]\033[0m')
        else: print('\033[32m --> [ Pass ]\033[0m')
print('')
