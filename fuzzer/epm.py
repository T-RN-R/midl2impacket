"""This module acts as a lookup for string bindings that are not in the target's epm"""

mappings = {
"82273FDC-E32A-18C3-3F78-827929DC23EA" : r'ncacn_np:%s[\PIPE\eventlog]',
'12345678-1234-ABCD-EF00-0123456789AB' : r'ncacn_np:%s[\PIPE\spoolss]',

}
def get_mapping(uuid, hostname):
    return mappings[uuid] % hostname