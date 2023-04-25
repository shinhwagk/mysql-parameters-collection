import json


def append_detail(version, category, parameter):
    p = parameter
    with open(f'{version}-{category}.json', 'r') as f:
        psdtl = json.load(f)
    for ps in psdtl:
        if 'System Variable' in ps and ps['System Variable'] == p['Name']:
            for k in dict(ps).keys():
                if k.startswith('Type ('):
                    p['Type'] = ps[k]
                    break
                if k == 'Type':
                    p['Type'] = ps[k]
                    break

            for k in dict(ps).keys():
                if k.startswith('Default Value'):
                    if 'Windows' in k or 'Mac' in k or 'windows' in k and 'mac' in k:
                        pass
                    else:
                        p['Default Value'] = ps[k]
                        break
            if 'Deprecated' in ps:
                p['Deprecated'] = ps['Deprecated']
            else:
                p['Deprecated'] = 'none'


def main(version):
    with open(f'{version}-all.json', 'r') as f:
        psall = json.load(f)

    for p in psall:
        # if p['Name'] == 'innodb_buffer_pool_instances':
        p['Version'] = version
        append_detail(version, 'system', p)
        append_detail(version, 'perf', p)
        append_detail(version, 'rep', p)
        append_detail(version, 'innodb', p)
        if not 'Type' in p:
            p['Type'] = ''
            p['Default Value'] = ''

    with open(f'{version}-all-merge.json', 'w') as f:
        json.dump(psall, f)


main('8.0')
main('5.7')


with open(f'8.0-all-merge.json', 'r') as f:
    p80all = json.load(f)

with open(f'5.7-all-merge.json', 'r') as f:
    p57all = json.load(f)

with open(f'9999-all-merge.json', 'w') as f:
    json.dump(p80all + p57all, f)
